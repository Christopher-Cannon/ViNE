def getScript():
  script = [
    # [completed, identifier, arguments] - completed is added before returning
    ["BG_IMG", {"file":"main_bg.png", "x":0, "y":0}],
    ["SPRITE", {"file": "bob_bored.png", "x": 180, "y": 50}],
    ["SPRITE", {"file": "jane_happy.png", "x": 480, "y": 70}],
    ["BGM", {"file":"filename.mp3"}],
    ["SFX", {"file":"filename.mp3"}],
    ["BGM_VOLUME", {"volume":0.5}], # Is it a good idea to dynamically change volume during play?
    ["SFX_VOLUME", {"volume":0.5}], # Might be better to remove these
    ["TEXT", {"speaker":"Bob", "body":"Text body goes here."}],
    ["TEXT", {"speaker":"Jane", "body":"Ah."}],
    ["TEXT", {"speaker":"Jane", "body":"That's not right."}]
  ]

  for i in script:
    i.insert(0, 0)

  return script
