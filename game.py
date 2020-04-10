import script as s
import config as c
import pygame
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

################################################################################
# Constants from config.py
################################################################################

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
TEXT_BODY_CHAR_LIMIT = c.assets["TEXT_BODY_CHAR_LIMIT"]
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
SETTINGS_BGM_PLUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_PLUS_BTN"]).convert_alpha()
SETTINGS_BGM_MINUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_BGM_MINUS_BTN"]).convert_alpha()
SETTINGS_SFX_PLUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_PLUS_BTN"]).convert_alpha()
SETTINGS_SFX_MINUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_SFX_MINUS_BTN"]).convert_alpha()
SETTINGS_TEXT_PLUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_TEXT_PLUS_BTN"]).convert_alpha()
SETTINGS_TEXT_MINUS_BTN = pygame.image.load(c.SPRITE_PATH + c.assets["SETTINGS_TEXT_MINUS_BTN"]).convert_alpha()

SETTINGS_BGM_PLUS_BTN_ORIGIN = c.assets["SETTINGS_BGM_PLUS_BTN_ORIGIN"]
SETTINGS_BGM_MINUS_BTN_ORIGIN = c.assets["SETTINGS_BGM_MINUS_BTN_ORIGIN"]
SETTINGS_SFX_PLUS_BTN_ORIGIN = c.assets["SETTINGS_SFX_PLUS_BTN_ORIGIN"]
SETTINGS_SFX_MINUS_BTN_ORIGIN = c.assets["SETTINGS_SFX_MINUS_BTN_ORIGIN"]
SETTINGS_TEXT_PLUS_BTN_ORIGIN = c.assets["SETTINGS_TEXT_PLUS_BTN_ORIGIN"]
SETTINGS_TEXT_MINUS_BTN_ORIGIN = c.assets["SETTINGS_TEXT_MINUS_BTN_ORIGIN"]

SETTINGS_BGM_TEXT = c.assets["SETTINGS_BGM_TEXT"]
SETTINGS_SFX_TEXT = c.assets["SETTINGS_SFX_TEXT"]
SETTINGS_TEXT_TEXT = c.assets["SETTINGS_TEXT_TEXT"]

SETTINGS_BGM_TEXT_ORIGIN = c.assets["SETTINGS_BGM_TEXT_ORIGIN"]
SETTINGS_SFX_TEXT_ORIGIN = c.assets["SETTINGS_SFX_TEXT_ORIGIN"]
SETTINGS_TEXT_TEXT_ORIGIN = c.assets["SETTINGS_TEXT_TEXT_ORIGIN"]

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

# Subject to change
TEXT_SPEED_SLOW = 1
TEXT_SPEED_NORMAL = 2
TEXT_SPEED_FAST = 3


# Game settings - move to config file?
volume_bgm = 0  # Default 0.5
volume_sfx = 0.5

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
# Current text and speaker to display
current_text = {
  "speaker": "",
  "body": "",
  "speaker_colour": c.WHITE,
  "body_colour": c.WHITE
}
# Holds the previous 100 TEXT lines
scrollback_log = []

running = True
title_bgm_playing = False

def splitText(text):
  if len(text) > 0:
    text = text.replace('\n', '')
    text_arr = text.split(" ")

    output = []
    new_string = ""

    for i in range(len(text_arr)):
      word = text_arr[i]

      if len(new_string + word + " ") > TEXT_BODY_CHAR_LIMIT:
        output.append(new_string.rstrip())
        new_string = ""

      new_string += word + " "

      if i+1 == len(text_arr):
        output.append(new_string.rstrip())
  else:
    output = ['']

  return output

# Event handlers
def drawText(text, x, y, fg_colour):
  counter = 0

  for t in text:
    text_to_draw = BODY_FONT_SMALL.render("{}".format(t), True, fg_colour)
    screen.blit(text_to_draw, (x, y + (counter * TEXT_BODY_LINE_SPACING)))
    counter += 1

def drawSpeaker(name, x, y, fg_colour, bg_colour=None):
  speaker_box = SPEAKER_FONT.render("{}".format(name), True, fg_colour, bg_colour)
  screen.blit(speaker_box, (x, y))

# To be changed or removed
def drawBG(filename, x, y):
  print("\nDraw BG {} at position {}, {}".format(
      c.BG_PATH + filename, x, y))

def drawSprite(filename, x, y):
  print("\nDraw sprite {} at position {}, {}".format(
      c.SPRITE_PATH + filename, x, y))

def displayText(speaker, body):
  print("\n{}: {}".format(speaker, body))

def playBGM():
  print("playBGM() called")

def playSFX():
  print("playSFX() called")

# Game loop
while running:
  # Draw black screen
  screen.fill(c.BLACK)
  # Set BG image
  screen.blit(current_background, (0, 0))

  ################################################################################
  #
  # TITLE SCREEN
  #
  ################################################################################
  if current_state == State.TITLE:
    current_background = TITLE_BACKGROUND
    # Set BG music - make sure it always plays on the title screen
    if not(title_bgm_playing):
      mixer.music.load(TITLE_BGM)
      mixer.music.set_volume(volume_bgm)
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
      if event.type == pygame.MOUSEBUTTONDOWN:
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
          current_state = State.GAME

        if TITLE_LOAD_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.LOAD

        if TITLE_SETTINGS_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_click.play()

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.SETTINGS

        if TITLE_QUIT_BTN_RECT.collidepoint(mouse_x, mouse_y):

          running = False

  ################################################################################
  #
  # LOAD SCREEN
  #
  ################################################################################
  elif current_state == State.LOAD:
    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ################################################################################
  #
  # SAVE SCREEN
  #
  ################################################################################
  elif current_state == State.SAVE:
    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ################################################################################
  #
  # GAME SCREEN
  #
  ################################################################################
  elif current_state == State.GAME:
    # Loop through and blit current sprites

    # Draw text box
    screen.blit(TEXT_BOX, TEXT_BOX_ORIGIN)
    # Draw buttons
    screen.blit(GAME_SAVE_BTN, GAME_SAVE_BTN_ORIGIN)
    screen.blit(GAME_LOAD_BTN, GAME_LOAD_BTN_ORIGIN)
    screen.blit(GAME_LOG_BTN, GAME_LOG_BTN_ORIGIN)
    screen.blit(GAME_QUIT_BTN, GAME_QUIT_BTN_ORIGIN)
    # Draw current text and speaker into the text box
    drawText(
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

    ################################################################################
    # Run through game script
    ################################################################################
    if script[current_index][0] == 0:
      # Set current instruction to complete to prevent repeat execution
      script[current_index][0] = 1
      # Get the current command and payload object
      cmd = script[current_index][1]
      obj = script[current_index][-1]
      # Carry out actions according to the script
      if cmd is c.SPRITE:
        new_sprite = dict(file=obj["file"], x=obj["x"], y=obj["y"])
        current_sprites[obj["reference"]] = new_sprite

        print(current_sprites)

      elif cmd is c.BG_IMG:
        current_background = pygame.image.load(c.BG_PATH + obj["file"])

      elif cmd is c.TEXT:
        # Update the current text
        current_text["speaker"] = obj["speaker"]
        # Split body text on to multiple lines
        current_text["body"] = splitText(obj["body"])
        current_text["speaker_colour"] = obj["speaker_colour"]
        current_text["body_colour"] = obj["body_colour"]
        current_text["body_colour"] = obj["body_colour"]
        current_text["body_colour"] = obj["body_colour"]
        
      elif cmd is c.BGM:
        playBGM()

      elif cmd is c.SFX:
        playSFX()

      # Do not advance if current index is TEXT
      if not(script[current_index][1] is c.TEXT):
        if current_index + 1 < len(script):
          current_index += 1

    ################################################################################
    # Now handle player input
    ################################################################################
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
  ################################################################################
  #
  # SETTINGS SCREEN
  #
  ################################################################################
  elif current_state == State.SETTINGS:
    bgm_text = BODY_FONT_MEDIUM.render("{}".format(SETTINGS_BGM_TEXT), True, c.WHITE, c.BLACK)
    screen.blit(bgm_text, SETTINGS_BGM_TEXT_ORIGIN)

    sfx_text = BODY_FONT_MEDIUM.render("{}".format(SETTINGS_SFX_TEXT), True, c.WHITE, c.BLACK)
    screen.blit(sfx_text, SETTINGS_SFX_TEXT_ORIGIN)

    text_text = BODY_FONT_MEDIUM.render("{}".format(SETTINGS_TEXT_TEXT), True, c.WHITE, c.BLACK)
    screen.blit(text_text, SETTINGS_TEXT_TEXT_ORIGIN)

    screen.blit(BACK_BTN, BACK_BTN_ORIGIN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        if BACK_BTN_RECT.collidepoint(mouse_x, mouse_y):
          sound_btn_back.play()
          current_state = State.TITLE

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ################################################################################
  #
  # CREDITS SCREEN
  #
  ################################################################################
  elif current_state == State.CREDITS:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  ################################################################################
  #
  # SCROLLBACK SCREEN
  #
  ################################################################################
  elif current_state == State.SCROLLBACK:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  # Update screen
  pygame.display.update()
