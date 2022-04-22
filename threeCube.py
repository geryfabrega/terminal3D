import numpy as np
from bresenham import bresenham
import time
from curses import wrapper
import curses
import math


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
z = 5

key = ''


d = 1

key = ''

screen.nodelay(1)
	
a =  200
h = 10


""" Sprite object creation area Start"""
""" Sprite object creation area end"""
    # this determines what objects the keyboard inputs will effect


theta = 0

finalLine = []

while key != ord('q'):

    

    # vAf = [x-2, y-0.5, z + 5]
    # vBf = [x-2, y+0.5, z + 5]
    # vCf = [x-1, y+0.5, z + 5]
    # vDf = [x-1, y-0.5, z + 5]

    # vAb = [x-2, y-0.5, z + 6]
    # vBb = [x-2, y+0.5, z + 6]
    # vCb = [x-1, y+0.5, z + 6]
    # vDb = [x-1, y-0.5, z + 6]

    vAf = [-2, -0.5, -.5]
    vBf = [-2, +0.5, -.5]
    vCf = [-1, +0.5, -.5]
    vDf = [-1, -0.5, -.5]

    vAb = [-2, -0.5, .5]
    vBb = [-2, +0.5, .5]
    vCb = [-1, +0.5, .5]
    vDb = [-1, -0.5, .5]

    frontFace = [vAb,vBb,vCb,vDb]
    frontFace = np.array(frontFace)

    backFace = [vAf,vBf,vCf,vDf]
    backFace = np.array(backFace)

    rotatex = [[1,0,0],
        [0,math.cos(theta),-math.sin(theta)],
        [0,math.sin(theta),math.cos(theta)]]

    rotatey = [[math.cos(theta),0,math.sin(theta)],
        [0,1,0],
        [-math.sin(theta),0,math.cos(theta)]]

    rotatex = np.array(rotatex)
    rotatey = np.array(rotatey)

    frontFace = np.dot(frontFace,rotatex)
    backFace = np.dot(backFace,rotatex)

    frontFace = np.dot(frontFace,rotatey)
    backFace = np.dot(backFace,rotatey)

    vAf = frontFace[0]
    vAf[2] += z
    vBf = frontFace[1]
    vBf[2] += z
    vCf = frontFace[2]
    vCf[2] += z
    vDf = frontFace[3]
    vDf[2] += z

    vAb = backFace[0]
    vAb[2] += z
    vBb = backFace[1]
    vBb[2] += z
    vCb = backFace[2]
    vCb[2] += z 
    vDb = backFace[3]
    vDb[2] += z 



    
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

    theta += .01



    screen.clear()
    for j in finalLine:
        for i in j:
            try:
                screen.addstr(i[1],i[0],"#")
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




