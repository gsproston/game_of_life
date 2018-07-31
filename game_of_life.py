import pygame, sys, time
from pygame.locals import *

import window

# global constants
FPS = 144
GRIDSIZE = 10

# global variables
Board = [[]]
Board2 = [[]]
shutdown = False

def draw(): #called when screen needs to be updated
    screen = pygame.display.get_surface()
    pygame.display.flip()
    
    # draw the board
    for i in range(0, len(Board)):
      for j in range(0, len(Board[i])):
        if (Board[i][j] == 0):
          # draw empty square
          pygame.draw.rect(screen, (0,0,0), (i*GRIDSIZE,j*GRIDSIZE,GRIDSIZE,GRIDSIZE), 1)
        else:
          # draw filled square
          pygame.draw.rect(screen, (0,0,0), (i*GRIDSIZE,j*GRIDSIZE,GRIDSIZE,GRIDSIZE))

def resetFlags(): #new flags set
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
    
def copyBoard():
  for i in range(0, len(Board)):
    for j in range(0, len(Board[i])):
      Board[i][j] = Board2[i][j]
    
def updateBoard():
  updated = False
  for i in range(0, len(Board)):
    for j in range(0, len(Board[i])):
      updateCell(i,j)
      updated = (Board[i][j] != Board2[i][j])
  return updated
    
def updateCell(x, y):
  # total holds the number of living cells
  total = 0
  # go through all surrounding cells
  for i in range(-1, 2):
    for j in range(-1, 2):
      # ignore the centre square (that's us!)
      if (i != 0 and j != 0):
        try:
          total += Board[x+i][y+j]
          continue
        except IndexError:
          continue
        
  if (total < 2 or total > 3):
    Board2[i][j] = 0
  elif (total == 3):
    Board2[i][j] = 1
  else:
    Board2[i][j] = Board[i][j]
    
def listenOnEvents():
  global shutdown
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == QUIT: #quit called
        shutdown = True #end loop
    
if __name__ == "__main__":
    pygame.init()
    window.init()    
    clock = pygame.time.Clock()

    #main game loop
    while (not shutdown):    
        # init the boards
        res = window.getResolution()
        boardw = int(res[0] / GRIDSIZE)
        boardh = int(res[1] / GRIDSIZE)
        Board = [[0 for x in range(boardh)] for y in range(boardw)]
        Board2 = [[0 for x in range(boardh)] for y in range(boardw)]
        
        updated = True
        # only keep drawing the board if the state changes
        while (updated): 
          listenOnEvents()
          draw() 
          clock.tick(FPS) #update x times a second, determines FPS    
        
          updated = updateBoard()
          if (updated):
            print("TRUE")
          else:
            print("FALSE")
          copyBoard()

    #main loop ends, exit
    pygame.quit()