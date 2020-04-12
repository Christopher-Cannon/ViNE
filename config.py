assets = {
  # General
  "BTN_CLICK_SFX": "btn-click.ogg",
  "BTN_BACK_SFX": "btn-back.ogg",
  "BODY_FONT": "MonospaceTypewriter.ttf",
  "SPEAKER_FONT": "MonospaceTypewriter.ttf",
  "FONT_SIZE_SMALL": 20,
  "FONT_SIZE_MEDIUM": 35,
  "FONT_SIZE_LARGE": 50,
  "BACK_BTN": "btn-back.png",
  "BACK_BTN_ORIGIN": (700, 610),
  "SCROLLBACK_LIMIT": 10,
  "BLANK_BG": "bg-black.png",
  # Title screen
  "TITLE_BG": "bg-title.png",
  "TITLE_BGM": "no-time.ogg",
  "TITLE_START_BTN":"btn-title-start.png",
  "TITLE_LOAD_BTN": "btn-title-load.png",
  "TITLE_SETTINGS_BTN": "btn-title-settings.png",
  "TITLE_QUIT_BTN": "btn-title-quit.png",
  "TITLE_START_BTN_ORIGIN": (700, 280), # Top Left
  "TITLE_LOAD_BTN_ORIGIN": (700, 390),
  "TITLE_SETTINGS_BTN_ORIGIN": (700, 500),
  "TITLE_QUIT_BTN_ORIGIN": (700, 610),
  # Settings screen
  "SETTINGS_BG": "bg-title.png",
  "SETTINGS_BGM_TEXT": " BGM Volume ",
  "SETTINGS_SFX_TEXT": " SFX Volume ",
  "SETTINGS_TEXT_TEXT": " Text Speed ",
  "SETTINGS_BGM_TEXT_ORIGIN": (100, 100),
  "SETTINGS_SFX_TEXT_ORIGIN": (100, 250),
  "SETTINGS_TEXT_TEXT_ORIGIN": (100, 400),
  "SETTINGS_BGM_PLUS_BTN": "btn-settings-plus.png",
  "SETTINGS_BGM_MINUS_BTN": "btn-settings-minus.png",
  "SETTINGS_SFX_PLUS_BTN": "btn-settings-plus.png",
  "SETTINGS_SFX_MINUS_BTN": "btn-settings-minus.png",
  "SETTINGS_TEXT_PLUS_BTN": "btn-settings-plus.png",
  "SETTINGS_TEXT_MINUS_BTN": "btn-settings-minus.png",
  "SETTINGS_BGM_PLUS_BTN_ORIGIN": (400, 100),
  "SETTINGS_BGM_MINUS_BTN_ORIGIN": (600, 100),
  "SETTINGS_SFX_PLUS_BTN_ORIGIN": (400, 250),
  "SETTINGS_SFX_MINUS_BTN_ORIGIN": (600, 250),
  "SETTINGS_TEXT_PLUS_BTN_ORIGIN": (400, 400),
  "SETTINGS_TEXT_MINUS_BTN_ORIGIN": (600, 400),
  # Save / Load screen
  "SAVE_LOAD_BG": "bg-title.png",
  "SAVE_LOAD_PANEL": "",
  "SAVE_BTN": "",
  "LOAD_BTN": "",
  # Game screen
  "TEXT_BOX": "text-box.png",
  "TEXT_BOX_ORIGIN": (0, 550),
  "SPEAKER_BOX_ORIGIN": (0, 505),
  # Origin of text to display
  "TEXT_BODY_ORIGIN": (10, 570),
  "TEXT_BODY_LINE_SPACING": 35,
  # How far text can go before wrapping to a new line
  "TEXT_BODY_BOUNDS": 840,
  "GAME_SAVE_BTN": "btn-game-save.png",
  "GAME_LOAD_BTN": "btn-game-load.png",
  "GAME_LOG_BTN": "btn-game-log.png",
  "GAME_QUIT_BTN": "btn-game-quit.png",
  "GAME_SAVE_BTN_ORIGIN": (850, 560),
  "GAME_LOAD_BTN_ORIGIN": (850, 600),
  "GAME_LOG_BTN_ORIGIN": (850, 640),
  "GAME_QUIT_BTN_ORIGIN": (850, 680),
  "SCROLLBACK_BOX": "scrollback-box.png",
  "SCROLLBACK_LINE_SPACING": 40
}

# Paths to assets
BG_PATH = 'backgrounds/'
FONT_PATH = 'fonts/'
BGM_PATH = 'music/'
SFX_PATH = 'sounds/'
SPRITE_PATH = 'sprites/'

# Various commands that can be included in scripts
# These can be changes so long as they are followed in the script
CHAPTER = "CHAPTER"
BG_IMG = "BG_IMG"
SPRITE = "SPRITE"
SPRITE_REMOVE = "SPRITE_REMOVE"
BGM = "BGM"
BGM_STOP = "BGM_STOP"
SFX = "SFX"
TEXT = "TEXT"

# Colours
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
