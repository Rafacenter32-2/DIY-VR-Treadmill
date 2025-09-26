
 #   print(f"\rSPD:{speed:4.0f} JOY: [{joystick_bar}] {mousey:5}", end='', flush=True)

import time
from pynput.mouse import Button, Controller
import vgamepad as vg
from collections import deque

gamepad = vg.VX360Gamepad()
mouse = Controller()

# Speed tracking
mouse_positions = deque(maxlen=20) # Store the last 20 positions
timestamps = deque(maxlen=20) # store their corresponding timestamps

peak_speed = 0

# Parameters
COUNTDOWN = 10

def create_bar(value, max_value, width, char='█', empty_char='░'):
    if max_value == 0:
        return empty_char * width
    filled = int((value / max_value) * width)
    filled = min(filled, width)
    empty = width - filled
    return char * filled + empty_char * empty

for i in range(COUNTDOWN):
    print("starting in", COUNTDOWN - i)
    time.sleep(1)

while True:
    time.sleep(0.01)

    
    mousey = max(-32768, min(32767, int((mousey1 + mousey2)/2))) # average and clamp
    mouse.position = (700, 500) # COMMENT OUT THIS LINE WITH A # SYMBOL TO MAKE SETTING UP CONTROLLER BINDING EASIER
    print(mousey)
    
    gamepad.left_joystick(x_value=0, y_value=mousey)  # values between -32768 and 32767
    

    gamepad.update()