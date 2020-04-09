import script as script_file
import assets as assets_file
import pygame
from pygame import mixer
from enum import Enum

pygame.init()

try:
  script = script_file.getScript()
except:
  print("An error occurred when retrieving the script\nExiting...")
  pygame.QUIT

try:
  title_assets = assets_file.getTitleAssets()
except:
  print("An error occurred when retrieving the title assets\nExiting...")
  pygame.QUIT

# Where are we in the script
current_index = 0

WIDTH = 800
HEIGHT = 600

# Create screen of 800 wide and 600 height
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RUNNING = True

class State:
  TITLE = 0
  LOAD = 1
  SAVE = 2
  GAME = 3
  SETTINGS = 4
  CREDITS = 5

current_state = State.TITLE

# Paths to assets
BG_PATH = 'backgrounds/'
FONT_PATH = 'fonts/'
BGM_PATH = 'music/'
SFX_PATH = 'sounds/'
SPRITE_PATH = 'sprites/'

# Various commands that can be included in scripts
TEXT = "TEXT"
BG_IMG = "BG_IMG"
SPRITE = "SPRITE"
BGM = "BGM"
SFX = "SFX"
BGM_VOL = "BGM_VOLUME"
SFX_VOL = "SFX_VOLUME"

# Colours
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)

# Game settings - move to config file?
volume_bgm = 0
volume_sfx = 0.5

# Title assets
TITLE_BACKGROUND = pygame.image.load(BG_PATH + title_assets["TITLE_BG"])
TITLE_BTN_START = pygame.image.load(SPRITE_PATH + title_assets["TITLE_START_BTN"]).convert()
TITLE_BTN_LOAD = pygame.image.load(SPRITE_PATH + title_assets["TITLE_LOAD_BTN"]).convert()
TITLE_BTN_SETTINGS = pygame.image.load(SPRITE_PATH + title_assets["TITLE_SETTINGS_BTN"]).convert()
TITLE_BTN_QUIT = pygame.image.load(SPRITE_PATH + title_assets["TITLE_QUIT_BTN"]).convert()

title_start = TITLE_BTN_START.get_rect(center=(665, 210))
title_load = TITLE_BTN_LOAD.get_rect(center=(665, 320))
title_settings = TITLE_BTN_SETTINGS.get_rect(center=(665, 430))
title_quit = TITLE_BTN_QUIT.get_rect(center=(665, 540))

title_bgm_playing = False

# Event handlers
def drawBG(filename, x, y):
  print("\nDraw BG {} at position {}, {}".format(BG_PATH + filename, x, y))

def drawSprite(filename, x, y):
  print("\nDraw sprite {} at position {}, {}".format(SPRITE_PATH + filename, x, y))

def displayText(speaker, body):
  print("\n{}: {}".format(speaker, body))

def playBGM():
  print("playBGM() called")

def playSFX():
  print("playSFX() called")

def volumeBGM():
  print("volumeBGM() called")

def volumeSFX():
  print("volumeSFX() called")

# Game loop
while RUNNING:
  # Draw black screen
  screen.fill(BLACK)

  ################################################################################
  #
  # TITLE SCREEN
  #
  ################################################################################
  if current_state == State.TITLE:
    # Set BG music
    if not(title_bgm_playing):
      mixer.music.load(BGM_PATH + title_assets["TITLE_BGM"])
      mixer.music.set_volume(volume_bgm)
      mixer.music.play(-1)

      title_bgm_playing = True

    # Set BG image
    screen.blit(TITLE_BACKGROUND, (0, 0))

    # Draw buttons
    screen.blit(TITLE_BTN_START, (540, 160))
    screen.blit(TITLE_BTN_LOAD, (540, 270))
    screen.blit(TITLE_BTN_SETTINGS, (540, 380))
    screen.blit(TITLE_BTN_QUIT, (540, 490))

    for event in pygame.event.get():
      # Stop RUNNING if QUIT event detected
      if event.type == pygame.QUIT:
        RUNNING = False
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos

        if title_start.collidepoint(mouse_x, mouse_y):
          print("Start btn clicked")

          mixer.music.stop()
          title_bgm_playing = False
          current_state = State.GAME

        if title_load.collidepoint(mouse_x, mouse_y):
          print("Load btn clicked")

        if title_settings.collidepoint(mouse_x, mouse_y):
          print("Settings btn clicked")

        if title_quit.collidepoint(mouse_x, mouse_y):
          print("Quit btn clicked")

          RUNNING = False

  ################################################################################
  #
  # GAME SCREEN
  #
  ################################################################################
  elif current_state == State.GAME:
    for event in pygame.event.get():
      # Stop RUNNING if QUIT event detected
      if event.type == pygame.QUIT:
        RUNNING = False

      if event.type == pygame.KEYDOWN:
        # Let player advance to next line in script if current index is TEXT
        if event.key == pygame.K_SPACE and script[current_index][1] is TEXT:
          if current_index + 1 < len(script):
            current_index += 1

        if event.key == pygame.K_ESCAPE:
          # Reset script progress for now
          current_index = 0

          for i in script:
            i[0] = 0

          current_state = State.TITLE

    if script[current_index][0] == 0:
      # Set current instruction to complete to prevent repeat execution
      script[current_index][0] = 1

      cmd = script[current_index][1]
      obj = script[current_index][-1]

      # Do command-specific actions
      if cmd is SPRITE:
        drawSprite(obj["file"], obj["x"], obj["y"])
      elif cmd is BG_IMG:
        drawBG(obj["file"], obj["x"], obj["y"])
      elif cmd is TEXT:
        displayText(obj["speaker"], obj["body"])
      elif cmd is BGM:
        playBGM()
      elif cmd is SFX:
        playSFX()
      elif cmd is BGM_VOL:
        volumeBGM()
      elif cmd is SFX_VOL:
        volumeSFX()

      # Do not advance if current index is TEXT
      if not(script[current_index][1] is TEXT):
        if current_index + 1 < len(script):
          current_index += 1

  # Update screen
  pygame.display.update()
