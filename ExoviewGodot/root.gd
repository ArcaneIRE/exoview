extends Node3D

var xr_interface: XRInterface

var debugMode = false

enum INTERFACE_MODE {DESKTOP, XR}
var interfaceMode: INTERFACE_MODE

@onready var desktopFPSDisplay = $FirstPersonController/Camera3D/DesktopFPS
@onready var XRFPSDisplay = $XROrigin3D/XRCamera3D/XRFPS

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	xr_interface = XRServer.find_interface("OpenXR")
	if xr_interface and xr_interface.is_initialized():	
		setupXRMode()
	else:
		setupDesktopMode()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	updateFPSDisplay()
	
func _input(event: InputEvent) -> void:
	if event.is_action_pressed("debug"):
		toggleDebugMode()

func setupXRMode():
	interfaceMode = INTERFACE_MODE.XR	
	DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED) # Turn off v-sync
	get_viewport().use_xr = true #Change viewport to output to HMD
	$XROrigin3D/XRCamera3D.current = true
	
func setupDesktopMode():
	interfaceMode = INTERFACE_MODE.DESKTOP
	$FirstPersonController/Camera3D.current = true

func toggleDebugMode():
	debugMode = !debugMode
	
	$FirstPersonController.moveEnabled = debugMode
	
	#FPS displays only show up in debug mode
	desktopFPSDisplay.visible = debugMode && (interfaceMode == INTERFACE_MODE.DESKTOP)
	XRFPSDisplay.visible = debugMode && (interfaceMode == INTERFACE_MODE.XR)
	
	if not debugMode: #Reset player positon and look dir when debug mode turned off
		$FirstPersonController.global_position = Vector3.ZERO
		$FirstPersonController.rotation_degrees = Vector3.ZERO

func updateFPSDisplay():
	var fpsString = "FPS: %d" % Engine.get_frames_per_second()
	desktopFPSDisplay.text = fpsString
	XRFPSDisplay.text = fpsString

func _on_right_controller_button_pressed(name: String) -> void:
	#XR Right Controller Pressed
	if name == "ax_button":
		toggleDebugMode()
