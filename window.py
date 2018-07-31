import pygame, sys
from pygame.locals import *

# window constants
RATIOS = ["16:9","16:10","4:3"] # ratios
RES169 = [[1024,576],[1152,648],[1280,720],[1366,768],[1600,900],[1920,1080]]
RES1610 = [[1280,800],[1440,900],[1680,1050]]
RES43 = [[960,720],[1024,768],[1280,960],[1400,1050],[1440,1080],[1600,1200],[1856,1392]]
RESS = [RES169,RES1610,RES43] # holds various resolution options

# new flags set
# returns the new screen object
def resetFlags(fscreen,bwindow): 
  # gets monitor info, used when resizing
  wInfo = pygame.display.Info()
  if fscreen:
    w = wInfo.current_w
    h = wInfo.current_h
    if bwindow:
      flags = FULLSCREEN|NOFRAME
    else:
      flags = FULLSCREEN
  else:
    w = windowWidth
    h = windowHeight
    if bwindow:
      flags = NOFRAME
    else:
      flags = 0
  pygame.display.set_mode((w,h),flags)
  
def getRatio():
  return RATIOS[ratind]
  
def getResolution():
  return RESS[ratind][resind]

def init():
  global ratind, resind
  print("Initialising the display")
  # variables
  flags = 0
  # menu variables
  fscreen = False # fullscreen
  bwindow = False # borderless
  ratind = 0 # index of the ratio menu
  resind = 0 # index of the resolution menu
  # ratios and resolutions can be found in constants
  windowWidth = RESS[ratind][resind][0]
  windowHeight = RESS[ratind][resind][1]

  # init screen
  screen = pygame.display.set_mode((windowWidth, windowHeight),flags)
  pygame.display.set_caption("Snap")
  screen.fill(Color(255,255,255))