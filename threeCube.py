import numpy as np
from bresenham import bresenham
import time
from curses import wrapper
import curses


# Update the buffer, adding text at different locations

def placePx(x):
    sX = 120 + x
    return sX

def placePy(y):
    sY = 20 + y
    return sY

def viewportToCanvas(x,y):
    cW = 100
    cH = 100

    vW = 1
    vH = 1
    return x * cW/vW, y * cH/vH 

def projectVertex(v):
    return viewportToCanvas(v[0]/v[2],v[1]/v[2])

#The function make lines takes in a 2 tuples (x1,y2),(x2,y2) and returns a list of discrete xy's to form a line between the two catersian points
def makelines(pair1,pair2):
    x1 = int(placePx(pair1[0]))
    y1 = int(placePy(pair1[1]))
    x2 = int(placePx(pair2[0]))
    y2 = int(placePy(pair2[1]))
    
    line1 = list(bresenham(x1,y1,x2,y2))

    return line1

screen = curses.initscr()

curses.cbreak()
screen.keypad(1)

screen.refresh()


count = 0 

running = True

x = 0
y = 0
z = 0

key = ''


d = 1

key = ''

screen.nodelay(1)
	
a =  200
h = 10


""" Sprite object creation area Start"""
""" Sprite object creation area end"""
    # this determines what objects the keyboard inputs will effect

finalLine = []

while key != ord('q'):

    

    vAf = [x-2, y-0.5, z + 5]
    vBf = [x-2, y+0.5, z + 5]
    vCf = [x-1, y+0.5, z + 5]
    vDf = [x-1, y-0.5, z + 5]

    vAb = [x-2, y-0.5, z + 6]
    vBb = [x-2, y+0.5, z + 6]
    vCb = [x-1, y+0.5, z + 6]
    vDb = [x-1, y-0.5, z + 6]
    
    pair1 = projectVertex(vAf)
    pair2 = projectVertex(vBf)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vBf)
    pair2 = projectVertex(vCf)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vCf)
    pair2 = projectVertex(vDf)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vDf)
    pair2 = projectVertex(vAf)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vAb)
    pair2 = projectVertex(vBb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vBb)
    pair2 = projectVertex(vCb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vCb)
    pair2 = projectVertex(vDb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)
    
    pair1 = projectVertex(vDb)
    pair2 = projectVertex(vAb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vAf)
    pair2 = projectVertex(vAb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vBf)
    pair2 = projectVertex(vBb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vCf)
    pair2 = projectVertex(vCb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    pair1 = projectVertex(vDf)
    pair2 = projectVertex(vDb)

    #pygame.draw.line(screen,(0,0,0),(placePx(pair1[0]),placePy(pair1[1])),(placePx(pair2[0]),placePy(pair2[1])),1)
    tempLine = makelines(pair1,pair2)

    finalLine.append(tempLine)

    screen.clear()
    for j in finalLine:
        for i in j:
            try:
                screen.addstr(i[1],i[0],"*")
            except:
                pass

    finalLine = []
    curses.napms(10)
    key = screen.getch()
	
    if key == curses.KEY_UP:
        z += .1
    elif key == curses.KEY_DOWN: 
        z -= .1
    if key == curses.KEY_RIGHT: 
        x += .1
    elif key == curses.KEY_LEFT:
        x -= .1


curses.endwin()


