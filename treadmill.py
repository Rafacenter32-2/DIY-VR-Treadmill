import time
from pynput.mouse import Button, Controller
import vgamepad as vg
from collections import deque
'''
    Quick note: to end this program hit ctrl+c or ctrl+alt+delete on windows
    if you need to end it abruptly. It should stop the controller and the program
'''
gamepad = vg.VX360Gamepad()
mouse = Controller()
# To track change in position (delta)
last_mouse_y = 500
accumulated_value = 0
# Speed tracking
mouse_positions = deque(maxlen=10)  # Store last 10 position samples
timestamps = deque(maxlen=10) # Store the corresponding timestamps
peak_speed = 0
# Parameters
sensitivity = 7 # Try to stay between 1 and 50
deadzone = 2
decay_rate = 0.92 # How quickly the joystick returns to center
max_speed = 32767 # Maximum joystick value in either positive or negative directions
# NEW: Speed-based boost parameters
min_output_threshold = 8000  # Minimum joystick value when moving (ensures slow walk registers)
speed_deadzone = 10  # Minimum speed (px/s) to count as intentional movement
# Visual Display Parameters
max_pixel_speed = 1000 # Max speed for the bar display, pixels per second
bar_width = 40 # Width of the speed bar

for i in range(10):
    print("starting in", 10 - i)
    time.sleep(1)

# A visual bar to help troubleshooting, even across the room on a treadmill
def create_bar(value, max_value, width, char='█', empty_char='░'):
    if max_value == 0:
        return empty_char * width
   
    filled = int((value / max_value) * width)
    filled = min(filled, width)  # Cap at width
    empty = width - filled
   
    return char * filled + empty_char * empty

while True:
    time.sleep(0.03)
    # Get the current position
    current_mouse_y = mouse.position[1]
    # Trying to calculate time for speed, maybe this will work
    current_time = time.time()
    # Get the change in position (delta)
    mouse_delta = (500 - current_mouse_y)
    # Add to speed tracking buffers
    mouse_positions.append(current_mouse_y)
    timestamps.append(current_time)
    # Calculate speed
    speed = 0
    if len(mouse_positions) >= 2:
        # Get total distance over the time window
        total_distance = 0
        for i in range(1, len(mouse_positions)):
            total_distance += abs(mouse_positions[i] - mouse_positions[i-1])
        # Calculate time span
        time_span = timestamps[-1] - timestamps[0]
        # Calculate pixels per second
        if time_span > 0:
            # I never thought I'd use the equation "speed is distance over time"
            # But here it is
            speed = total_distance / time_span
    # Track peak speed
    if speed > peak_speed:
        peak_speed = speed
    
    if abs(mouse_delta) < deadzone:
        mouse_delta = 0
    
    accumulated_value += mouse_delta * sensitivity
    accumulated_value *= decay_rate
   
    mousey = max(-max_speed, min(max_speed, int(accumulated_value))) # convert mouse position to joystick value
    
    # If we detect movement speed, ensure minimum output
    if speed > speed_deadzone:
        if mousey > 0 and mousey < min_output_threshold:
            mousey = min_output_threshold
        elif mousey < 0 and mousey > -min_output_threshold:
            mousey = -min_output_threshold
    else:
        # If no real speed detected, decay faster to zero
        accumulated_value *= 0.7
   
    # Reset mouse to center
    mouse.position = (700, 500) # COMMENT THIS OUT WITH A # SYMBOL AT THE START OF THE LINE TO MAKE SETTING UP CONTROLLER BINDING EASIER
   
    joystick_bar = create_bar(abs(mousey), max_speed, bar_width)
    print(f"\rSPD:{speed:4.0f} JOY: [{joystick_bar}] {mousey:5}", end='', flush=True)
   
    gamepad.left_joystick(x_value=0, y_value=mousey)  # values between -32768 and 32767
   
    gamepad.update()