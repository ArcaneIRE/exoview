extends Node3D

const DATA_DIR = "res://data/"
var planetArray = []
var currentPlanet = 0

const MATERIAL_DIR = "res://assets/PlanetTextures/"
var matArray = []

const STAR_RADIUS = 500
const MIN_APP_BRIGHTNESS = 7
const MAX_APP_BRIGHTNESS = -20

const MIN_BRIGHNESS_MULT = 1
const MAX_BRIGHTNESS_MULT = 8
const MIN_SIZE = 1
const MAX_SIZE = 15

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
			var appMag = absMag + 5 * (log(dist) / log(10) - 1)
			if appMag <= 6:		
				star.global_position = galacticToCartesian(gLat, gLon, STAR_RADIUS)
				
				var material = StandardMaterial3D.new()				
				
				var star_type = randi() % 5  # Randomly choose a star type
				var color:Color
				match star_type:
					0: color =  Color(1,0.613,0.338)
					1: color =  Color(0.618, 0.704, 1.0)
					2: color =  Color(0.807, 0.828, 1.0)
					3: color =  Color(1, 1, 1)
					4: color =  Color(1, 0.89, 0.869)
			
				material.emission = color
			
				material.emission_enabled = true
		
				material.emission_energy_multiplier = remap(appMag, MIN_APP_BRIGHTNESS, MAX_APP_BRIGHTNESS, MIN_BRIGHNESS_MULT, MAX_BRIGHTNESS_MULT) 
				star.material_override = material
				
				var sphereMesh = SphereMesh.new()
				
				var sizeScalar = remap(appMag, MIN_APP_BRIGHTNESS, MAX_APP_BRIGHTNESS, MIN_SIZE, MAX_SIZE)
								
				sphereMesh.radius = 0.5 * sizeScalar
				sphereMesh.height = 1 * sizeScalar
				
				star.mesh = sphereMesh

				add_child(star)


func get_random_color(min_rgb: Vector3, max_rgb: Vector3) -> Color:
	var r = randf_range(min_rgb.x, max_rgb.x)
	var g = randf_range(min_rgb.y, max_rgb.y)
	var b = randf_range(min_rgb.z, max_rgb.z)
	return Color(r, g, b)

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
