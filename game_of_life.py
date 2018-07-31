import pygame, sys, time
from pygame.locals import *

import window

# global constants
FPS = 144
GRIDSIZE = 10
ROUNDTIME = 0.2

# global variables
Board = [[]]
Board2 = [[]]
shutdown = False
paused = True

def draw(): #called when screen needs to be updated
    screen = pygame.display.get_surface()
    
    screen.fill((255,255,255))
    # draw the board
    for i in range(0, len(Board)):
      for j in range(0, len(Board[i])):
        if (Board[i][j] == 0):
          # draw empty square
          pygame.draw.rect(screen, (0,0,0), (i*GRIDSIZE,j*GRIDSIZE,GRIDSIZE,GRIDSIZE), 1)
        else:
          # draw filled square
          pygame.draw.rect(screen, (0,0,0), (i*GRIDSIZE,j*GRIDSIZE,GRIDSIZE,GRIDSIZE))
    pygame.display.flip()
    
def copyBoard():
  for i in range(0, len(Board)):
    for j in range(0, len(Board[i])):
      Board[i][j] = Board2[i][j]
    
def updateBoard():
  updated = False
  for i in range(0, len(Board)):
    for j in range(0, len(Board[i])):
      updateCell(i,j)
      updated = updated or (Board[i][j] != Board2[i][j])
  return updated
    
def updateCell(x, y):
  # total holds the number of living cells
  total = 0
  # go through all surrounding cells
  for i in range(-1, 2):
    for j in range(-1, 2):
      # ignore the centre square (that's us!)
      if (i != 0 or j != 0):
        try:
          total += Board[x+i][y+j]
          continue
        except IndexError:
          continue
        
  if (total < 2 or total > 3):
    Board2[x][y] = 0
  elif (total == 3):
    Board2[x][y] = 1
  else:
    Board2[x][y] = Board[x][y]
    
def changeLifeOnClick():
  x = pygame.mouse.get_pos()[0]
  x = int(x/10)
  y = pygame.mouse.get_pos()[1]
  y = int(y/10)
  Board[x][y] = (Board[x][y] + 1) % 2
    
def listenOnEvents():
  global shutdown, paused
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == QUIT: #quit called
        shutdown = True #end loop
    elif event.type == MOUSEBUTTONDOWN: #mouse clicked
        changeLifeOnClick()
    elif event.type == KEYDOWN: #key has been pressed
      if pygame.key.get_pressed()[pygame.K_SPACE]:
        paused = not paused
    
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
        waitCount = 0
        # only keep drawing the board if the state changes
        while (updated and not shutdown): 
          listenOnEvents()
          draw() 
          clock.tick(FPS) #update x times a second, determines FPS    
        
          if (not paused):          
            if (waitCount >= FPS*ROUNDTIME):      
              waitCount = 0
              updated = updateBoard()
              copyBoard()
            waitCount += 1
            
        shutdown = True

    #main loop ends, exit
    pygame.quit()