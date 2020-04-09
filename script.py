def getScript():
  script = [
    # [completed, identifier, arguments] - completed is added before returning
    ["BG_IMG", {"file": "main_bg.png", "x": 0, "y": 0}],
    ["SPRITE", {"file": "bob_bored.png", "x": 180, "y": 50}],
    ["SPRITE", {"file": "jane_happy.png", "x": 480, "y": 70}],
    ["CHAPTER", {"number": 1, "title": "Sudden Complications"}],
    ["BGM", {"file": "filename.mp3"}],
    ["SFX", {"file": "filename.mp3"}],
    ["TEXT", {"speaker": "Bob", "body": "Text body goes here."}],
    ["TEXT", {"speaker": "Jane", "body": "Ah."}],
    ["TEXT", {"speaker": "Jane", "body": "That's not right."}],
    ["CHAPTER", {"number": 2, "title": "Everything's Better Now"}]
  ]

  for i in script:
    i.insert(0, 0)

  return script
