import pygame, sys
from pygame.locals import *

pygame.init()

def draw(): #called when screen needs to be updated
    pygame.display.flip()
    
def wresize(): #screen is resized, recalculate some variables
    global cxpos,cypos
    cxpos = int(screen.get_width()/2)
    cypos = int(screen.get_height()/2)

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
    
if __name__ == "__main__":
    #gets monitor info, used when resizing
    wInfo = pygame.display.Info()

    #variables
    shutdown = False
    windowWidth = 1024
    windowHeight = 576
    flags = 0
    #menu variables
    fscreen = False #fullscreen
    bwindow = False #borderless
    RATIOS = ["16:9","16:10","4:3"] #ratios
    RESS = [[],[],[]] #holds various resolution options
    RES169 = [[1024,576],[1152,648],[1280,720],[1366,768],[1600,900],[1920,1080]]
    RES1610 = [[1280,800],[1440,900],[1680,1050]]
    RES43 = [[960,720],[1024,768],[1280,960],[1400,1050],[1440,1080],[1600,1200],[1856,1392]]
    RESS[0] = RES169
    RESS[1] = RES1610
    RESS[2] = RES43

    #init screen
    screen = pygame.display.set_mode((windowWidth, windowHeight),flags)
    cxpos = int(screen.get_width()/2)
    cypos = int(screen.get_height()/2)
    screen.fill(Color(255,255,255))
    
    clock = pygame.time.Clock()

    draw()

    #main game loop
    while (not shutdown):        
        for event in pygame.event.get(): #runs when an event occurs
            if event.type == QUIT: #quit called
                shutdown = True #end loop

        clock.tick(144) #update x times a second, determines FPS

    #main loop ends, exit
    pygame.quit()    
