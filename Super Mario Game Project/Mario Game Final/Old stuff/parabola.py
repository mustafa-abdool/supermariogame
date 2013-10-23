
################################################


def findavalue(xcoord,ycoord,axis,vertex):
    xsquared=(xcoord-axis)**2
    yvalue=ycoord-vertex
    avalue=yvalue/float(xsquared)
    return avalue


from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=800,600
screen=display.set_mode(size)



mario1=image.load("Mario Run 1.png")
mario2=image.load("Mario Run 2.png")
mario3=image.load("Mario Run 3.png")
mario4=image.load("Mario Run 4.png")

mario_jump=image.load("Mario Jump.png")

pic_list=[mario1,mario2,mario3,mario4] #list of running animation
jump_list=[mario_jump]

xcoordinate=400
ycoordinate=300


def drawScene(screen,x,y,pic_list): #draws mario with various animations
    global mario_rect
    mario_rect=Rect(x,y,34,34)  #maybe give it a length...each time it changes draws an ew one?
    for pic in pic_list:
        screen.blit(pic,mario_rect)
#        Drawplatforms(screen)
        display.flip()
        screen.fill(black)

def Parabola2(screen,xcoordinate,ycordinate,xincrease,yincrease):

    axis=xcoordinate-xincrease
    vertex=ycoordinate-yincrease

    x=xcoordinate

    avalue=findavalue(xcoordinate,ycoordinate,axis,vertex)

    avalue=avalue*-1

    start=avalue*(x-axis)**2-vertex

    start=start*(-1)

    x=x-1
    
    while True:
        y=avalue*(x-axis)**2-vertex

        y=y*-1
        print y

        
        if start==y or start<y:
            break
       # print y
        draw.circle(screen,green,(x,y),2)
        display.flip()
        x=x-1 


def Parabola(screen,xcoordinate,ycoordinate,xincrease,yincrease): #now...it is fixed you fool


    axis=xcoordinate+xincrease
    vertex=ycoordinate-yincrease

    x=xcoordinate

    avalue=findavalue(xcoordinate,ycoordinate,axis,vertex)

    avalue=avalue*-1

    start=avalue*(x-axis)**2-vertex

    start=start*-1
    
    x+=1

    print start

    jumping=True
    while jumping:
        y=avalue*(x-axis)**2-vertex

        y=y*-1
        
        if x%1==0:
            drawScene(screen,x,y,jump_list)
            

        x+=.0625
    

count=0
running=True
while running:
    print mouse.get_pos()
    #print "gay"
    if count==0:
        Parabola(screen,xcoordinate,ycoordinate,50,100) 
    count+=1
    myClock=time.Clock()






