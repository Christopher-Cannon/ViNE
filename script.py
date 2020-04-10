def getScript():
  script = [
    # [completed, identifier, arguments] - completed is added before returning
    ["BG_IMG", {"file": "bg-sea.png"}],
    # SPRITE reference MUST be unique
    ["SPRITE", 
      {"reference": "bob", "file": "bob_bored.png", "x": 180, "y": 50}
    ],
    ["SPRITE", 
      {"reference": "jane", "file": "jane_happy.png", "x": 480, "y": 70}
    ],
    ["CHAPTER", {"number": 1, "title": "Sudden Complications"}],
    ["BGM", {"file": "filename.mp3"}],
    ["SFX", {"file": "filename.mp3"}],
    ["TEXT", {
      "speaker": "Bob", 
      "body": "Text body goes here. This line is to test the limits of small text. It has gone", 
      "size": "small", 
      "speaker_colour": (255, 255, 255),
      "body_colour": (255, 255, 255)}
    ],
    ["SPRITE",
      {"reference": "jane", "file": "jane_shocked.png", "x": 480, "y": 70}
    ],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "Ah.", 
      "size": "small", 
      "speaker_colour": (255, 255, 255),
      "body_colour": (255, 255, 255)}
    ],
    ["BG_IMG", {"file": "bg-trees.png"}],
    ["TEXT", {
      "speaker": "Jane", 
      "body": "That's not right.", 
      "size": "small", 
      "speaker_colour": (255, 255, 255),
      "body_colour": (255, 255, 255)}
    ],
    ["BG_IMG", {"file": "bg-sea.png"}],
    ["CHAPTER", {"number": 2, "title": "Everything's Better Now"}]
  ]

  for i in script:
    i.insert(0, 0)

  return script
