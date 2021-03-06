def getScript():
  # Would recommend using comments to 'bookmark' sections in long scripts
  # so you can C^f for quick access. A ToC might be a good idea too.
  SPR_JANE_HAPPY = "spr-jane-happy.png"
  SPR_JANE_SAD = "spr-jane-sad.png"
  SPR_JANE_SHOCKED = "spr-jane-shocked.png"
  SPR_JANE_BORED = "spr-jane-bored.png"

  SPR_BOB_HAPPY = "spr-bob-happy.png"
  SPR_BOB_SAD = "spr-bob-sad.png"
  SPR_BOB_SHOCKED = "spr-bob-shocked.png"
  SPR_BOB_BORED = "spr-bob-bored.png"

  SPR_FREDERICA_CONFUSED = "spr-frederica-confused.png"
  SPR_FREDERICA_CONTENT = "spr-frederica-content.png"
  SPR_FREDERICA_SLEEPY = "spr-frederica-sleepy.png"

  COL_WHITE = (250, 250, 250)
  COL_RED = (250, 40, 55)
  COL_GREEN = (40, 250, 55)

  # Remove spaces from tuples for correct parsing
  def colour(colour):
    colour_string = "({},{},{})".format(colour[0], colour[1], colour[2])
    return colour_string

  script = [
    ["BG_IMG", {"file": "bg-black.png"}],
    ["TEXT", {
      "speaker": "",
      "body": "Wait  a second, we're not ready yet.",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "",
      "body": "Just a little more...",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "",
      "body": "A little more...",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "",
      "body": "Ok, done. Time to play some music and brighten this place up a bit.",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["CHAPTER", {"title": "Introduction", "file": "chapter-1.png"}],
    ["BG_IMG", {"file": "bg-sea.png"}],
    ["BGM", {"file": "kaleetan.ogg"}],
    # SPRITE reference MUST be unique
    ["SPRITE", 
      {"reference": "bob", "file": SPR_BOB_HAPPY, "x": 50, "y": 120}
    ],
    ["TEXT", {
      "speaker": "Bob", 
      # Multi-line strings are good for long lines
      "body": """Hello and "welcome to ViNE", A.K.A Visual Novel Engine. 
It's a little basic but it has its uses.""",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["SPRITE",
      {"reference": "jane", "file": SPR_JANE_SHOCKED, "x": 670, "y": 220}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "Ah.", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["SPRITE",
      {"reference": "jane", "file": SPR_JANE_HAPPY, "x": 640, "y": 220}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "Hello.", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "ViNE is a simple engine that allows users to create simple linear visual novels.", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "It is powered by a script, sort of like a screenplay but a little more powerful.", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob", 
      "body": """Users can bring in their own assets, backgrounds, 
sprites, sfx and music to be played and displayed when and where they wish.""", 
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob", 
      "body": """Most importantly, text events can be added with or without a speaker. 
The speaker and body text can be coloured differently too.""", 
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob", 
      "body": """[b] And did you know? [/b] Inline text formatting is supported, useful 
for when you need to add a [i] [u] little emphasis [/u] [/i] to your speech.""", 
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob", 
      "body": """The colour of {} individual {} words {} can be changed too.""".format(
        colour(COL_RED),
        colour(COL_GREEN),
        colour(COL_WHITE)
      ), 
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane",
      "body": "And if you want, you can hide the text box.",
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT_BOX_HIDE", {}],
    ["TEXT", {
      "speaker": "", 
      "body": "", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT_BOX_SHOW", {}],
    ["TEXT", {
      "speaker": "Jane",
      "body": "As you might have noticed, the script allows the user to play or stop music.",
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane",
      "body": "Or play sound effects.",
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["SFX", {"file": "btn-click.ogg"}],
    ["TEXT", {
      "speaker": "", 
      "body": "...huh?", 
      "speaker_colour": COL_WHITE,
      "body_colour": (180, 180, 180)}
    ],
    ["SPRITE",
      {"reference": "frederica", "file": SPR_FREDERICA_SLEEPY, "x": 300, "y": 320}
    ],
    ["TEXT", {
      "speaker": "Frederica", 
      "body": "Oh, hello.", 
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["SFX", {"file": "btn-back.ogg"}],
    ["TEXT", {
      "speaker": "Frederica",
      "body": "...",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["TEXT", {
      "speaker": "Frederica",
      "body": "Stop that.",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["SPRITE",
      {"reference": "frederica", "file": SPR_FREDERICA_CONTENT, "x": 300, "y": 320}
    ],
    ["SPRITE",
      {"reference": "bob", "file": SPR_BOB_BORED, "x": 50, "y": 120}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": """Sprites can be added and removed easily through 
the script, great for quickly changing character expressions or 
moving them around.""", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "You just need to specify the filename and the coordinates (origin in top left).", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": """So long as you provide a unique reference for each 
sprite, the engine will keep track of them all automatically.""", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "And with that, it's time for me to go.", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["SPRITE_REMOVE", {"reference": "jane"}],
    ["CHAPTER", {"title": "The second part", "file": "chapter-2.png"}],
    ["BG_IMG", {"file": "bg-trees.png"}],
    ["TEXT", {
      "speaker": "Frederica",
      "body": "The scenery changes fast around here doesn't it.",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["SPRITE",
      {"reference": "bob", "file": SPR_BOB_HAPPY, "x": 100, "y": 120}
    ],
    ["SPRITE",
      {"reference": "frederica", "file": SPR_FREDERICA_CONTENT, "x": 550, "y": 320}
    ],
    ["TEXT", {
      "speaker": "Bob",
      "body": """Another feature is that you can specify chapters for your story, 
the numbering auto-increments too!""",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob",
      "body": """As you have likely noticed, a splash image is displayed to indicate 
The move to a new chapter. Saving the game will reflect this in the file view.""",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Frederica",
      "body": """Saving and loading is an important feature, you can have three 
different save files at once. A dialogue box helps you avoid accidental clicks too.""",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["TEXT", {
      "speaker": "Frederica",
      "body": """Also, if you miss what someone has said, you can review the 
conversation so far using the scrollback log.""",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["TEXT", {
      "speaker": "Frederica",
      "body": """Use the mouse wheel or up and down keys to navigate. Pressing 
the escape key will return you to the game.""",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["SPRITE",
      {"reference": "bob", "file": SPR_BOB_HAPPY, "x": 200, "y": 120}
    ],
    ["SPRITE",
      {"reference": "frederica", "file": SPR_FREDERICA_CONTENT, "x": 500, "y": 320}
    ],
    ["TEXT", {
      "speaker": "Bob",
      "body": """Well, that's all for now. Until next time.""",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Frederica",
      "body": """...it's impressive how long a short script like this can get...""",
      "speaker_colour": COL_GREEN,
      "body_colour": (220, 220, 220)}
    ],
    ["BGM_STOP", {}],
    ["BG_IMG", {"file": "bg-black.png"}],
    ["SPRITE_REMOVE", {"reference": "bob"}],
    ["SPRITE_REMOVE", {"reference": "frederica"}],
    ["TEXT", {
      "speaker": "",
      "body": """Next are the credits""",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["CREDITS", {}]
  ]

  for i in script:
    i.insert(0, 0)

  return script

# Examples of script commands
# Filenames can be entered without concern for paths since they 
# are added later using constants in config.py
def testScript():
  # You can set colours and assets using constants
  # Prefix with COL_ to differentiate from config.py colours
  COL_WHITE = (250, 250, 250)
  COL_RED = (250, 40, 55)
  COL_GREEN = (40, 250, 55)

  SPR_JANE_HAPPY = "spr-jane-happy.png"

  # [completed, command, payload] - completed is added before returning
  script = [
    # Show or hide text box
    ["TEXT_BOX_HIDE", {}],
    ["TEXT_BOX_SHOW", {}],
    # Move to credits
    ["CREDITS", {}],
    # Update chapter title and splash
    ["CHAPTER", {"title": "This is chapter one", "file": "bg-chapter-1.png"}],
    # Add / Update background image (Removal?)
    ["BG_IMG", {"file": "bg-sea.png"}],
    # Add / Update sprite
    ["SPRITE",
     {"reference": "jane", "file": SPR_JANE_HAPPY, "x": 480, "y": 70}
    ],
    # Remove sprite
    ["SPRITE_REMOVE", {"reference": "jane"}],
    # Play background music (only one at a time)
    ["BGM", {"file": "filename.mp3"}],
    # Stop background music
    ["BGM_STOP", {}],
    # Play a sound effect
    ["SFX", {"file": "filename.mp3"}],
    # Text to be displayed in the text box
    # The colour of the speaker and body text can be changed
    ["TEXT", {
      "speaker": "Jane",
      "body": "The one speaking here is Jane.",
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    # Omitting the speaker will prevent it being drawn, good for narration
    # The body can be omitted in the same way, but a blank text box 
    # might look strange
    ["TEXT", {
      "speaker": "",
      "body": "This text has no speaker, indicated narration.",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    # Longer lines can be written with multi-line strings
    # Character limit for a single TEXT line (with this font 
    # and at this font size) is 267 chars
    ["TEXT", {
      "speaker": "Bob",
      # Multi-line strings are good for long lines
      "body": """Text body goes here. This line is to 
test the limits of small text. It has gotten quite long. 
Still testing the limits of sentence length. It keeps 
getting longer. I am running out of things to say here, 
but I will add this at the end just in case. This is 
the limit.""",
      "speaker_colour": COL_GREEN,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "Bob",
      # Multi-line strings are good for long lines
      "body": """[b] This [i] is [u] {} demonstrating, [/b] how 
inline [/u] text formatting [/i] {} works.""".format(
        colour(COL_GREEN), colour(COL_WHITE)
      ),
      "speaker_colour": COL_GREEN,
      "body_colour": COL_WHITE}
    ]
  ]

  for i in script:
    i.insert(0, 0)

  return script
