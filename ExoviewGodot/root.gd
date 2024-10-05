extends Node3D

var xr_interface: XRInterface

enum INTERFACE_MODE {DESKTOP, XR}
var interfaceMode: INTERFACE_MODE

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	xr_interface = XRServer.find_interface("OpenXR")
	if xr_interface and xr_interface.is_initialized():	
		setupXRMode()
	else:
		setupDesktopMode()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func setupXRMode():
	interfaceMode = INTERFACE_MODE.XR	
	DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_DISABLED) # Turn off v-sync
	get_viewport().use_xr = true #Change viewport to output to HMD
	$XROrigin3D/XRCamera3D.current = true
	
func setupDesktopMode():
	interfaceMode = INTERFACE_MODE.DESKTOP
	$FirstPersonController/Camera3D.current = true
