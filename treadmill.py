import time
from pynput.mouse import Button, Controller
import vgamepad as vg

gamepad = vg.VX360Gamepad()
mouse = Controller()

mousey = 0
mousey1 = 0
mousey2 = 0

# To track change in position (delta)
last_mouse_y = 500
accumulated_value = 0

# Paramters
sensitivity = 7 # Try to stay between 1 and 50
deadzone = 2
decay_rate = 0.92 # How quickly the joystick returns to center
max_speed = 32767 # Maximum joystick value in either positive or negative directions

for i in range(10):
    print("starting in", 10 - i)
    time.sleep(1)

while True:
    time.sleep(0.03)

    # Get the current position
    current_mouse_y = mouse.position[1]

    # Get the change in position (delta)
    mouse_delta = (500 - current_mouse_y)

    if abs(mouse_delta) < deadzone: 
        mouse_delta = 0

    accumulated_value += mouse_delta * sensitivity
    accumulated_value *= decay_rate
    
    mousey = max(-max_speed, min(max_speed, int(accumulated_value))) # convert mouse position to joystick value
    
    # Reset mouse to center
    mouse.position = (700, 500) # COMMENT OUT THIS LINE WITH A # SYMBOL AT THE START OF THE LINE TO MAKE SETTING UP CONTROLLER BINDING EASIER
    
    print(f"Delta: {mouse_delta:3d} | Accumulated: {accumulated_value:7.1f} | Joystick: {mousey:6d}")
    
    gamepad.left_joystick(x_value=0, y_value=mousey)  # values between -32768 and 32767
    
    gamepad.update()
