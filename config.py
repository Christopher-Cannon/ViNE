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
  "SCROLLBACK_LIMIT": 25,
  "BLANK_BG": "bg-black.png",
  "HEADING_ORIGIN": (50, 50),
  "DEFAULT_BGM_VOLUME": 6,
  "DEFAULT_SFX_VOLUME": 8,
  "DIALOGUE_BOX": "dialogue-box.png",
  "DIALOGUE_BOX_BTN_YES": "btn-yes.png",
  "DIALOGUE_BOX_BTN_NO": "btn-no.png",
  # Keep this short
  "DIALOGUE_BOX_TEXT": "Are you sure?",
  "DIALOGUE_BOX_ORIGIN": (280, 280),
  "DIALOGUE_BOX_BTN_YES_ORIGIN": (313, 330),
  "DIALOGUE_BOX_BTN_NO_ORIGIN": (496, 330),
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
  "SETTINGS_HEADING_TEXT": " SETTINGS ",
  "SETTINGS_BGM_TEXT": " BGM Volume ",
  "SETTINGS_SFX_TEXT": " SFX Volume ",
  "SETTINGS_BGM_TEXT_ORIGIN": (100, 200),
  "SETTINGS_SFX_TEXT_ORIGIN": (100, 300),
  "SETTINGS_BGM_PLUS_BTN": "btn-settings-plus.png",
  "SETTINGS_BGM_MINUS_BTN": "btn-settings-minus.png",
  "SETTINGS_SFX_PLUS_BTN": "btn-settings-plus.png",
  "SETTINGS_SFX_MINUS_BTN": "btn-settings-minus.png",
  "SETTINGS_BGM_PLUS_BTN_ORIGIN": (450, 200),
  "SETTINGS_BGM_MINUS_BTN_ORIGIN": (550, 200),
  "SETTINGS_SFX_PLUS_BTN_ORIGIN": (450, 300),
  "SETTINGS_SFX_MINUS_BTN_ORIGIN": (550, 300),
  # Save / Load screen
  "SAVE_HEADING_TEXT": " SAVE GAME ",
  "LOAD_HEADING_TEXT": " LOAD GAME ",
  "SAVE_LOAD_BG": "bg-title.png",
  "SAVE_LOAD_PANEL": "panel.png",
  "SAVE_BTN": "btn-save.png",
  "LOAD_BTN": "btn-load.png",
  "SAVE_LOAD_PANEL_ONE_ORIGIN": (80, 150),
  "SAVE_BTN_ONE_ORIGIN": (670, 160),
  "LOAD_BTN_ONE_ORIGIN": (670, 160),
  "SAVE_LOAD_PANEL_TWO_ORIGIN": (80, 300),
  "SAVE_BTN_TWO_ORIGIN": (670, 310),
  "LOAD_BTN_TWO_ORIGIN": (670, 310),
  "SAVE_LOAD_PANEL_THREE_ORIGIN": (80, 450),
  "SAVE_BTN_THREE_ORIGIN": (670, 460),
  "LOAD_BTN_THREE_ORIGIN": (670, 460),
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
  "SCROLLBACK_LINE_SPACING": 40,
  # Credits gallery - requires at least 1 bg image
  "CREDITS_GALLERY": [
    "credits-1.png",
    "credits-2.png",
    "credits-3.png"
  ],
  "CREDITS_BGM": ""
}

# Paths to assets
BG_PATH = 'backgrounds/'
FONT_PATH = 'fonts/'
BGM_PATH = 'music/'
SFX_PATH = 'sounds/'
SPRITE_PATH = 'sprites/'

# Various commands that can be included in scripts
# These can be changes so long as they are followed in the script
TEXT_BOX_HIDE = "TEXT_BOX_HIDE"
TEXT_BOX_SHOW = "TEXT_BOX_SHOW"
CHAPTER = "CHAPTER"
CREDITS = "CREDITS"
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
