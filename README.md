# VR-Treadmill

script that converts mouse movement into joystick movement for a VR treadmill.
(requires Python3)

to bind the virtual gamepad using steam input, open the script in a text editor and comment out the indicated line. when the bind is set up, uncomment the line and restart the script.

# Golly's Version

Instead of doing a hard reset, there's now more of a decay so there's not so much jitter. Also reworked some things. Hope this helps! :D

REQUIRED:
pynput
vgamepad

FUTURE IDEAS:
using an openxr library to directly control the game instead of a virtual xbox360 controller
