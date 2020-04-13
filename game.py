import script as s
import config as c
import pygame
import math
import re
from pygame import mixer
from enum import Enum

pygame.init()
pygame.display.set_caption("ViNE")

try:
  script = s.getScript()
except:
  print("An error occurred when retrieving the script\nExiting...")
  pygame.QUIT

WIDTH = 960
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ICON = pygame.image.load(c.SPRITE_PATH + 'icon-vine.png')
pygame.display.set_icon(ICON)

###################################################################
# Constants from config.py
###################################################################

# General
BACK_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["BACK_BTN"]).convert_alpha()
BACK_BTN_ORIGIN = c.assets["BACK_BTN_ORIGIN"]

BODY_FONT_SMALL = pygame.font.Font(
    c.FONT_PATH + c.assets["BODY_FONT"], 
    c.assets["FONT_SIZE_SMALL"])

BODY_FONT_MEDIUM = pygame.font.Font(
    c.FONT_PATH + c.assets["BODY_FONT"], 
    c.assets["FONT_SIZE_MEDIUM"])

BODY_FONT_LARGE = pygame.font.Font(
    c.FONT_PATH + c.assets["BODY_FONT"], 
    c.assets["FONT_SIZE_LARGE"])

SPEAKER_FONT = pygame.font.Font(
    c.FONT_PATH + c.assets["SPEAKER_FONT"], 
    c.assets["FONT_SIZE_MEDIUM"])

SCROLLBACK_LIMIT = c.assets["SCROLLBACK_LIMIT"]
BLANK_BG = pygame.image.load(c.BG_PATH + c.assets["BLANK_BG"])
HEADING_ORIGIN = c.assets["HEADING_ORIGIN"]

TEXT_BOLD_PATTERN_START = "\[b\]"
TEXT_BOLD_PATTERN_END = "\[\/b\]"
TEXT_ITALIC_PATTERN_START = "\[i\]"
TEXT_ITALIC_PATTERN_END = "\[\/i\]"
TEXT_UNDERLINE_PATTERN_START = "\[u\]"
TEXT_UNDERLINE_PATTERN_END = "\[\/u\]"
TEXT_COLOUR_PATTERN = "\((\W|\d)+\)"

# Title
TITLE_BACKGROUND = pygame.image.load(c.BG_PATH + c.assets["TITLE_BG"])
TITLE_START_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_START_BTN"]).convert_alpha()
TITLE_LOAD_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_LOAD_BTN"]).convert_alpha()
TITLE_SETTINGS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_SETTINGS_BTN"]).convert_alpha()
TITLE_QUIT_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["TITLE_QUIT_BTN"]).convert_alpha()

TITLE_BGM = c.BGM_PATH + c.assets["TITLE_BGM"]

TITLE_START_BTN_ORIGIN = c.assets["TITLE_START_BTN_ORIGIN"]
TITLE_LOAD_BTN_ORIGIN = c.assets["TITLE_LOAD_BTN_ORIGIN"]
TITLE_SETTINGS_BTN_ORIGIN = c.assets["TITLE_SETTINGS_BTN_ORIGIN"]
TITLE_QUIT_BTN_ORIGIN = c.assets["TITLE_QUIT_BTN_ORIGIN"]

# Game
TEXT_BOX = pygame.image.load(c.SPRITE_PATH + c.assets["TEXT_BOX"]).convert_alpha()
TEXT_BOX_ORIGIN = c.assets["TEXT_BOX_ORIGIN"]

TEXT_BODY_ORIGIN = c.assets["TEXT_BODY_ORIGIN"]
TEXT_BODY_BOUNDS = c.assets["TEXT_BODY_BOUNDS"]
TEXT_BODY_LINE_SPACING = c.assets["TEXT_BODY_LINE_SPACING"]

SPEAKER_BOX_ORIGIN = c.assets["SPEAKER_BOX_ORIGIN"]

GAME_SAVE_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_SAVE_BTN"]).convert_alpha()
GAME_LOAD_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_LOAD_BTN"]).convert_alpha()
GAME_LOG_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_LOG_BTN"]).convert_alpha()
GAME_QUIT_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["GAME_QUIT_BTN"]).convert_alpha()

GAME_SAVE_BTN_ORIGIN = c.assets["GAME_SAVE_BTN_ORIGIN"]
GAME_LOAD_BTN_ORIGIN = c.assets["GAME_LOAD_BTN_ORIGIN"]
GAME_LOG_BTN_ORIGIN = c.assets["GAME_LOG_BTN_ORIGIN"]
GAME_QUIT_BTN_ORIGIN = c.assets["GAME_QUIT_BTN_ORIGIN"]

# Settings
SETTINGS_BG = pygame.image.load(c.BG_PATH + c.assets["SETTINGS_BG"])

SETTINGS_BGM_PLUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_PLUS_BTN"]).convert_alpha()
SETTINGS_BGM_MINUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_MINUS_BTN"]).convert_alpha()
SETTINGS_SFX_PLUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_PLUS_BTN"]).convert_alpha()
SETTINGS_SFX_MINUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_MINUS_BTN"]).convert_alpha()

SETTINGS_BGM_PLUS_BTN_ORIGIN = c.assets["SETTINGS_BGM_PLUS_BTN_ORIGIN"]
SETTINGS_BGM_MINUS_BTN_ORIGIN = c.assets["SETTINGS_BGM_MINUS_BTN_ORIGIN"]
SETTINGS_SFX_PLUS_BTN_ORIGIN = c.assets["SETTINGS_SFX_PLUS_BTN_ORIGIN"]
SETTINGS_SFX_MINUS_BTN_ORIGIN = c.assets["SETTINGS_SFX_MINUS_BTN_ORIGIN"]

SETTINGS_HEADING_TEXT = c.assets["SETTINGS_HEADING_TEXT"]
SETTINGS_BGM_TEXT = c.assets["SETTINGS_BGM_TEXT"]
SETTINGS_SFX_TEXT = c.assets["SETTINGS_SFX_TEXT"]

SETTINGS_BGM_TEXT_ORIGIN = c.assets["SETTINGS_BGM_TEXT_ORIGIN"]
SETTINGS_SFX_TEXT_ORIGIN = c.assets["SETTINGS_SFX_TEXT_ORIGIN"]

# Save / Load
SAVE_LOAD_BG = pygame.image.load(c.BG_PATH + c.assets["SAVE_LOAD_BG"])

SAVE_HEADING_TEXT = c.assets["SAVE_HEADING_TEXT"]
LOAD_HEADING_TEXT = c.assets["LOAD_HEADING_TEXT"]

SAVE_LOAD_PANEL = pygame.image.load(c.SPRITE_PATH + c.assets["SAVE_LOAD_PANEL"]).convert_alpha()

SAVE_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SAVE_BTN"]).convert_alpha()
LOAD_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["LOAD_BTN"]).convert_alpha()
DELETE_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["DELETE_BTN"]).convert_alpha()

SAVE_LOAD_PANEL_ONE_ORIGIN = c.assets["SAVE_LOAD_PANEL_ONE_ORIGIN"]
SAVE_BTN_ONE_ORIGIN = c.assets["SAVE_BTN_ONE_ORIGIN"]
LOAD_BTN_ONE_ORIGIN = c.assets["LOAD_BTN_ONE_ORIGIN"]
DELETE_BTN_ONE_ORIGIN = c.assets["DELETE_BTN_ONE_ORIGIN"]

SAVE_LOAD_PANEL_TWO_ORIGIN = c.assets["SAVE_LOAD_PANEL_TWO_ORIGIN"]
SAVE_BTN_TWO_ORIGIN = c.assets["SAVE_BTN_TWO_ORIGIN"]
LOAD_BTN_TWO_ORIGIN = c.assets["LOAD_BTN_TWO_ORIGIN"]
DELETE_BTN_TWO_ORIGIN = c.assets["DELETE_BTN_TWO_ORIGIN"]

SAVE_LOAD_PANEL_THREE_ORIGIN = c.assets["SAVE_LOAD_PANEL_THREE_ORIGIN"]
SAVE_BTN_THREE_ORIGIN = c.assets["SAVE_BTN_THREE_ORIGIN"]
LOAD_BTN_THREE_ORIGIN = c.assets["LOAD_BTN_THREE_ORIGIN"]
DELETE_BTN_THREE_ORIGIN = c.assets["DELETE_BTN_THREE_ORIGIN"]

# Scrollback
SCROLLBACK_BOX = pygame.image.load(c.SPRITE_PATH + c.assets["SCROLLBACK_BOX"])
SCROLLBACK_LINE_SPACING = c.assets["SCROLLBACK_LINE_SPACING"]

# General rectangles
BACK_BTN_RECT = BACK_BTN.get_rect(topleft=c.assets["BACK_BTN_ORIGIN"])

# Title rectangles
TITLE_START_BTN_RECT = TITLE_START_BTN.get_rect(topleft=TITLE_START_BTN_ORIGIN)
TITLE_LOAD_BTN_RECT = TITLE_LOAD_BTN.get_rect(topleft=TITLE_LOAD_BTN_ORIGIN)
TITLE_SETTINGS_BTN_RECT = TITLE_SETTINGS_BTN.get_rect(topleft=TITLE_SETTINGS_BTN_ORIGIN)
TITLE_QUIT_BTN_RECT = TITLE_QUIT_BTN.get_rect(topleft=TITLE_QUIT_BTN_ORIGIN)

# Game rectangles
GAME_SAVE_BTN_RECT = GAME_SAVE_BTN.get_rect(topleft=GAME_SAVE_BTN_ORIGIN)
GAME_LOAD_BTN_RECT = GAME_LOAD_BTN.get_rect(topleft=GAME_LOAD_BTN_ORIGIN)
GAME_LOG_BTN_RECT = GAME_LOG_BTN.get_rect(topleft=GAME_LOG_BTN_ORIGIN)
GAME_QUIT_BTN_RECT = GAME_QUIT_BTN.get_rect(topleft=GAME_QUIT_BTN_ORIGIN)

# Setting rectangles
SETTINGS_BGM_PLUS_BTN_RECT = SETTINGS_BGM_PLUS_BTN.get_rect(
    topleft=SETTINGS_BGM_PLUS_BTN_ORIGIN)
SETTINGS_BGM_MINUS_BTN_RECT = SETTINGS_BGM_MINUS_BTN.get_rect(
    topleft=SETTINGS_BGM_MINUS_BTN_ORIGIN)
SETTINGS_SFX_PLUS_BTN_RECT = SETTINGS_SFX_PLUS_BTN.get_rect(
    topleft=SETTINGS_SFX_PLUS_BTN_ORIGIN)
SETTINGS_SFX_MINUS_BTN_RECT = SETTINGS_SFX_MINUS_BTN.get_rect(
    topleft=SETTINGS_SFX_MINUS_BTN_ORIGIN)

# Save / Load rectangles
SAVE_BTN_ONE_RECT = SAVE_BTN.get_rect(
    topleft=SAVE_BTN_ONE_ORIGIN)
SAVE_BTN_TWO_RECT = SAVE_BTN.get_rect(
    topleft=SAVE_BTN_TWO_ORIGIN)
SAVE_BTN_THREE_RECT = SAVE_BTN.get_rect(
    topleft=SAVE_BTN_THREE_ORIGIN)
LOAD_BTN_ONE_RECT = LOAD_BTN.get_rect(
    topleft=LOAD_BTN_ONE_ORIGIN)
LOAD_BTN_TWO_RECT = LOAD_BTN.get_rect(
    topleft=LOAD_BTN_TWO_ORIGIN)
LOAD_BTN_THREE_RECT = LOAD_BTN.get_rect(
    topleft=LOAD_BTN_THREE_ORIGIN)
DELETE_BTN_ONE_RECT = DELETE_BTN.get_rect(
    topleft=DELETE_BTN_ONE_ORIGIN)
DELETE_BTN_TWO_RECT = DELETE_BTN.get_rect(
    topleft=DELETE_BTN_TWO_ORIGIN)
DELETE_BTN_THREE_RECT = DELETE_BTN.get_rect(
    topleft=DELETE_BTN_THREE_ORIGIN)

# Subject to change
TEXT_SPEED_SLOW = 1
TEXT_SPEED_NORMAL = 2
TEXT_SPEED_FAST = 3

# Game settings - Need to get these from user_settings.txt
volume_bgm = 0  # Default 0.5
volume_sfx = 0.2

mixer.music.set_volume(volume_bgm)

# Sounds and volume
sound_btn_click = mixer.Sound(c.SFX_PATH + c.assets["BTN_CLICK_SFX"])
sound_btn_back = mixer.Sound(c.SFX_PATH + c.assets["BTN_BACK_SFX"])

sound_btn_click.set_volume(volume_sfx)
sound_btn_back.set_volume(volume_sfx)

# Application state
class State:
  TITLE = 0
  LOAD = 1
  SAVE = 2
  GAME = 3
  SETTINGS = 4
  CREDITS = 5
  SCROLLBACK = 6

current_state = State.TITLE

current_background = TITLE_BACKGROUND
# Our current position in the script
current_index = 0
# Holds the current sprites to be displayed on the game screen
current_sprites = {}
# Holds the current chapter - number + 1 if CHAPTER cmd encountered in the script
current_chapter = {
  "number": 0,
  "title": ""
}
# Current text and speaker to display
current_text = {
  "speaker": "",
  "body": "",
  "speaker_colour": c.WHITE,
  "body_colour": c.WHITE
}
# Holds the previous 100 TEXT lines
scrollback_log = []
scrollback_pos = 0

running = True
title_bgm_playing = False

# Functions
def getUserSettings():
  # Try to read user_settings.txt
    # Create if doesn't exist, populate with defaults, return defaults
  
  # Get BGM / SFX Volume and Text Speed

  # Return dictionary containing values

  return 0

def saveUserSettings():
  # Write file with currently assigned values
  return 0

def renderBodyText(text, font_size, origin, aa, fg, bg=None):
  if font_size == "large":
    output = BODY_FONT_LARGE.render("{}".format(text), aa, fg, bg)
  elif font_size == "medium":
    output = BODY_FONT_MEDIUM.render("{}".format(text), aa, fg, bg)
  else:
    output = BODY_FONT_SMALL.render("{}".format(text), aa, fg, bg)

  screen.blit(output, origin)

# Set inline dialogue formatting
def inlineTextFormat(word):
  if re.search(TEXT_BOLD_PATTERN_START, word):
    BODY_FONT_SMALL.set_bold(1)
    return 1

  if re.search(TEXT_BOLD_PATTERN_END, word):
    BODY_FONT_SMALL.set_bold(0)
    return 1

  # Italic
  if re.search(TEXT_ITALIC_PATTERN_START, word):
    BODY_FONT_SMALL.set_italic(1)
    return 1

  if re.search(TEXT_ITALIC_PATTERN_END, word):
    BODY_FONT_SMALL.set_italic(0)
    return 1

  # Underline
  if re.search(TEXT_UNDERLINE_PATTERN_START, word):
    BODY_FONT_SMALL.set_underline(1)
    return 1

  if re.search(TEXT_UNDERLINE_PATTERN_END, word):
    BODY_FONT_SMALL.set_underline(0)
    return 1

  return 0

# Get colour for inline dialogue formatting
def getColour(word):
  if re.search(TEXT_COLOUR_PATTERN, word):
    match = re.search(TEXT_COLOUR_PATTERN, word).string
    match = match.replace('(', '')
    match = match.replace(')', '')

    return tuple(map(int, match.split(',')))
  
  return 0

# Output text box dialogue (all at once)
def drawDialogue(text, x, y, fg_colour):
  counter = 0
  cur_x = x
  colour = fg_colour

  split_text = text.split()

  for word in split_text:
    # Bold
    if inlineTextFormat(word):
      continue

    # Colour
    if getColour(word):
      colour = getColour(word)
      continue

    # Render word to surface for drawing
    word_to_draw = BODY_FONT_SMALL.render(
      "{} ".format(word), 
      True, 
      colour
    )
    word_width = word_to_draw.get_width()

    if cur_x + word_width > TEXT_BODY_BOUNDS:
      # Reset x back to start, increment counter
      cur_x = x
      counter += 1

    screen.blit(
      word_to_draw, 
      (cur_x, y + (counter * TEXT_BODY_LINE_SPACING))
    )

    # Where to place the next word
    cur_x += word_width

def drawSpeaker(name, x, y, fg_colour, bg_colour=None):
  speaker_box = SPEAKER_FONT.render(
    "{}".format(name), 
    True, 
    fg_colour, 
    bg_colour
  )
  screen.blit(speaker_box, (x, y))

# Game loop
while running:
  # Draw black screen
  screen.fill(c.BLACK)
  # Set BG image
  screen.blit(current_background, (0, 0))

  ###################################################################
  #
  # TITLE SCREEN
  #
  ###################################################################
  if current_state == State.TITLE:
    current_background = TITLE_BACKGROUND
    # Set BG music - make sure it always plays on the title screen
    if not(title_bgm_playing):
      mixer.music.load(TITLE_BGM)
      mixer.music.play(-1)

      title_bgm_playing = True

    # Draw buttons
    screen.blit(TITLE_START_BTN, TITLE_START_BTN_ORIGIN)
    screen.blit(TITLE_LOAD_BTN, TITLE_LOAD_BTN_ORIGIN)
    screen.blit(TITLE_SETTINGS_BTN, TITLE_SETTINGS_BTN_ORIGIN)
    screen.blit(TITLE_QUIT_BTN, TITLE_QUIT_BTN_ORIGIN)

    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False
      
      # Temporary state switcher events
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.SAVE

        if event.key == pygame.K_2:
          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.CREDITS

        if event.key == pygame.K_3:
          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.SCROLLBACK

      # Detect button clicks
      if (event.type == pygame.MOUSEBUTTONDOWN and 
        event.button == 1
        ):
        mouse_x, mouse_y = event.pos

        if TITLE_START_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()
          # Reset to prevent any stored text flashing up briefly
          current_text["speaker"] = ""
          current_text["body"] = ""
          current_text["speaker_colour"] = c.WHITE
          current_text["body_colour"] = c.WHITE

          mixer.music.stop()
          title_bgm_playing = False

          current_sprites = {}
          current_state = State.GAME

        if TITLE_LOAD_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          current_state = State.LOAD

        if TITLE_SETTINGS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          current_state = State.SETTINGS

        if TITLE_QUIT_BTN_RECT.collidepoint(mouse_x, mouse_y):
          running = False

  ###################################################################
  #
  # LOAD SCREEN
  #
  ###################################################################
  elif current_state == State.LOAD:
    current_background = SAVE_LOAD_BG

    # Output the heading
    renderBodyText(LOAD_HEADING_TEXT, "large",
      HEADING_ORIGIN, True, c.WHITE, c.BLACK
    )

    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_ONE_ORIGIN)
    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_TWO_ORIGIN)
    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_THREE_ORIGIN)

    screen.blit(LOAD_BTN, LOAD_BTN_ONE_ORIGIN)
    screen.blit(LOAD_BTN, LOAD_BTN_TWO_ORIGIN)
    screen.blit(LOAD_BTN, LOAD_BTN_THREE_ORIGIN)

    screen.blit(DELETE_BTN, DELETE_BTN_ONE_ORIGIN)
    screen.blit(DELETE_BTN, DELETE_BTN_TWO_ORIGIN)
    screen.blit(DELETE_BTN, DELETE_BTN_THREE_ORIGIN)

    # Check for existence of save1-3 and load details accordingly

    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

      if (event.type == pygame.MOUSEBUTTONDOWN and
        event.button == 1
        ):
        mouse_x, mouse_y = event.pos

  ###################################################################
  #
  # SAVE SCREEN
  #
  ###################################################################
  elif current_state == State.SAVE:
    current_background = SAVE_LOAD_BG

    # Output the heading
    renderBodyText(SAVE_HEADING_TEXT, "large",
      HEADING_ORIGIN, True, c.WHITE, c.BLACK
    )

    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_ONE_ORIGIN)
    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_TWO_ORIGIN)
    screen.blit(SAVE_LOAD_PANEL, SAVE_LOAD_PANEL_THREE_ORIGIN)

    screen.blit(SAVE_BTN, SAVE_BTN_ONE_ORIGIN)
    screen.blit(SAVE_BTN, SAVE_BTN_TWO_ORIGIN)
    screen.blit(SAVE_BTN, SAVE_BTN_THREE_ORIGIN)

    screen.blit(DELETE_BTN, DELETE_BTN_ONE_ORIGIN)
    screen.blit(DELETE_BTN, DELETE_BTN_TWO_ORIGIN)
    screen.blit(DELETE_BTN, DELETE_BTN_THREE_ORIGIN)
    # Three text files (save1, save2, save3)

    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

      if (event.type == pygame.MOUSEBUTTONDOWN and
        event.button == 1
        ):
        mouse_x, mouse_y = event.pos

  ###################################################################
  #
  # GAME SCREEN
  #
  ###################################################################
  elif current_state == State.GAME:
    # Loop through and blit current sprites
    if len(current_sprites) > 0:
      for spr in current_sprites.values():
        sprite_to_draw = pygame.image.load(
          c.SPRITE_PATH + spr["file"]
        ).convert_alpha()
        
        screen.blit(sprite_to_draw, (spr["x"], spr["y"]))

    # Draw text box
    screen.blit(TEXT_BOX, TEXT_BOX_ORIGIN)
    # Draw buttons
    screen.blit(GAME_SAVE_BTN, GAME_SAVE_BTN_ORIGIN)
    screen.blit(GAME_LOAD_BTN, GAME_LOAD_BTN_ORIGIN)
    screen.blit(GAME_LOG_BTN, GAME_LOG_BTN_ORIGIN)
    screen.blit(GAME_QUIT_BTN, GAME_QUIT_BTN_ORIGIN)
    # Draw current text and speaker into the text box
    if current_text["body"] != "":
      drawDialogue(
          current_text["body"],
          c.assets["TEXT_BODY_ORIGIN"][0],
          c.assets["TEXT_BODY_ORIGIN"][1],
          current_text["body_colour"]
      )

    if current_text["speaker"] != "":
      drawSpeaker(
        " " + current_text["speaker"] + " ", 
        SPEAKER_BOX_ORIGIN[0],
        SPEAKER_BOX_ORIGIN[1],
        current_text["speaker_colour"],
        c.BLACK
      )

    ###################################################################
    # Run through game script
    ###################################################################
    if script[current_index][0] == 0:
      # Set current instruction to complete to prevent repeat execution
      script[current_index][0] = 1
      # Get the current command and payload object
      cmd = script[current_index][1]
      obj = script[current_index][-1]
      # Carry out actions according to the script
      if cmd is c.SPRITE:
        current_sprites[obj["reference"]] = dict(
          file=obj["file"], 
          x=obj["x"],
          y=obj["y"]
        )

        print(current_sprites)

      elif cmd is c.SPRITE_REMOVE:
        current_sprites.pop(obj["reference"])

      elif cmd is c.BG_IMG:
        current_background = pygame.image.load(c.BG_PATH + obj["file"])

      elif cmd is c.CHAPTER:
        current_chapter["number"] = current_chapter["number"] + 1
        current_chapter["title"] = obj["title"]

        print("\nCHAPTER {}: {}\n".format(
          current_chapter["number"],
          current_chapter["title"]
        ))

      elif cmd is c.TEXT:
        # Update the current text
        current_text = dict(
          speaker=obj["speaker"],
          body=obj["body"], 
          speaker_colour=obj["speaker_colour"],
          body_colour=obj["body_colour"]
        )
        # Update scrollback log
        scrollback_log.insert(0, current_text)

        # Prune scrollback log if stored text exceeds limit
        if len(scrollback_log) > SCROLLBACK_LIMIT:
          scrollback_log.pop(-1)
        
      elif cmd is c.BGM:
        mixer.music.load(c.BGM_PATH + obj["file"])
        mixer.music.play(-1)
        
      elif cmd is c.BGM_STOP:
        mixer.music.stop()

      elif cmd is c.SFX:
        sound = mixer.Sound(c.SFX_PATH + obj["file"])
        sound.play()

      # Do not advance if current index is TEXT
      if not(script[current_index][1] is c.TEXT):
        if current_index + 1 < len(script):
          current_index += 1

    ###################################################################
    # Now handle player input
    ###################################################################
    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        # Let player advance to next line in script if current index is TEXT
        if event.key == pygame.K_SPACE and script[current_index][1] is c.TEXT:
          if current_index + 1 < len(script):
            current_index += 1

        if event.key == pygame.K_ESCAPE:
          # Reset script progress for now
          current_index = 0

          for i in script:
            i[0] = 0

          # Make sure to stop any music playing before returning to title
          current_state = State.TITLE
      if (event.type == pygame.MOUSEBUTTONDOWN and 
        event.button == 1
        ):
        mouse_x, mouse_y = event.pos

        if GAME_SAVE_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

        if GAME_LOAD_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

        if GAME_LOG_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()
          current_state = State.SCROLLBACK

        if GAME_QUIT_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_back.play()
          current_state = State.TITLE

  ###################################################################
  #
  # SETTINGS SCREEN
  #
  ###################################################################
  elif current_state == State.SETTINGS:
    # Output the heading
    renderBodyText(SETTINGS_HEADING_TEXT, "large", 
      HEADING_ORIGIN, True, c.WHITE, c.BLACK
    )
    # Output text for each setting
    renderBodyText(SETTINGS_BGM_TEXT, "medium", 
      SETTINGS_BGM_TEXT_ORIGIN, True, c.WHITE, c.BLACK
    )
    renderBodyText(SETTINGS_SFX_TEXT, "medium", 
      SETTINGS_SFX_TEXT_ORIGIN, True, c.WHITE, c.BLACK
    )
    # Output plus / minus buttons
    screen.blit(SETTINGS_BGM_PLUS_BTN, SETTINGS_BGM_PLUS_BTN_ORIGIN)
    screen.blit(SETTINGS_BGM_MINUS_BTN, SETTINGS_BGM_MINUS_BTN_ORIGIN)

    screen.blit(SETTINGS_SFX_PLUS_BTN, SETTINGS_SFX_PLUS_BTN_ORIGIN)
    screen.blit(SETTINGS_SFX_MINUS_BTN, SETTINGS_SFX_MINUS_BTN_ORIGIN)

    renderBodyText(math.floor((volume_bgm + 0.01) * 10), "medium",
      (500, 200), True, c.WHITE, c.BLACK
    )
    renderBodyText(math.floor((volume_sfx + 0.01) * 10), "medium",
      (500, 300), True, c.WHITE, c.BLACK
    )

    # Draw back button
    screen.blit(BACK_BTN, BACK_BTN_ORIGIN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if (event.type == pygame.MOUSEBUTTONDOWN and 
        event.button == 1
        ):
        mouse_x, mouse_y = event.pos

        if BACK_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_back.play()
          current_state = State.TITLE

        # Raise / Lower BGM / SFX volume
        if SETTINGS_BGM_PLUS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()
          
          if volume_bgm < 0.9:
            volume_bgm += 0.1
          else:
            volume_bgm = 1

        if SETTINGS_BGM_MINUS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          if volume_bgm >= 0.1:
            volume_bgm -= 0.1
          else:
            volume_bgm = 0

        if SETTINGS_SFX_PLUS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          if volume_sfx < 0.9:
            volume_sfx += 0.1
          else:
            volume_sfx = 1

        if SETTINGS_SFX_MINUS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          if volume_sfx >= 0.1:
            volume_sfx -= 0.1
          else:
            volume_sfx = 0

        mixer.music.set_volume(volume_bgm)

        sound_btn_click.set_volume(volume_sfx)
        sound_btn_back.set_volume(volume_sfx)

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ###################################################################
  #
  # CREDITS SCREEN
  #
  ###################################################################
  elif current_state == State.CREDITS:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ###################################################################
  #
  # SCROLLBACK SCREEN
  #
  ###################################################################
  elif current_state == State.SCROLLBACK:
    # Loop through and blit current sprites
    if len(current_sprites) > 0:
      for spr in current_sprites.values():
        sprite_to_draw = pygame.image.load(
            c.SPRITE_PATH + spr["file"]
        ).convert_alpha()

        screen.blit(sprite_to_draw, (spr["x"], spr["y"]))

    # Output translucent box over current background image
    screen.blit(SCROLLBACK_BOX, (0, 0))
    # Current position to draw text
    start_x = 80
    cur_y = 20

    # Iterate through the entire scrollback log
    for i in range(len(scrollback_log)):
      pos = i + scrollback_pos
      cur_x = start_x
      # Stop drawing text if we're going to go off the bottom of the screen
      if cur_y + SCROLLBACK_LINE_SPACING > HEIGHT:
        break

      # Output the speaker
      try:
        scrollback_speaker = BODY_FONT_SMALL.render(
          "{}".format(scrollback_log[pos]["speaker"]), 
          True, 
          scrollback_log[pos]["speaker_colour"]
        )
        screen.blit(scrollback_speaker, (50, cur_y))
        cur_y += SCROLLBACK_LINE_SPACING

      except:
        pass

      # Output each line of the body text on separate lines
      try:
        current_line = scrollback_log[pos]["body"].split()
        colour = scrollback_log[pos]["body_colour"]

        for j in range(len(current_line)):
          # Bold
          if inlineTextFormat(current_line[j]):
            continue

          # Colour
          if getColour(current_line[j]):
            colour = getColour(current_line[j])
            continue

          word_to_draw = BODY_FONT_SMALL.render(
            "{} ".format(current_line[j]), 
            True, 
            colour
          )
          word_width = word_to_draw.get_width()

          # Reset x and move a line down if line will be too long
          if cur_x + word_width > TEXT_BODY_BOUNDS:
            cur_x = start_x
            cur_y += SCROLLBACK_LINE_SPACING

          screen.blit(word_to_draw, (cur_x, cur_y))

          cur_x += word_width
        cur_y += SCROLLBACK_LINE_SPACING

      except:
        pass

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sound_btn_back.play()
          current_state = State.GAME

        # Scroll log with arrow keys
        if event.key == pygame.K_UP:
          if not(scrollback_pos >= len(scrollback_log)-1):
            scrollback_pos += 1
        if event.key == pygame.K_DOWN:
          if not(scrollback_pos <= 0):
            scrollback_pos -= 1

      if event.type == pygame.MOUSEBUTTONDOWN:
        # Scroll log with mousewheel
        if event.button == 4:
          if not(scrollback_pos <= 0):
            scrollback_pos -= 1
        if event.button == 5:
          if not(scrollback_pos >= len(scrollback_log)-1):
            scrollback_pos += 1

  # Update screen
  pygame.display.update()
