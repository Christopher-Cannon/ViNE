import script as s
import assets as a  # Should really be called game config or something
import pygame
from pygame import mixer
from enum import Enum

pygame.init()

try:
  script = s.getScript()
except:
  print("An error occurred when retrieving the script\nExiting...")
  pygame.QUIT

# Our current position in the script
current_index = 0

WIDTH = 960
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

class State:
  TITLE = 0
  LOAD = 1
  SAVE = 2
  GAME = 3
  SETTINGS = 4
  CREDITS = 5

current_state = State.TITLE

# Title assets
TITLE_BACKGROUND = pygame.image.load(
    a.BG_PATH + a.assets["TITLE_BG"])
TITLE_BTN_START = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_START_BTN"]).convert()
TITLE_BTN_LOAD = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_LOAD_BTN"]).convert()
TITLE_BTN_SETTINGS = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_SETTINGS_BTN"]).convert()
TITLE_BTN_QUIT = pygame.image.load(
    a.SPRITE_PATH + a.assets["TITLE_QUIT_BTN"]).convert()

# Game settings - move to config file?
volume_bgm = 0
volume_sfx = 0.5

title_start = TITLE_BTN_START.get_rect(
    topleft=a.assets["TITLE_START_BTN_ORIGIN"])
title_load = TITLE_BTN_LOAD.get_rect(
    topleft=a.assets["TITLE_LOAD_BTN_ORIGIN"])
title_settings = TITLE_BTN_SETTINGS.get_rect(
    topleft=a.assets["TITLE_SETTINGS_BTN_ORIGIN"])
title_quit = TITLE_BTN_QUIT.get_rect(
    topleft=a.assets["TITLE_QUIT_BTN_ORIGIN"])

title_bgm_playing = False

# Event handlers
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

  ################################################################################
  #
  # TITLE SCREEN
  #
  ################################################################################
  if current_state == State.TITLE:
    # Set BG music
    if not(title_bgm_playing):
      mixer.music.load(a.BGM_PATH + a.assets["TITLE_BGM"])
      mixer.music.set_volume(volume_bgm)
      mixer.music.play(-1)

      title_bgm_playing = True

    # Set BG image
    screen.blit(TITLE_BACKGROUND, (0, 0))

    # Draw buttons
    screen.blit(TITLE_BTN_START, a.assets["TITLE_START_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_LOAD, a.assets["TITLE_LOAD_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_SETTINGS, a.assets["TITLE_SETTINGS_BTN_ORIGIN"])
    screen.blit(TITLE_BTN_QUIT, a.assets["TITLE_QUIT_BTN_ORIGIN"])

    for event in pygame.event.get():
      # Stop running if QUIT event detected
      if event.type == pygame.QUIT:
        running = False
      
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

  ################################################################################
  #
  # GAME SCREEN
  #
  ################################################################################
  elif current_state == State.GAME:
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
    # Run through game script
    ################################################################################
    if script[current_index][0] == 0:
      # Set current instruction to complete to prevent repeat execution
      script[current_index][0] = 1

      cmd = script[current_index][1]
      obj = script[current_index][-1]

      # Do command-specific actions
      if cmd is a.SPRITE:
        drawSprite(obj["file"], obj["x"], obj["y"])
      elif cmd is a.BG_IMG:
        drawBG(obj["file"], obj["x"], obj["y"])
      elif cmd is a.TEXT:
        displayText(obj["speaker"], obj["body"])
      elif cmd is a.BGM:
        playBGM()
      elif cmd is a.SFX:
        playSFX()

      # Do not advance if current index is TEXT
      if not(script[current_index][1] is a.TEXT):
        if current_index + 1 < len(script):
          current_index += 1

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

  # Update screen
  pygame.display.update()
