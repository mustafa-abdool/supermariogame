#SIDE SCROLLING EXAMPLE
#MOVING SCREENS ETC ETC


#IDEAS AND SUGGESTIONS

#mario's position in a virtaul world
#storet his
#subtract it everytime
#platforms...bit of a hassle?
#subtract mario's x coordiante from the plaform everytime
# list comprehension for plaform list...
#changing it everytime...
#use filter to get the platforms that would be on the screen...?

#ADD IN RUNNING
#ADD IN SUPER MARIO
#ADD IN ENEMIES
#ADD IN PIPES ETC

#Coin blocks
#mushrooms
#flowers
#enemies
#barriers on platforms
#pipes
#use 2-d list for plaforms...allows you to change TEXTURES


from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=800,600
screen=display.set_mode(size)
############################################

mixer.init()

Musicdictionary={}

Musicdictionary["Jump Sound"]="Jump.wav"
Musicdictionary["Game Over"]="Game Over.OGG"
Musicdictionary["Basic Theme"]="World 1.OGG"
Musicdictionary["SMB3 Theme"]="sm3wd3.mid"

Musiclist=["Jump.wav","Game Over.OGG","World 1.OGG","sm3wd3.mid"]




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

Scenerylist=[(image.load("Block World 1.PNG")),(image.load("Grass Middle.PNG")),(image.load("Cloud.PNG")),(image.load("Question Block 1.PNG"))]

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
background5=image.load("cloud background.jpg")



##############################33

#def falling(x,y):
  #  while True:
        

def Deathcheck(x,y):
    if y>600:
        changemusic(Musicdictionary["Game Over"],4)
        time.wait(5000)
        quit()
    

def runcheck():
    if key.get_pressed()[K_LSHIFT]==True:
        horizontal_movement=7
        speed=15
    else:
        horizontal_movement=4
        speed=10
    return horizontal_movement,speed

def drawFullscene(screen,x,y,mx,my,deltax): #draws the full scene, returns what it looks like
    drawScene(screen,mx,my,background5,False)
    Drawplatforms(screen,deltax,platforms,"question block",x,y)
    return screen.copy()
    

def drawScene(screen,x,y,back,flipflag): #controls the screen moving, left or right, maybe some problems moving back..?
    if flipflag==True:
        screen.blit(transform.flip(back,True,False),(x,y))
    if flipflag==False:
        screen.blit(back,(x,y))



def changemusic(name,repeating): #changes the music 
    current_music=mixer.music.load( name )
    mixer.music.play(repeating,0)

def standingCheck(platformlist,x,y,mx,my,deltax): #checks if mario is standing , PASSING IN MORE STUFF, IF HIT JUMP OFF WITH HIGH GRAVITY
    global State 
    bottom=Rect(x,y+37,34,4) # its 400 because that will always be his position
    top=Rect(x,y,34,4)
    #draw.rect(screen,red,top)
    #display.flip()
    if top.collidelist(barriers)!=-1 and bottom.collidelist(platformlist)==-1: # this means that he hit the underside of the platform   
        State="Bounce"
    elif bottom.collidelist(platformlist)==-1:
        State="Falling"
    else:
        State="Standing"

def makeplatforms(): #makes some platforms 
    list1=[[Rect(0,600-32,2000,20),"cloud"],[Rect(800,480,200,5),"question block"]] #bottom most layer
    barriers=[]
    #for i in range(10):
        #xpos=randint(1,width)
        #ypos=randint(1,height)
        #something=Rect(xpos,ypos,32,32) #has to be divisible by 32, 10 so that it won't collide every position 
        #list1.append(something) #15 makes it able to collide or else sometimes he may to through it, width is 32, better chance for collissions
    for i in range(0,len(list1)):
        something1=Rect(list1[i][0][0],list1[i][0][1]+34,list1[i][0][2],5)
        barriers.append(something1)
    return list1,barriers,

def Drawplatforms(screen,deltax,platformlist,texture,x,y): #draws the platforms
    #newlist=filter(lambda x:# possible filtering later, if there are too many platforms
    mario_pos=x-400
   # print mario_pos
    for plat in platformlist: # WE AREN'T MOVING THINGS RELATIVE TO MARIO'S POSITION JUST DRAWING THINGS...BIZNATCH
        newplat=Rect(plat[0]-mario_pos,plat[1],plat[2],plat[3]) #subtract mario's position but don't change the rect
        if not newplat[0]>600 and not newplat[0]+newplat[2]<0: #only draw a tiny picture, by checking these collissions
            for i in range(newplat[0],newplat[0]+newplat[2],32): #then blit the textures to it...not sure if this is perfect or not STILL NEEDS SOME WORK
               # print "moose"
                screen.blit(Scenerydictionary[texture],(i,newplat[1]))



    

def jump(x,y,intial_velocity,delta_x,gravity_change,pictures,boolean,mx,my,oldx): # make intial velocity negative, boolean represents left jump image
    gravity=0
    while True:
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase
        y+=change #change the  y
        x+=delta_x #change the x
      #  time.wait(10)
        mx=mx-delta_x
        drawMario(screen,x,y,pictures,boolean,mx,my,delta_x) #draw mario, use the delta_x to indiciate the change 
        standingCheck(platforms,x,y,mx,my,deltax)
       # print State
        if State=="Standing":
            drawMario(screen,x,y,standing,False,mx,my,delta_x) #if standing then we stop 
            return mx,my,x,y
        if State=="Bounce": # if he hit the underside then we just jump again but this time with no velocity,a nd high gravity to make him fall#
            return jump(x,y,0,delta_x,3,jumplist,boolean,mx,my,oldx)
        Deathcheck(x,y)
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax): #draws mario with various animations
    global mario_rect
    mario_rect=Rect(400,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first 
    for pic in pic_list:

        if leftflag==True: #flips the image if its on the left side 
            pic=transform.flip(pic,True,False)
            
        screen.blit(updated_screen,(0,0)) #blits the updated screen 
        screen.blit(pic,mario_rect) #blits mario 
        display.flip()
        screen.fill(black)




changemusic(Musicdictionary["SMB3 Theme"],4)

speed=10
gravityforce=.4
jumpingheight=-10
horizontal_movement=4
deltax=2

bothplatforms,barriers=makeplatforms() #both platforms contains both the rect and the texture in a 2d list 

platforms=[]
for plat in range(len(bothplatforms)):
    platforms.append(bothplatforms[plat][0])


flipvariable=False




mx=-100 #make screen movement schronized with mario 
my=0

x=400
y=300

running=True
State="Falling"
#Facing="Right"
myClock=time.Clock()
while running:
    event.get()

   # print x,y
    standingCheck(platforms,x,y,mx,my,deltax)

    horizontal_movement,speed=runcheck()

    Deathcheck(x,y)
    
    if key.get_pressed()[27]==True:
        quit()

    
    if State=="Falling":
        y=y+10
        drawMario(screen,x,y,standing,False,mx,my,flipvariable)
    
    if State=="Standing":
            
        if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
           # changemusic(0,1)  #ask sir about this
            mx,my,x,y=jump(x,y,-10,horizontal_movement,gravityforce,jumplist,False,mx,my,deltax) #boolen is for left flag
        elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
           # changemusic(0,1)
            mx,my,x,y=jump(x,y,-10,horizontal_movement*(-1),gravityforce,jumplist,True,mx,my,deltax)
        elif key.get_pressed()[K_SPACE]==True:# jumping straight up
           # changemusic(0,1)
            mx,my,x,y=jump(x,y,-10,.1,gravityforce,jumplist,False,mx,my,oldx)
        elif key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
            x+=speed
            mx=mx-speed
            deltax=x-oldx
            drawMario(screen,x,y,pic_list,False,mx,my,deltax) #for run animation 
        elif key.get_pressed()[K_LEFT]==True:
            x=x-speed
            mx=mx+speed
            deltax=x-oldx
            drawMario(screen,x,y,pic_list,True,mx,my,deltax)
    else:
        
        drawMario(screen,x,y,standing,False,mx,my,flipvariable)

    
#    print (x,y)
    #print State
    
    oldx=x
    oldy=y

    
            
    myClock.tick(100)
    

    
