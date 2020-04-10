import script as s
import assets as a
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

# Title assets
TITLE_BACKGROUND = pygame.image.load(
    a.BG_PATH + a.assets["TITLE_BG"]
)

TITLE_BTN_START = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_START_BTN"]
).convert_alpha()

TITLE_BTN_LOAD = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_LOAD_BTN"]
).convert_alpha()

TITLE_BTN_SETTINGS = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_SETTINGS_BTN"]
).convert_alpha()

TITLE_BTN_QUIT = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_QUIT_BTN"]
).convert_alpha()

# Game assets
TEXT_BOX = pygame.image.load(
    a.SPRITE_PATH + a.assets["TEXT_BOX"]
)

TEXT_BOX_ORIGIN = a.assets["TEXT_BOX_ORIGIN"]

title_start = TITLE_BTN_START.get_rect(
    topleft=a.assets["TITLE_START_BTN_ORIGIN"])
title_load = TITLE_BTN_LOAD.get_rect(
    topleft=a.assets["TITLE_LOAD_BTN_ORIGIN"])
title_settings = TITLE_BTN_SETTINGS.get_rect(
    topleft=a.assets["TITLE_SETTINGS_BTN_ORIGIN"])
title_quit = TITLE_BTN_QUIT.get_rect(
    topleft=a.assets["TITLE_QUIT_BTN_ORIGIN"])

# Settings assets

# Save / Load assets

running = True

# Game settings - move to config file?
volume_bgm = 0  # Default 0.5
volume_sfx = 0.5

btn_click = mixer.Sound(a.SFX_PATH + a.assets["BTN_CLICK_SFX"])
btn_back = mixer.Sound(a.SFX_PATH + a.assets["BTN_BACK_SFX"])

btn_click.set_volume(volume_sfx)
btn_back.set_volume(volume_sfx)

title_bgm_playing = False

TITLE_BGM = a.BGM_PATH + a.assets["TITLE_BGM"]

TEXT_SPEED_SLOW = 1
TEXT_SPEED_NORMAL = 2
TEXT_SPEED_FAST = 3

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
  "speaker_colour": a.WHITE,
  "body_colour": a.WHITE
}

# Holds the previous 100 TEXT lines
scrollback_log = []

# Fonts
BODY_FONT_SMALL = pygame.font.Font(
    a.FONT_PATH + a.assets["BODY_FONT"], 
    a.assets["FONT_SIZE_SMALL"]
)
BODY_FONT_MEDIUM = pygame.font.Font(
    a.FONT_PATH + a.assets["BODY_FONT"], 
    a.assets["FONT_SIZE_MEDIUM"]
)
BODY_FONT_LARGE = pygame.font.Font(
    a.FONT_PATH + a.assets["BODY_FONT"], 
    a.assets["FONT_SIZE_LARGE"]
)

SPEAKER_FONT_SMALL = pygame.font.Font(
    a.FONT_PATH + a.assets["SPEAKER_FONT"], 
    a.assets["FONT_SIZE_SMALL"]
)
SPEAKER_FONT_MEDIUM = pygame.font.Font(
    a.FONT_PATH + a.assets["SPEAKER_FONT"], 
    a.assets["FONT_SIZE_MEDIUM"]
)
SPEAKER_FONT_LARGE = pygame.font.Font(
    a.FONT_PATH + a.assets["SPEAKER_FONT"], 
    a.assets["FONT_SIZE_LARGE"]
)

print(a.assets["SPEAKER_BOX_ORIGIN"][1])

def splitText(text):
  if len(text) > 0:
    text = text.replace('\n', '')
    text_arr = text.split(" ")

    output = []
    new_string = ""

    for i in range(len(text_arr)):
      word = text_arr[i]

      if len(new_string + word + " ") > a.assets["TEXT_BODY_CHAR_LIMIT"]:
        output.append(new_string.rstrip())
        new_string = ""

      new_string += word + " "

      if i+1 == len(text_arr):
        output.append(new_string.rstrip())
  else:
    output = ['']

  print(output)
  return output

# Event handlers
def drawText(text, x, y, fg_colour):
  counter = 0

  for t in text:
    text_to_draw = BODY_FONT_SMALL.render("{}".format(t), True, fg_colour)
    screen.blit(text_to_draw, (x, y + (counter*a.assets["TEXT_BODY_LINE_SPACING"])))
    counter += 1

def drawSpeaker(name, x, y, fg_colour, bg_colour=None):
  speaker_box = SPEAKER_FONT_MEDIUM.render("{}".format(name), True, fg_colour, bg_colour)
  screen.blit(speaker_box, (x, y))

def drawBG(filename, x, y):
  print("\nDraw BG {} at position {}, {}".format(
      a.BG_PATH + filename, x, y))

def drawSprite(filename, x, y):
  print("\nDraw sprite {} at position {}, {}".format(
      a.SPRITE_PATH + filename, x, y))

def displayText(speaker, body):
  print("\n{}: {}".format(speaker, body))

def playBGM():
  print("playBGM() called")

def playSFX():
  print("playSFX() called")

# Game loop
while running:
  # Draw black screen
  screen.fill(a.BLACK)

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
    screen.blit(TITLE_BTN_START, a.assets["TITLE_START_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_LOAD, a.assets["TITLE_LOAD_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_SETTINGS, a.assets["TITLE_SETTINGS_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_QUIT, a.assets["TITLE_QUIT_BTN_ORIGIN"])

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

        if title_start.collidepoint(mouse_x, mouse_y):
          btn_click.play()

          # Reset to prevent any stored text flashing up briefly
          current_text["speaker"] = ""
          current_text["body"] = ""
          current_text["speaker_colour"] = a.WHITE
          current_text["body_colour"] = a.WHITE

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.GAME

        if title_load.collidepoint(mouse_x, mouse_y):
          btn_click.play()

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.LOAD

        if title_settings.collidepoint(mouse_x, mouse_y):
          btn_click.play()

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.SETTINGS

        if title_quit.collidepoint(mouse_x, mouse_y):

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

    # Draw current text and speaker into the text box
    drawText(
        current_text["body"],
        a.assets["TEXT_BODY_ORIGIN"][0],
        a.assets["TEXT_BODY_ORIGIN"][1],
        current_text["body_colour"]
    )

    if current_text["speaker"] != "":
      drawSpeaker(
        " " + current_text["speaker"] + " ", 
        a.assets["SPEAKER_BOX_ORIGIN"][0],
        a.assets["SPEAKER_BOX_ORIGIN"][1],
        current_text["speaker_colour"],
        a.BLACK
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
      if cmd is a.SPRITE:
        new_sprite = dict(file=obj["file"], x=obj["x"], y=obj["y"])
        current_sprites[obj["reference"]] = new_sprite

        print(current_sprites)
      elif cmd is a.BG_IMG:
        current_background = pygame.image.load(a.BG_PATH + obj["file"])
      elif cmd is a.TEXT:
        displayText(obj["speaker"], obj["body"])
        current_text["speaker"] = obj["speaker"]
        current_text["body"] = splitText(obj["body"])
        current_text["speaker_colour"] = obj["speaker_colour"]
        current_text["body_colour"] = obj["body_colour"]
        current_text["body_colour"] = obj["body_colour"]
        current_text["body_colour"] = obj["body_colour"]
        
      elif cmd is a.BGM:
        playBGM()
      elif cmd is a.SFX:
        playSFX()

      # Do not advance if current index is TEXT
      if not(script[current_index][1] is a.TEXT):
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
        if event.key == pygame.K_SPACE and script[current_index][1] is a.TEXT:
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
  # SAVE SCREEN
  #
  ################################################################################
  elif current_state == State.SETTINGS:
    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

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
      # Stop running if QUIT event detected
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
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          current_state = State.TITLE

  # Update screen
  pygame.display.update()
