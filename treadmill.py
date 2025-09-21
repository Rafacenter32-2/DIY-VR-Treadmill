import time
from pynput.mouse import Button, Controller
import vgamepad as vg

gamepad = vg.VX360Gamepad()
mouse = Controller()
mousey = 0
mousey1 = 0
mousey2 = 0
mousey3 = 0

sensitivity = 150

for i in range(10):
    print("starting in", 10 - i)
    time.sleep(1)

while True:
    time.sleep(0.03)
    
    mousey2 = mousey1
    mousey1 = 0
    
    mousey1 = (mouse.position[1] - 500) * -(sensitivity) # convert mouse position to joystick value
    
    mousey = max(-32768, min(32767, int((mousey1 + mousey2)/2))) # average and clamp
    mouse.position = (700, 500) # COMMENT OUT THIS LINE WITH A # SYMBOL TO MAKE SETTING UP CONTROLLER BINDING EASIER
    print(mousey)
    
    gamepad.left_joystick(x_value=0, y_value=mousey)  # values between -32768 and 32767
    

    gamepad.update()
