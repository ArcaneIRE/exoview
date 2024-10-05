extends Node3D

const DATA = "res://data/testData.json"

var starScene = load("res://star.tscn")

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	createStars(DATA)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

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

func createStars(starDataFile):
	var starDict = loadStarData(starDataFile)
	if starDict == null:
		return null
		
	var starDataArray = starDict["stars"]
	
	for starData in starDataArray:
		var star = starScene.instantiate()
		
		var gLat = starData["GLAT"]
		var gLon = starData["GLON"]
		var dist = starData["dist"]
		
		# Default to 1.0 if not found
		var kR = starData.get("kR", 1.0)  
		var kG = starData.get("kG", 1.0)  
		var kB = starData.get("kB", 1.0)  
		
		if typeof(gLat) != TYPE_STRING and typeof(gLon) != TYPE_STRING and typeof(dist) != TYPE_STRING:			
			star.global_position = galacticToCartesian(gLat, gLon, dist)
			
			var material = StandardMaterial3D.new()
			material.albedo_color = Color(kR,kG,kB)
			material.flags_unshaded = true			#No lighting applied to material
			star.material_override = material
			
			add_child(star)
			
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
	
	#Scale star coordinates
	x *= 30
	y *= 30
	z *= 30

	return Vector3(x, y, z)	
