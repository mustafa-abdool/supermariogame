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

#RECTANGLES AT THE SIDE FOR PIPE COLISSIONSSSSSSSSSSSSSSSS

#Coin blocks
#mushrooms
#flowers
#enemies
#barriers on platforms
#pipes
#use 2-d list for plaforms...allows you to change TEXTURES

#Problems

#if the platform is too close to mario's head he won't bounce off it..>?
#MAKE ALL THE PLATFORMS BE AT THE TOP


# Schedule


#making large platforms 
# Side Collisions - making rects, checking collisions, try to just use the BASIC RECT for mario


#Block Events - have a 3rd spot in your 2d list if the block has anythign "special" in it. Put it into a list, once its hit delete it
#Super Mario and Fire Mario (do fire mario after..complicated =\)
#Enemies - move much like mario
#Roto disks...?
#Sprites and Classes..>?



from pygame import*
from random import*
from colours import *
from glob import *

init()
size=width,height=600,600
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
Scenerydictionary["empty block"]=image.load("Empty Block.PNG")

#################################################

background=image.load("mariobg.png") #use dictionary
background2=image.load("Sky.bmp")
background3=image.load("mario.jpg")
background4=image.load("underwater.jpg")
background5=image.load("cloud background.jpg")



##############################33

#Beanstalk and obstacles stuf

beanstalkimage=image.load("beanstalk.jpg")
screen2=Rect(0,0,600,600)

def beanstalk(px,py,picture,x,y,mx,my,deltax):
    global beanstalkimage
    global screen2
    picture=beanstalkimage
    count=0
    for i in range(py,py-300,-32):
        count+=1
        Myrect=Rect(px,i,32,32*count) # rect that controls what can be modified
        screen.set_clip(screen2)
        drawFullscene(screen,x,y,mx,my,0)             #draw full scene then blit it
        screen.set_clip(Myrect) #increases each time
        screen.blit(picture,(px,i)) #blit the picture
        time.wait(100) #delay
        display.flip() #update
       # screen.fill(black)
        print "gay"
    screen.set_clip(screen2)

def Indexfunction(something): #finds the index of a thing in the list
    for i in range(len(bothplatforms)):
        for j in range(2):
            if bothplatforms[i][j]==something:
                print "lauraaa"

def Deathcheck(x,y): #checks if mario is dead yet
    if y>600:
        changemusic(Musicdictionary["Game Over"],4)
        time.wait(5000)
        quit()
    

def movementcheck(State,Facing): #checks to see if mario is running or colliding with an obstacle 
    #if State=="Bounce2":
      #  speed=0
     #   horizontal_movement=4
    if key.get_pressed()[K_LSHIFT]==True:
        horizontal_movement=7
        speed=15
    else:
        horizontal_movement=4
        speed=10
    return horizontal_movement,speed

def drawFullscene(screen,x,y,mx,my,deltax): #draws the full scene, returns what it looks like
    drawScene(screen,mx,my,background5,False)
    Drawplatforms(screen,deltax,platforms,"question block",)
    return screen.copy()
    

def drawScene(screen,x,y,back,flipflag): #controls the screen moving, left or right, maybe some problems moving back..?
    if flipflag==True:
        screen.blit(transform.flip(back,True,False),(x,y))
    if flipflag==False:
        screen.blit(back,(x,y))



def changemusic(name,repeating): #changes the music 
    current_music=mixer.music.load( name )
    mixer.music.play(repeating,0)

def standingCheck(jumpflag,x,y,mx,my,deltax): #YOU DON'T NEED TO PASS IN PLATFORMLISTTT
    global State #having a top and bottom RECT makes it more accurate, won't "glitch" through platforms and such 
   # someflag=False
    bottom=Rect(400,y+37,34,4) # its 400 because that will always be his position
    top=Rect(400,y,34,4) #all rectangles surrounding mario, like "walls" sort of 
    right_side=Rect(435,y,5,34)
    left_side=Rect(395,y,5,34)
   
    platforms=[]
    for plat in range(len(bothplatforms)): #makes a list called platforms which is basically all the platforms, taken out of the 2d list
       platforms.append(bothplatforms[plat][0])
       
    if jumpflag==True: #if he's jumping we always see if he can stop first 
        #USE TOP PLATS INSTEAD OF EVERYTHING...
        if bottom.collidelist(top_plats)!=-1:
            State="Standing"

        elif right_side.collidelist(platforms)!=-1: 
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side      
        elif top.collidelist(barriers)!=-1 and bottom.collidelist(top_plats)==-1: # this means that he hit the underside of the platform
           # if toplist top.collidelist(barriers)
            State="Bounce"
            if bothplatforms[top.collidelist(barriers)][1]=="question block": # if it was a question block we set to an empty block
                bothplatforms[top.collidelist(barriers)][1]="empty block"
                beanstalk(bothplatforms[top.collidelist(barriers)][0][0],bothplatforms[top.collidelist(barriers)][0][1]-32,"laura",x,y,mx,my,deltax)
            #Indexfunction( barriers[top.collidelist(barriers)])
        elif bottom.collidelist(top_plats)==-1:
            State="Falling"




    else: #else we always check for collissions first 

        
        if right_side.collidelist(platforms)!=-1: 
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side 
        elif bottom.collidelist(top_plats)!=-1:
            State="Standing"
     
        elif top.collidelist(barriers)!=-1 and bottom.collidelist(platforms)==-1: # this means that he hit the underside of the platform   
            State="Bounce"
        elif bottom.collidelist(platforms)==-1:
            State="Falling"
    #else:
    #    State="Standing"


def makeplatforms(): #makes some platforms 
    list1=[[Rect(0,600-32,2000,20),"block 1"],[Rect(800,450,32,32),"question block"],[Rect(900,450,32,32),"question block"]] #bottom most layer, 
    barriers=[]
    sidebarriers=[]
    platforms2=[]
    for i in range(0,len(list1)): #platforms at the top...rect for side collisions, MAKE PLATFORMS A BIT BIGGER
        something4=Rect(list1[i][0][0],list1[i][0][1]-5,list1[i][0][2],32) #top platforms 
        platforms2.append(something4)
    #for i in range(10):
        #xpos=randint(1,width)
        #ypos=randint(1,height)
        #something=Rect(xpos,ypos,32,32) #has to be divisible by 32, 10 so that it won't collide every position 
        #list1.append(something) #15 makes it able to collide or else sometimes he may to through it, width is 32, better chance for collissions
    for i in range(0,len(list1)):
        something1=Rect(list1[i][0][0],list1[i][0][1]+list1[i][0][3],list1[i][0][2],5) #appends the bottom most layer
        #something2=Rect(list1[i][0][0],list1[i][0][1],15,list1[i][0][3]) #left layer, the 10 makes it look closer
       # something3=Rect(list1[i][0][0]+list1[i][0][2]-10,list1[i][0][1],5,list1[i][0][3])     #right layer,                                              # right layer
        barriers.append(something1)
       # sidebarriers.append(something2)
       # sidebarriers.append(something3)
    return list1,barriers,sidebarriers,platforms2

def Drawplatforms(screen,deltax,platformlist,texture): #draws the platforms, DON'T NEED TO PAST IN PLATFORMLIST
    print bothplatforms
    #newlist=filter(lambda x:# possible filtering later, if there are too many platforms
    #print top_plats
    #for plat in top_plats:
       # plat[0]=plat[0]-deltax
        #draw.rect(screen,blue,plat)
       # display.flip()
  #  for bar in barriers:
       # bar[0]=bar[0]-deltax
        #draw.rect(screen,red,bar)
   # display.flip()
    for i in range(len(bothplatforms)):
        bothplatforms[i][0][0]=bothplatforms[i][0][0]-deltax #have to change both where it starts depending on mario's position
       #the minus 1 underneath is because range is one short
        for p in range(bothplatforms[i][0][1],bothplatforms[i][0][1]+bothplatforms[i][0][3]-1,32):#goes through all y values...
            for j in range(bothplatforms[i][0][0],bothplatforms[i][0][0]+bothplatforms[i][0][2]-1,32): # then go through and blit the appropirate texture
                screen.blit(Scenerydictionary[bothplatforms[i][1]],(j,p)) #minus makes it go higher, plus makes it go lower
            


    

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
        standingCheck(True,x,y,mx,my,deltax)
        if State=="Standing":
            drawMario(screen,x,y,standing,False,mx,my,delta_x) #if standing then we stop 
            return mx,my,x,y
        print State
        if State=="Bounce": # if he hit the underside then we just jump again but this time with no velocity,a nd high gravity to make him fall#
            return jump(x,y,0,delta_x,2,jumplist,boolean,mx,my,oldx) #delta_x makes him bouncee
        if State=="Bounce2" or State=="Bounce3":
            return jump(x,y,-2,0,7,standing,boolean,mx,my,oldx) #makes him fall really fast 
        Deathcheck(x,y)
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax): #draws mario with various animations
  #  global mario_rect
#    mario_rect=Rect(400,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first 
    for pic in pic_list:

        if leftflag==True: #flips the image if its on the left side 
            pic=transform.flip(pic,True,False)
            
        screen.blit(updated_screen,(0,0)) #blits the updated screen 
        screen.blit(pic,(400,y)) #blits mario 
        display.flip()
      #  time.wait(50)
        screen.fill(black)




changemusic(Musicdictionary["SMB3 Theme"],4)

platforms=[] #need to define this before...
speed=10
gravityforce=.40
#jumpingheight=-10
horizontal_movement=4
deltax=2

bothplatforms,barriers,sidebarriers,top_plats=makeplatforms() #both platforms contains both the rect and the texture in a 2d list 


flipvariable=False

Facing="Right"



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
    standingCheck(platforms,x,y,mx,my,deltax)

   # print Facing
    #print State
    horizontal_movement,speed=movementcheck(State,Facing)

    Deathcheck(x,y)
    
    if key.get_pressed()[27]==True:
        quit()

    
    if State=="Falling":
        y=y+10
        drawMario(screen,x,y,standing,False,mx,my,flipvariable)
    
    if State=="Standing" or State=="Bounce2" or State=="Bounce3": #Bounce2 and Bounce3 are collision states
            
        if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
           # changemusic(0,1)  #ask sir about this
           Facing="Right"
           mx,my,x,y=jump(x,y,-10,horizontal_movement,gravityforce,jumplist,False,mx,my,deltax) #boolen is for left flag
        elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
           # changemusic(0,1)
            Facing="Left"
            mx,my,x,y=jump(x,y,-10,horizontal_movement*(-1),gravityforce,jumplist,True,mx,my,deltax)
        elif key.get_pressed()[K_SPACE]==True:# jumping straight up
           # changemusic(0,1)
            Facing=Facing #special case...where we check the facing to see how he jumps 
            if Facing=="Right":
                leftflag=False
                movement=.1
            if Facing=="Left":
                leftflag=True
                movement=-.1
            mx,my,x,y=jump(x,y,-10,movement,gravityforce,jumplist,leftflag,mx,my,oldx) #NEEDA F ACING VARIABLE 
        elif key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
            Facing="Right"
            standingCheck(platforms,x+speed,y,mx,my,deltax) #MAKE THIS NON GLOBAL
            if State=="Bounce3": #if he would collide, then we speed to zero because that can'
                speed=0
            x+=speed
            mx=mx-speed
            deltax=x-oldx
            drawMario(screen,x,y,pic_list,False,mx,my,deltax) #for run animation 
        elif key.get_pressed()[K_LEFT]==True:
            Facing="Left"
            standingCheck(platforms,x-speed,y,mx,my,deltax)
            if State=="Bounce2": #if he would collide we set his sppeed to zero cause he can't, but he can move hte other way
                speed=0
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
    

    
