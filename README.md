# ViNE
A basic visual novel engine written in python 3

## Components
ViNE is made up of several parts:

* game.py
* config.py
* script.py

### game.py
This is the engine proper.

### config.py
This holds references to statics assets, paths to asset folders on the 
file system, script command references and colours.

### script.py
This file allows one to create a scenario to tell a story using ViNE. 
You can define custom assets here, such as background music, sound effects, 
background images, sprites and colours, using variables to ease script 
maintenance.

The script is a 2D list with each sub-list holding a particular command 
and an object containing information pertaining to that command.

## Script commands
The following is a list of script commands and options that must be 
provided.

### CHAPTER
* number (not set by user)
* title

Define the current chapter title, allowing you to divide up your story 
while acting as a useful reference for where you are in a save file.

Holds a number which is automatically incremented.

### BG_IMG
* file

Change the current background image.

### SPRITE
* reference
* file
* x
* y

Add / Update a stored sprite to the specified coordinates.

A unique reference is used to keep track of each sprite.

### SPRITE_REMOVE
* reference

Remove the specified sprite from storage.

### BGM
* file

Play a music track.

### BGM_STOP
Stop any playing music tracks.

### SFX
* file

Play a sound effect.

### TEXT
* speaker
* body
* speaker_colour
* body_colour

Display text in the text box. Speaker can be left blank to indicate 
narration. Speaker and body text can each be given a base colour.

The body allows for various inline formatting options:

* Bold: `[b] Hello [/b] world!`
* Italic: `[i] Hello [/i] world!`
* Underline:  `[u] Hello [/u] world!`
* Colour:  `(255,0,0) Hello world!`

Formatting tags should not contain spaces but should be surrounded 
by spaces due to the way text is parsed.
