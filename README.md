# VR-Treadmill

script that converts mouse movement into joystick movement for a VR treadmill.
(requires Python3)

to bind the virtual gamepad using steam input, open the script in a text editor and comment out the indicated line. when the bind is set up, uncomment the line and restart the script.

REQUIRED:
pynput
vgamepad

FUTURE IDEAS:
using an openxr library to directly control the game instead of a virtual xbox360 controller

# Golly's Version

Instead of doing a hard reset, there's now more of a decay so there's not so much jitter. Also reworked some things. Hope this helps! :D

## Golly's Plan

### Realistic Plans

- **Speed**: Get the speed tracker to roughly calculate a general speed for walking vs jogging vs sprinting. It may not need to differentiate between these three, but I want it to be able to increment rather than going full force for 2 miles an hour.
- **Joystick Movement**: The joystick needs to push a little bit for walking, a little more for jogging, and even more for sprinting. Need to sort this out and smooth out this movement
- **Display**: I realized that I'm testing the treadmill across the room so having a bar that visibly changes is much better for testing (that way I don't have to open up steam and squint at the left joystick to see what it's doing). May want to build on this a little bit to make it nicer

### Optimistic Plans

- **Controller Mocking**: As fer sler mentioned, using an openxr library to control the game may be better, or mocking more of the controller. Depending on the bindings needed, one could, theoretically, make it so sprinting actually triggers the sprint action of the game you're playing once you get to a certain speed. The current problem, though, is the jankiness of the setup. We're losing track of how fast the user is going after a certain speed, so we may have to settle for a "oh I've lost track of how fast you're going, I guess you're sprinting now" mode. Still in the process of fine tuning things.

## Golly's Notes

- On 9/25 sometime in the evening I tested it and it worked much more gradually in speed but I'm not totally happy with it, trying new things tomorrow
- As of 9/25 1:15PM EST I haven't had a chance to test this out properly. It theoretically works but I need to hop in-game to test it and I'm technically on lunch rn :P
