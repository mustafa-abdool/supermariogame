#SIDE SCROLLING EXAMPLE
#MOVING SCREENS ETC ETC

#Things to fix

#gravity/collission problem
#maybe just make check to see if ANY part of his rectangle collides with a platform?






#Whats New?

#added beanstalk (kinda)
#block events(kinda)
#side collisions 

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
#looks like mario's feet are not colliding with the platform 

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

#big_pic_list=image.load[

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
background6=image.load("laura's background fixed.png")



##############################33

#Beanstalk and obstacles stuf

#have a list for obstacles such as [Rect(blah blah blah blha),mushroom]

beanstalkimage=image.load("beanstalk copy.png")
mushroompic=image.load("Mushroom.png")
screen2=Rect(0,0,600,600) #rectangles which represents the screen

def Sizecheck(screen,x,y,False,mx,my,deltax,Action): #gets the picture list of whatever mario is doing
    if mario_size=="small":
        if Action=="standing":
            return drawMario(screen,x,y,standing,False,mx,my,deltax)
       # if Action=="jumping":
           # x,y,mx,my=jump(x,y,-10
    


def Interactions(Rectobject): #pass in mario_size, if nothing happens then we return it 
    temp_obstacles=[]
   # print Obstacles
    for i in range(len(Obstacles)):
        # Obstacles[i][0]!=None:
        temp_obstacles.append(Obstacles[i][0])
    #print temp_obstacles        
    if Rectobject.collidelist(temp_obstacles)!=-1:
        if Obstacles[Rectobject.collidelist(temp_obstacles)][1]=="mushroom":
            mario_size="Super"
    return mario_size 
            
            

def twodim(row,col):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append((Rect(1,1,1,1)))
        list1.append(temp)
    return list1


def Statecheck(Rectobject):#almost like standing check except for obstacles
    if Rectobject.collidelist(top_plats)==-1: #they are either falling or moving 
        State="Falling"
    else:
        State="Moving"
    return State

def drawObstacles(Displayflag,x,y,mx,my,deltax):
    global mushroompic
    for object1 in Obstacles:
     #   print object1
        if object1[1]=="mushroom": #always subtracting Mario's original position
            object1[0][0]=object1[0][0]-deltax
            State=Statecheck(object1[0]) #Create a SPEED VARIABLE that way if the mushroom hits a wall if will "bounce off"
            if State=="Moving":
                object1[0][0]=object1[0][0]+5
            if State=="Falling":
                object1[0][1]=object1[0][1]+5
            screen.blit(mushroompic,(object1[0][0],object1[0][1]))



def mushroom(px,py,x,y,mx,my,deltax,pos): #pos represents the place in the Obstacle list that it will be 
    global mushroompic
    drawFullscene(screen,x,y,mx,my,deltax)
    screen.blit(mushroompic,(px,py-32))
    Obstacles[pos][0]=Rect(px,py-30,32,32)
    Obstacles[pos][1]="mushroom"
   # display.flip()
   # time.wait(3000)

def blockevents(name,px,py,x,y,mx,my,deltax,pos):
    if name=="mushroom":
       # print "okay"
        mushroom(px,py,x,y,mx,my,deltax,pos)

        


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
    drawScene(screen,mx,my,background6,False)
    Drawplatforms(screen,deltax,platforms,"question block",)
    drawObstacles(False,x,y,mx,my,deltax)
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

    #TRY CHANGING THINGS TO MARIO_RECT

    
    global State #having a top and bottom RECT makes it more accurate, won't "glitch" through platforms and such
   # someflag=False
    mario_rect=Rect(400,y,34,34)
    bottom=Rect(400,y+34,34,4) # its 400 because that will always be his position
    top=Rect(400,y,34,4) #all rectangles surrounding mario, like "walls" sort of 
    right_side=Rect(435,y,5,30)
    left_side=Rect(395,y,5,30) #SHORTENED THISSS
    
    #draw.rect(screen,blue,bottom)
    #isplay.flip()
   
    platforms=[]
    for plat in range(len(bothplatforms)): #makes a list called platforms which is basically all the platforms, taken out of the 2d list
       platforms.append(bothplatforms[plat][0])
       
    if jumpflag==True: #if he's jumping we always see if he can stop first
        
        if mario_rect.collidelist(top_plats)!=-1: #CHANGED THIS TO MARIO RECT, MAYBE USING MARIO RECT IS MORE USEFUL - TRY IT! 
            State="Standing"

        elif right_side.collidelist(platforms)!=-1: 
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side

           #CHANGED THIS... 
        elif mario_rect.collidelist(barriers)!=-1 and bottom.collidelist(top_plats)==-1: # this means that he hit the underside of the platform
           # if toplist top.collidelist(barriers)
            State="Bounce"
            if bothplatforms[top.collidelist(barriers)][1]=="question block": # if it was a question block we set to an empty block
                bothplatforms[top.collidelist(barriers)][1]="empty block"
                if bothplatforms[top.collidelist(barriers)][2]=="mushroom":
                    blockevents( bothplatforms[top.collidelist(barriers)][2],bothplatforms[top.collidelist(barriers)][0][0],bothplatforms[top.collidelist(barriers)][0][1]-32,x,y,mx,my,deltax,top.collidelist(barriers))
               # blockevents(
               # beanstalk(bothplatforms[top.collidelist(barriers)][0][0],bothplatforms[top.collidelist(barriers)][0][1]-32,"laura",x,y,mx,my,deltax)
            #Indexfunction( barriers[top.collidelist(barriers)])
        elif bottom.collidelist(top_plats)==-1: #change to mario_rect?
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
    list1=[[Rect(0,600-32,2000,20),"block 1","none"],[Rect(800,450,32,500),"question block","mushroom"],[Rect(900,450,32,32),"question block","mushroom"],[Rect(1000,450,32,32),"question block","mushroom"]] #bottom most layer, 
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
    #newlist=filter(lambda x:# possible filtering later, if there are too many platforms
    for plat in top_plats:
        plat[0]=plat[0]-deltax

    for bar in barriers:
        bar[0]=bar[0]-deltax
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

        #for i in range here...divide delta x by ratio?
        y+=change #change the  y
        x+=delta_x #change the x
      #  time.wait(10)
        mx=mx-delta_x
        drawMario(screen,x,y,pictures,boolean,mx,my,delta_x) #draw mario, use the delta_x to indiciate the change
    #for i in range...maybe make a range and go through it, might make collisions better 
        standingCheck(True,x,y,mx,my,deltax)
        if State=="Standing":
            drawMario(screen,x,y,standing,False,mx,my,delta_x) #if standing then we stop 
            return mx,my,x,y
        #print State
        if State=="Bounce": # if he hit the underside then we just jump again but this time with no velocity,a nd high gravity to make him fall#
            return jump(x,y,0,delta_x,5,jumplist,boolean,mx,my,oldx) #delta_x makes him bouncee
        if State=="Bounce2" or State=="Bounce3":
            return jump(x,y,-2,0,7,standing,boolean,mx,my,oldx) #makes him fall really fast, if he collides w/ the side 
        Deathcheck(x,y)
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax): #draws mario with various animations
  #  global mario_rect
    mario_rect=Rect(400,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first
    Interactions(mario_rect)
    for pic in pic_list:

        if leftflag==True: #flips the image if its on the left side 
            pic=transform.flip(pic,True,False)
            
        screen.blit(updated_screen,(0,0)) #blits the updated screen 
        screen.blit(pic,mario_rect) #blits mario 
        display.flip()
      #  time.wait(50)
        screen.fill(black)


Obstacles=twodim(10,2)
leftflag=False  
changemusic(Musicdictionary["SMB3 Theme"],4)

platforms=[] #need to define this before...
speed=10
gravityforce=.40
#jumpingheight=-10
horizontal_movement=4
deltax=2
mario_size="small"

bothplatforms,barriers,sidebarriers,top_plats=makeplatforms() #both platforms contains both the rect and the texture in a 2d list 


flipvariable=False

Facing="Right"

oldx=2
mx=-100 #make screen movement schronized with mario 
my=0

x=400
y=300

running=True
State="Falling"
#Facing="Right"
myClock=time.Clock()
while running:
    #print Obstacles
    
    
    
    event.get()
    standingCheck(platforms,x,y,mx,my,deltax)

   # print Facing
    #print State
    horizontal_movement,speed=movementcheck(State,Facing)

    Deathcheck(x,y)
    
    if key.get_pressed()[27]==True:
        quit()

    #PUT ALL THIS INTO A FUNCTION
    if State=="Falling":
        y=y+10
        Sizecheck(screen,x,y,standing,False,mx,my,"Standing")
       # drawMario(screen,x,y,standing,False,mx,my,0)#changed this to zero 
    
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

    if x==oldx: #if he's not moving we just draw it, this ways the obstacles can move tooo
        drawMario(screen,x,y,standing,leftflag,mx,my,0)
   # else:
        
       # drawMario(screen,x,y,standing,False,mx,my,flipvariable)
      #  drawMario(screen,x,y,standing,False,mx,my,flipvariable)
    
#    print (x,y)
    #print State
   # drawFullscene(screen,x,y,mx,my,0)
    oldx=x
    oldy=y


    
            
    myClock.tick(100)
    

    
