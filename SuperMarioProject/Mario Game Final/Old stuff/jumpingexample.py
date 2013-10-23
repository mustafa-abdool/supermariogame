from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=800,600
screen=display.set_mode(size)
############################################

mixer.init()

jumpsound=mixer.music.load("Jump.wav") #...odd why doesn't it work? 


standing=[image.load("Mario Stand.png")]


mario1=image.load("Mario Run 1.png")
mario2=image.load("Mario Run 2.png")
mario3=image.load("Mario Run 3.png")
mario4=image.load("Mario Run 4.png")

mario_jump=image.load("Mario Jump.png")

pic_list=[mario1,mario2,mario3,mario4] #list of running animation

marioleft1=image.load("Mario Run 1 Left.png")
marioleft2=image.load("Mario Run Left 2.png")
marioleft3=image.load("Mario Run 3 Left.png")
marioleft4=image.load("Mario Run 4 Left.png")

left_pic_list=[marioleft1,marioleft2,marioleft3,marioleft4]


jumplist=[mario_jump] #jumping animation

mario=image.load("Mario Stand.png")

leftjump=image.load("Mario Jump Left.png")

left_jumplist=[leftjump]

#################################################

def standingCheck(platformlist,x,y):
    global State 
    bottom=Rect(x,y+37,34,4)
    if bottom.collidelist(platformlist)==-1:
        State="Falling"
    else:
        State="Standing"

def makeplatforms(): #makes some platforms 
    list1=[]
    for i in range(20):
        something=Rect(randint(1,800),randint(1,800),100,10)
        list1.append(something)
    return list1

def Drawplatforms(screen,platformlist): #draws the platforms 
    for plat in platformlist:
        draw.rect(screen,green,plat)



    

def jump(intial_velocity,delta_x,gravity_change,pictures): # make intial velocity negative
    global x
    global y
    gravity=0
    while True:
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase
        y+=change #change the  y
        x+=delta_x #change the x
        time.wait(10)
        drawMario(screen,x,y,pictures) #draw mario 
        standingCheck(platforms,x,y)
        if State=="Standing":
            drawMario(screen,x,y,standing)
            break
        print (x,y)
    
        

def drawMario(screen,x,y,pic_list): #draws mario with various animations
    global mario_rect
    mario_rect=Rect(x,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    for pic in pic_list:
        screen.blit(pic,mario_rect)
        Drawplatforms(screen,platforms)
       # draw.rect(screen,green,bottom)
        display.flip()
        screen.fill(black)



platforms=makeplatforms()


x=400
y=300
running=True
State="Falling"
myClock=time.Clock()
while running:
    event.get()
    standingCheck(platforms,x,y)
    print State
        
    if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
        mixer.music.play(1,0)
        jump(-10,3,.5,jumplist)
    elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
        mixer.music.play(1,0)
        jump(-10,-3,.5,left_jumplist)
    elif key.get_pressed()[K_SPACE]==True:# jumping straight up
        mixer.music.play(1,0)
        jump(-10,.1,.5,jumplist)
    elif key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
        x+=5
        drawMario(screen,x,y,pic_list) #for run animation 
    elif key.get_pressed()[K_LEFT]==True:
        x=x-5
        drawMario(screen,x,y,left_pic_list)
    elif key.get_pressed()[K_UP]==True:
        y=y-5
        drawMario(screen,x,y,standing)
    elif key.get_pressed()[K_DOWN]==True:
        y=y+5
        drawMario(screen,x,y,standing)
    print (x,y)
    myClock.tick(30)
    

    
