# stickEmUp
Simple tool to sanity check RC channels on 3DR Solo

## Installation:

1. Copy the files to your Solo (I saved mine in ``/opt/stickEmUp``). FileZilla works great for this, or you can copy/paste with PuTTY.
2. Give both scripts execute permissions with ``chmod +x /opt/stickEmUp/*``

## Solex Setup:

You can run the scripts via SSH or via a remote command in the Solex app. The latter is my preferred method, as it means all you have to do to run the test is push a button within Solex.

I configured two commands in Solex:

- **Quick Stick Test**: This just says "safe to arm" or "not safe to arm".
  - Command: ``/opt/stickEmUp/stickemup_quick.py 2> /dev/null``
- **Verbose Stick Test**: This gives specifics about which axis failed the sanity check. It's harder to read the output quickly though. Use this only if the quick test fails.
  - Command: ``/opt/stickEmUp/stickemup.py 2> /dev/null``
  
## Usage:

I find it works more reliably if you let Solo acquire a GPS lock and pass all the pre-arm checks before you try this. Solex kind of flips out about not being ready to arm if you start moving the sticks before it's ready.

When you're ready to run the test, open "Commands" within Solex and press the "Quick Stick Test" button. Then immediately begin moving the sticks around in all directions (like a stick calibration). Pay attention to the Solex screen while you do this.

After 10 seconds, you should see a notification from Solex. If your controller passed the sanity check, it will say "SAFE TO ARM." If not, it will warn you, and you can run the more verbose stick test to figure out which axis fails.

**Note:** Sometimes Solex calls the command more than once, and the second test will fail since you will have stopped moving the sticks by that time. If you receive a seemingly random "DO NOT ARM YOUR COPTER!" message, that may be why, but I would run another quick stick test just to double check.
