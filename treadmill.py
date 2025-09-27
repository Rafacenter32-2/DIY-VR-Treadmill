import time
from pynput.mouse import Button, Controller
import vgamepad as vg

gamepad = vg.VX360Gamepad()
mouse = Controller()
mousey = 0
mousey1 = 0
mousey2 = 0

current_speed = 0
peak_speed = 0

# Parameters
SENSITIVITY = 25
ZERO_FACTOR = 0.7 # How quickly the speed returns to 0 upon stopping
NORMAL_FACTOR = 0.3 # How quickly the joystick's will move towards the mouse speed

COUNT = 10 # The number the program will count down from before locking the cursor

MAX_SPEED = 32768
BAR_WIDTH = 40

def smooth_speed(speed, target_speed):
    diff = target_speed - speed
    if target_speed == 0:
        factor = ZERO_FACTOR
    else:
        factor = NORMAL_FACTOR

    return int(speed + diff * factor)

# A visual bar to help troubleshooting, even across the room on a treadmill
def create_bar(value, max_value, width, char='█', empty_char='░'):
    if max_value == 0:
        return empty_char * width
   
    filled = int((abs(value) / max_value) * width)
    filled = min(filled, width)  # Cap at width
    empty = width - filled
   
    return char * filled + empty_char * empty

for i in range(COUNT):
    print("starting in", COUNT - i)
    time.sleep(1)

while True:
    time.sleep(0.03)
    
    mousey2 = mousey1
    mousey1 = 0
    
    mousey1 = (mouse.position[1] - 500) * -(SENSITIVITY) # convert mouse position to joystick value
    
    mousey = max(-32768, min(32767, int((mousey1 + mousey2)/2))) # average and clamp
    mouse.position = (700, 500) # COMMENT OUT THIS LINE WITH A # SYMBOL TO MAKE SETTING UP CONTROLLER BINDING EASIER
    
    # Adjust the current speed based on the mouse y position rather than jumping straight to that number
    current_speed = smooth_speed(current_speed, mousey)
    if peak_speed < current_speed:
        peak_speed = current_speed
    
    joystick_bar = create_bar(current_speed, MAX_SPEED, BAR_WIDTH)

    print(f"\rJOY: [{joystick_bar}] PEAK SPEED: {peak_speed}", end='', flush=True)
    
    gamepad.left_joystick(x_value=0, y_value=current_speed)  # values between -32768 and 32767

    gamepad.update()