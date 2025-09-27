# WARNING

This project is majorly in development and occasionally may not work fully. I'm often in and out, making updates and pushing changes/notes/thoughts to my branch. I'll remove this when it's in a more stable position, but feel free to parse through old versions, some were very close to functional!

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

- **Controller Mocking**: As fer sler mentioned, using an openxr library to control the game may be better, or mocking more of the controller. Depending on the bindings needed, one could, theoretically, make it so sprinting actually triggers the sprint action of the game you're playing once you get to a certain speed. The current problem, though, is the jankiness of the setup. We're losing track of how fast the user is going after a certain speed, so we may have to settle for a "oh I've lost track of how fast you're going, I guess you're sprinting now" mode. Still in the process of fine tuning things

## Golly's Notes (if you try to read them, they are in reverse order, most recent at the top)

- 9:55AM After experimenting with my own xbox 360 controller, I can confirm: it doesn't work. In order to get half life 2 to work (and probably many other games) I will need to use openxr to make a virtual vr controller, pass through the inputs from the actual vr controllers, and pass through the mouse input. This changes... a lot of things. Because of this, I'm going to rework this project a bit to explain.
- 9:23AM I tried half life 2 but there's a major problem: the menu uses the mouse itself to navigate, which is being repeatedly reset, making navigation very difficult. Also, the solution doesn't seem to work right now, at least with my through-setup for fer sler's code. I'm going to try resetting to the original fer sler solution, and see if half life 2 works then
- 8:11AM Ope fer sler didn't play half life 2, he played Alyx, a much more expensive game :( so I'm going to have to rely on comparing this program that I've modified from one other person who made it in around 45 minutes, with the no-doubt massively maintained and team-constructed product which has been developed over years that is reWASD. So I'm sure there will be differences
- 7:53AM I continue to struggle with Portal 2. I'm thinking of getting Half Life 2 for myself that way I can play it on vr and compare my experience with fer sler and bheeks. Portal 2 consistently moves backwards slowly when at rest and I have no clue if that's a bug with Portal 2, or with my setup. I'm thinking that going with Half Life 2 I can watch both the other videos and see how their programs function.

##### 9/27

- 7:10PM Pack it in, boys, I'm restarting from fer sler's solution. The data I have is as follows:

  - Fer Sler got half life 2 to work (I don't have this game except for friend share and I can't get the vr with friend share, sadly) which is a flatscreen to VR game.
  - Portal 2 "works" with Fer Sler's original code, but goes backwards for some reason???
  - Decay is promising, but needs to be stripped away so I can handle more raw input for this thing. Any smoothing and editing is removed in favor of the raw input data so I can get a better grasp. Once again, I have overcomplicated something and made it a mess. I will, however, save the code so I can pull in elements once the base input is ready.
  - Skyrim VR is not a good test game because of long load times and bad character movement overall. Portal 2 is very promising
  - Valheim also, sadly, doesn't recognize the Maratron for me. At least not without reWASD.
  - speed = distance / time (thanks grade school)
  - general things for consideration:
    - when the mouse hits the edge of the screen before resetting, it stops registering the speed
      - this could, theoretically, also be used to my advantage? If we're hitting the bounds of the screen, we are going "max speed". I don't necessarily want to rely on this, however, as I tried an iteration with, like, "zones" where it'd do a hardcoded 25% for walking, 75% for jogging, 100% for sprinting, but it feels weird like this
    - Some games may have an issue with registering both an xbox 360 controller AND an oculus controller at the same time. So far, Portal 2 is not one of those games

- 6:12PM Inexplicably, with fer sler's code in Portal 2 my character moves backwards EXCEPT for when I am walking on the treadmill (in which case I move forward). Going to work on the code some more...
- 9/26 6:10PM Nope I did the test and it works fine. It's JUST this program that won't be recognized. I'm going to try reverting back to fer sler's version to see if it's my own code that's the issue.
- On 9/26 at around 6:00PM Still bugged about what I realized earlier: I'm going to try a few experiments to see if my hunch is right about the double controller situation. Gonna plug in a 360 controller I have and see if I can use that and my Oculus at the same time. If I can, then there's something odd going on with the script. If I can't, then the issue is that these VR games (at least the modded VR games thus far, Valheim and Portal 2 so far) don't allow for multiple controller inputs at the same time.
- On 9/26 at around 2:50PM (during another lunch :P): Realized a major flaw during lunch when trying to play Valheim. We're mocking two controllers into one, and I don't think this works on all games. There are a few possibilities on how to work this, but none of them are very ideal. Here's what I'm thinking:
  - Get HIDHide and hide the controller inputs from all games, then have this program create a virtual oculus controller set and map through all the controller input that it sees from the real oculus controllers, EXCEPT the left analog stick, which it will use some algorithm to read the mouse movements for (still a work in progress). Would need to be configured for any other controllers, and is going to be obnoxious to sort through.
  - Use Universal Control Remapper or some similar tool to remap both the xbox 360 controller input, and the oculus input, to one output. Seems to be several years out of date but I'm a C# dev so I may be able to figure it out?
- On 9/25 sometime in the evening I tested it and it worked much more gradually in speed but I'm not totally happy with it, trying new things tomorrow
- As of 9/25 1:15PM EST I haven't had a chance to test this out properly. It theoretically works but I need to hop in-game to test it and I'm technically on lunch rn :P
