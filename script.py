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

  script = [
    # [completed, command, payload] - completed is added before returning
    ["BG_IMG", {"file": "bg-black.png"}],
    ["TEXT", {
      "speaker": "",
      "body": "Wait a second, we're not ready yet.",
      "size": "small",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "",
      "body": "Just a bit more...",
      "size": "small",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["TEXT", {
      "speaker": "",
      "body": "Ok, done.",
      "size": "small",
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["BG_IMG", {"file": "bg-sea.png"}],
    ["BGM", {"file": "kaleetan.ogg"}],
    # SPRITE reference MUST be unique
    ["SPRITE", 
     {"reference": "bob", "file": SPR_BOB_HAPPY, "x": 50, "y": 120}
    ],
    ["SPRITE", 
     {"reference": "jane", "file": SPR_JANE_BORED, "x": 660, "y": 220}
    ],
    ["CHAPTER", {"title": "Sudden Complications"}],
    ["TEXT", {
      "speaker": "Bob", 
      # Multi-line strings are good for long lines
      "body": """Text body goes here. This line is to test the limits of small text. It has gotten quite long. 
Still testing the limits of sentence length. It keeps getting longer. I am running out of things 
to say here, but I will add this at the end just in case. This is the limit.""",
      "size": "small", 
      "speaker_colour": COL_WHITE,
      "body_colour": COL_WHITE}
    ],
    ["SPRITE",
     {"reference": "jane", "file": SPR_JANE_SHOCKED, "x": 640, "y": 220}
    ],
    ["SFX", {"file": "btn-click.ogg"}],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "Ah.", 
      "size": "small", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["SFX", {"file": "btn-back.ogg"}],
    ["TEXT", {
      "speaker": "", 
      "body": "Oh no.", 
      "size": "small", 
      "speaker_colour": COL_WHITE,
      "body_colour": (150, 150, 150)}
    ],
    ["SPRITE",
     {"reference": "frederica", "file": SPR_FREDERICA_SLEEPY, "x": 280, "y": 320}
    ],
    ["TEXT", {
      "speaker": "Frederica", 
      "body": "Hello.", 
      "size": "small", 
      "speaker_colour": COL_GREEN,
      "body_colour": (200, 200, 200)}
    ],
    ["BG_IMG", {"file": "bg-trees.png"}],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "That's not right.", 
      "size": "small", 
      "speaker_colour": COL_RED,
      "body_colour": COL_WHITE}
    ],
    ["SPRITE_REMOVE", {"reference": "jane"}],
    ["BG_IMG", {"file": "bg-sea.png"}],
    ["BGM_STOP", {}],
    ["CHAPTER", {"title": "Everything's Better Now"}]
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

  script = [
    # Update chapter
    # Could numbering be done automatically?
    ["CHAPTER", {"number": 1, "title": "This is chapter one"}],
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
    ]
  ]

  for i in script:
    i.insert(0, 0)

  return script
