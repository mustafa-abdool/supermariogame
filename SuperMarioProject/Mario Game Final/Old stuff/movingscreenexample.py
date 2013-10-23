# moving screen example

from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=600,600
screen=display.set_mode(size)


background=image.load("mariobg.png") #use dictionary
background2=image.load("Sky.bmp")
background3=image.load("mario.jpg")
background4=image.load("underwater.jpg")


def drawScene(screen,x,y,back,flipflag):
#    screen.fill(blue)
    if flipflag==True:
        screen.blit(transform.flip(back,True,False),(x,y))
    if flipflag==False:
        screen.blit(back,(x,y))
    display.flip()
    screen.fill(black)
    


mx=0
my=0
running=True
variable=False
myClock=time.Clock()
while running:
    event.get()
    drawScene(screen,mx,my,background4,variable)
    mx=mx-.5
    if mx==-200:
        mx=0
        if variable==True:
            variable=False
        if variable==False:
            variable=True
    print (mx,my)
    myClock.tick(60)
