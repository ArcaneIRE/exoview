extends Node3D

const DATA_DIR = "res://data/"
var planetArray = []
var currentPlanet = 0

const MATERIAL_DIR = "res://assets/PlanetTextures/"
var matArray = []

const STAR_RADIUS = 500
const MIN_APP_BRIGHTNESS = 6
const MAX_APP_BRIGHTNESS = -20
const MIN_BRIGHNESS_MULT = 0.0
const MAX_BRIGHTNESS_MULT = 5

var starScene = load("res://star.tscn")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	buildFileArray(DATA_DIR, planetArray)
	buildFileArray(MATERIAL_DIR, matArray)
	setPlanetTexture()
	createStars()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func buildFileArray(dataDir, array):
	var dir = DirAccess.open(dataDir)
	if dir:
		dir.list_dir_begin()
		var fileName = dir.get_next()
		while fileName != "":
			array.append(fileName)
			fileName = dir.get_next()
	
func loadStarData(starDataFile: String):
	var file = FileAccess.open(starDataFile, FileAccess.READ)
	
	if file == null:
		print("Error opening file...")
		return null
	
	var jsonString = file.get_as_text()
	var json = JSON.new()
	var result = json.parse(jsonString)	
	
	if result == OK:
		return json.data
	else:		
		print(json.get_error_message())
		return null

func createStars():
	var starDataFile = DATA_DIR + planetArray[currentPlanet] + "/stars.json"
	
	var starDict = loadStarData(starDataFile)
	if starDict == null:
		return null
		
	var starDataArray = starDict["stars"]
	
	for starData in starDataArray:
		var star = starScene.instantiate()
		
		var gLat = starData["GLAT"]
		var gLon = starData["GLON"]
		var dist = starData["dist"]
		var absMag = starData["absmag"]
		
		if typeof(gLat) != TYPE_STRING and typeof(gLon) != TYPE_STRING and typeof(dist) != TYPE_STRING:			
			star.global_position = galacticToCartesian(gLat, gLon, STAR_RADIUS)
			
			var material = StandardMaterial3D.new()
			
			material.emission = Color(1,1,1)
			material.emission_enabled = true
			
			var appMag = absMag + 5 * (log(dist) / log(10) - 1)
			if appMag <= 6:
			
				material.emission_energy_multiplier = remap(appMag, MIN_APP_BRIGHTNESS, MAX_APP_BRIGHTNESS, MIN_BRIGHNESS_MULT, MAX_BRIGHTNESS_MULT) 
				
				star.material_override = material
				
				add_child(star)

func clearStars():
	for star in get_children():
		star.queue_free()

func setPlanetTexture():
	var material = load(MATERIAL_DIR + matArray[currentPlanet])
	$"../Ground".material_override = material		
		
func cyclePlanets():
	currentPlanet = (currentPlanet + 1) % planetArray.size()
	
	setPlanetTexture()
	clearStars()
	createStars()

func galacticToCartesian(gLat:float, gLong:float, dist:float):
	"""
	Convert Galactic coordinates to Cartesian coordinates.	
	gLat: Galactic latitude in degrees
	gLong: Galactic longitude in degrees
	dist: Distance
	"""
	
	# Convert angles from degrees to radians
	var gLongRad = deg_to_rad(gLong) 
	var gLatRad = deg_to_rad(gLat)

	# Cartesian coordinates conversion
	var x = dist * cos(gLatRad) * cos(gLongRad)
	var y = dist * cos(gLatRad) * sin(gLongRad)
	var z = dist * sin(gLatRad)

	return Vector3(x, y, z)	

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("left_mouse_click"):
		cyclePlanets()

func _on_right_controller_button_pressed(name: String) -> void:
	if name == "ax_button":
		cyclePlanets()
