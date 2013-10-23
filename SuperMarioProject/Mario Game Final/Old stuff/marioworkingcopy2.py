from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=800,600
screen=display.set_mode(size)
############################################

mixer.init()


Musiclist=["Jump.wav","Game Over.OGG","World 1.OGG"]

###############################################


standing=[image.load("Mario Stand.png")]


mario1=image.load("Mario Run 1.png") #use dictionary 
mario2=image.load("Mario Run 2.png")
mario3=image.load("Mario Run 3.png")
mario4=image.load("Mario Run 4.png")

mario_jump=image.load("Mario Jump.png")

pic_list=[mario1,mario2,mario3,mario4] # list of running animation



jumplist=[mario_jump] #jumping animation

mario=image.load("Mario Stand.png")



###############################################

image.load("Block World 1.PNG")

Scenerydictionary={}
Scenerydictionary["block 1"]=image.load("Block World 1.PNG")
Scenerydictionary["grass"]=image.load("Grass Middle.PNG")
Scenerydictionary["cloud"]=image.load("Cloud.PNG")
Scenerydictionary["question block"]=image.load("Question Block 1.PNG")

#################################################

background=image.load("mariobg.png") #use dictionary
background2=image.load("Sky.bmp")
background3=image.load("mario.jpg")
background4=image.load("underwater.jpg")



##############################33

#def drawFullscene(screen):
    

def drawScene(screen,x,y,back,flipflag): #controls the screen moving 
#    screen.fill(blue)
    if flipflag==True:
        screen.blit(transform.flip(back,True,False),(x,y))
    if flipflag==False:
        screen.blit(back,(x,y))
  #  display.flip()
   # screen.fill(black)

def testscreen(platformlist): #gets one background, we don't have keep blitting everything again which slows it down 
    screen.blit(background2,(0,0)) #perhaps make seperate layers for later on 
    Drawplatforms(screen,platformlist,"cloud")
    return screen.copy()

def changemusic(index,repeating):
    mixer.music.load(Musiclist[index])
    mixer.music.play(repeating,0)

def standingCheck(platformlist,x,y):
    global State 
    bottom=Rect(x,y+37,34,4)
    if bottom.collidelist(platformlist)==-1:
        State="Falling"
    else:
        State="Standing"

def makeplatforms(): #makes some platforms 
    list1=[Rect(0,432,800,20)]
    for i in range(5):
        xpos=randint(1,width)
        ypos=randint(1,height)
        something=Rect(xpos,ypos,(xpos+32)*randint(1,8),10) #has to be divisible by 32, 10 so that it won't collide every position 
        list1.append(something)
    return list1

def Drawplatforms(screen,platformlist,texture): #draws the platforms 
    for plat in platformlist:
       # draw.rect(screen,green,plat)
        for i in range(plat[0],plat[2]+1,32):
            screen.blit(Scenerydictionary[texture],(i,plat[1]))



    

def jump(intial_velocity,delta_x,gravity_change,pictures,boolean): # make intial velocity negative
    global x
    global y
    gravity=0
    while True:
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase
        y+=change #change the  y
        x+=delta_x #change the x
        time.wait(10)
        drawMario(screen,x,y,pictures,boolean) #draw mario 
        standingCheck(platforms,x,y)
        if State=="Standing":
            drawMario(screen,x,y,standing,False)
            break
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag): #draws mario with various animations
    global mario_rect
    mario_rect=Rect(x,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    
    for pic in pic_list:
       # print pic
        if leftflag==True: #flips the image if its on the left side 
            pic=transform.flip(pic,True,False)
        screen.blit(background_layer,(0,0))
        screen.blit(pic,mario_rect)
        display.flip()
        screen.fill(black)




platforms=makeplatforms()
background_layer=testscreen(platforms)




x=400
y=300
running=True
State="Falling"
myClock=time.Clock()
while running:
    event.get()
    standingCheck(platforms,x,y)

    if key.get_pressed()[27]==True:
        quit()
    
    if State=="Falling":
        y=y+10
        drawMario(screen,x,y,standing,False)
    
    if State=="Standing":
            
        if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
           # changemusic(0,1)  #ask sir about this 
            jump(-10,3,.5,jumplist,False)
        elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
           # changemusic(0,1)
            jump(-10,-3,.5,jumplist,True)
        elif key.get_pressed()[K_SPACE]==True:# jumping straight up
           # changemusic(0,1)
            jump(-10,.1,.5,jumplist,False)
        elif key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
            x+=10
            drawMario(screen,x,y,pic_list,False) #for run animation 
        elif key.get_pressed()[K_LEFT]==True:
            x=x-10
            drawMario(screen,x,y,pic_list,True)

            
    #print (x,y)
    myClock.tick(100)
    

    
