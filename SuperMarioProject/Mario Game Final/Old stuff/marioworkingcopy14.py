
#USE KEYDOWN EVNTS

# OBSTACLES AND ENEMIES MOVE FASTER WHILE JUMPING

# FIX STATECHECKKK...PASSING IN DIFFERENT THINGS, remember you changed it to past in two parameters...fix the mushroom thing

# DO MUSHROOMS IN THE SAME WAY THAT YOU DID ENEMIES

#ENEMIES CAN'T FALL OFF PLATFORMS...MAKE SOME KIND OF COUNTER SO THAT THEY CAN KEEP FALLING, KEEPING TRACK OF OLD STATES?

#FIX NEUTRAL JUMPING


#SIDE SCROLLING EXAMPLE
#MOVING SCREENS ETC ETC

#Things to fix

#gravity/collission problem
#maybe just make check to see if ANY part of his rectangle collides with a platform?
#MY DOESN'T REALLY  MATTTERRR
#if obstacles y coordinate is greater than 600 just remove it
# filter to only get stuff that will be shown...lambda?

#CREATE A JUMPING THING....GOES THROUGH EVERY Y COORDINATE..WILL MAKE COLISSIONS MORE ACCURATE

#maybe lower super mario's y coordinate to make his standing look more realistic

#JUMPIGN COLLISIONS...MAYBE CYCLE THROUGH EACH TIME?


#NEUTRAL SPACE JUMPING WILL GLITCH THROUGH PLATFORMS

#SHORTEN TOP AND BOTTOM RECTS...WELL..MAYBE JUST TOP, SHORTEN TOP ON SUPER MARIOOOOOOOOOO 

#ADD IN USE OF ARROW KEYS WHILE JUMPING

#SOME WAY TO REMEMBER THE DIRECTION THAT THE FIREBAL IS MOVING IN...USING LEFTFLAG AND A 2D LIST

#MAKE MUSHROOMJ ABLE TO HIT THE WALL AND BOUNCE OFFFF


#CREATE SPEED VARIABLE FOR OBSTACLES

#CREATE 2 SIDE RECTS

####################################################

#Whats New?

#added beanstalk (kinda)
#block events(kinda)
#side collisions
#SUPER MARIO, and Z

#IDEAS AND SUGGESTIONS

#mario's position in a virtaul world
#storet his
#subtract it everytime
#platforms...bit of a hassle?
#subtract mario's x coordiante from the plaform everytime
# list comprehension for plaform list...
#changing it everytime...
#use filter to get the platforms that would be on the screen...?


#ADD IN ENEMIES
#ADD IN PIPES ETC

#RECTANGLES AT THE SIDE FOR PIPE COLISSIONSSSSSSSSSSSSSSSS



#Problems

#if the platform is too close to mario's head he won't bounce off it..>?
#MAKE ALL THE PLATFORMS BE AT THE TOP
#looks like mario's feet are not colliding with the platform 

# Schedule


#making large platforms 
# Side Collisions - making rects, checking collisions, try to just use the BASIC RECT for mario


#Block Events - have a 3rd spot in your 2d list if the block has anythign "special" in it. Put it into a list, once its hit delete it
#Super Mario and Fire Mario (do fire mario after..complicated =\)
#Enemies - move much like MUSHROOMS
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




mario1=image.load("Mario Run 1.png") #use dictionary 
mario2=image.load("Mario Run 2.png")
mario3=image.load("Mario Run 3.png")
mario4=image.load("Mario Run 4.png")

mario5=image.load("Super Mario Run 1.png")
mario6=image.load("Super Mario Run 2.png")
mario7=image.load("Super Mario Run 3.png")

mario8=image.load("Fiery Mario Run 1.png")
mario9=image.load("Fiery Mario Run 2.png")
mario10=image.load("Fiery Mario Run 3.png")

standing=[image.load("Mario Stand.png")]

big_standing=[image.load("Super Mario Stand.png")]

fire_standing=[image.load("Fiery Mario Stand.png")]

########################################################

running_list=[mario1,mario2,mario3,mario4] # list of running animation

big_running_list=[mario5,mario6,mario7]

fire_running_list=[mario8,mario9,mario10]

#################################################

jumplist=[image.load("Mario Jump.png")] #jumping animation

big_jumplist=[image.load("Super Mario Jump.png")]

fire_jumplist=[image.load("Fiery Mario Jump.png")]


################

throwanimation=[image.load("Fiery Mario Throw.png")]
####################################################

Enemiesdictionary={}

Enemiesdictionary['goomba']=image.load("Goomba 2 w-2.png")

Enemiesdictionary['koopa']=image.load("Green Koopa 1.png")




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

beanstalkimage=image.load("beanstalk copy.png") #MAKE THIS A DICTIONARY THEN YOU WON'T HAVE TO GLOBAL STUFFF
mushroompic=image.load("Mushroom.png")
screen2=Rect(0,0,600,600) #rectangles which represents the screen
flowerpic=image.load("Fire Flower 1.png")
fireballpic=image.load("Fireball.png")

#########################################################

def movebadguys(deltax): #maybe break it up into smaller functions, moves enemies
    for i in range(len(Enemies)): #makea  side rectangle, see if collides, if it does, reverse velocity...just put it INTO FUNCTION
        if Enemies[i]!=None: #MAYBE MAKE VARIABLES...MAKES THINGS EASIER TO UNDERSTAND
         #   print Enemies[i][4]
            Enemies[i][1][0]=Enemies[i][1][0]-deltax #subtract mario's pos
            siderect=Rect(Enemies[i][1][0]+Enemies[i][3][0],Enemies[i][1][1],3,Enemies[i][3][1]-5)# represents rectangle at the side
            siderect2=Rect(Enemies[i][1][0]-3,Enemies[i][1][1],3,Enemies[i][3][1]-5)
            State=Statecheck(Enemies[i][1],siderect,siderect2)
            if State=="Bounce":
                Enemies[i][2]=Enemies[i][2]*-1 #reverse velocity
                if Enemies[i][4]==True: #reverse direction he's facing...SOMETHING WRONG WITH THIS
                    #print "moose"
                    Enemies[i][4]=False
                elif Enemies[i][4]==False:
                   # print "moose"
                    Enemies[i][4]=True
            if State=="Falling":
                Enemies[i][1][1]=Enemies[i][1][1]+3 # make a tuple that invovles vertical nad horizontal movement
            else:
                Enemies[i][1][0]+=Enemies[i][2] # enemies[i][2] is the speed
           # siderect=Rect(Enemies[i][1][0]+30,Enemies[i][1][1],3,30)
           # draw.rect(screen,pink,siderect)
            pic=Enemiesdictionary[Enemies[i][0]]
            if Enemies[i][4]==False:
              #   print "gay"
                 pic=transform.flip(pic,True,False)
            screen.blit(pic,Enemies[i][1])
          #  screen.blit(Enemiesdictionary[Enemies[i][0]],Enemies[i][1])
        
def movefireball(intial_v,horizontal_movement,gravity,deltax): #moves fireballs, GIVE A DIRECTION THAT ITS MOVING IN...IF IT COLLIDES THEN DELETE
    global fireballgravity1
    global fireballgravity2
    for fire in range(len(fireball_list)):
     #   print fireball_list[fire]
        if fireball_list[fire]!=None:
            fireball_list[fire][0]=fireball_list[fire][0]-deltax
            fireballgravity1+=gravity
            change=intial_v-fireballgravity1
            fireball_list[fire][1]+=change
            fireball_list[fire][0]+=horizontal_movement
            State=Statecheck(fireball_list[fire],fireball_list[fire])
            if State=="Moving":
                fireballgravity1=0
            if State=="Bounce":
                del fireball_list[fire]
                break
            screen.blit(fireballpic,fireball_list[fire]) #OUT OF RANGE ERRORS 
            


def pictureCheck(mario_size,Action): #gets the picture list of whatever mario is doing
    if mario_size=="small":
        
        if Action=="Jumping Right" or Action=="Jumping Left" or Action=="Neutral Jumping":
            return jumplist
        if Action=="Moving Right" or Action=="Moving Left":
            return running_list
        if Action=="Standing":
            return standing
    if mario_size=="Super":
        if Action=="Jumping Right" or Action=="Jumping Left" or Action=="Neutral Jumping":
            return big_jumplist
        if Action=="Moving Right" or Action=="Moving Left":
            return big_running_list
        if Action=="Standing":
            return big_standing
    if mario_size=="Fire":
        if Action=="Jumping Right" or Action=="Jumping Left" or Action=="Neutral Jumping":
            return fire_jumplist
        if Action=="Moving Right" or Action=="Moving Left":
            return fire_running_list
        if Action=="Standing":
            return fire_standing        

def Interactions(Rectobject,mario_size,y): #pass in mario_size, if nothing happens then we return it
    global State
    temp_obstacles=[]
   # print Obstacles
    for i in range(len(Obstacles)):
        # Obstacles[i][0]!=None:
        temp_obstacles.append(Obstacles[i][0])
    #print temp_obstacles        
    if Rectobject.collidelist(temp_obstacles)!=-1:
        pos=Rectobject.collidelist(temp_obstacles)
        if Obstacles[pos][1]=="flower":
            if State=="Standing":
                del Obstacles[pos]
                mario_size="Fire"
        elif Obstacles[pos][1]=="mushroom":
            del Obstacles[pos]
            mario_size="Super"


    if mario_size=="Super" or mario_size=="Fire":
        mario_rect=Rect(400,y-34,40,64)
        bottom=Rect(400,y+34,34,4) # its 400 because that will always be his position


    if mario_size=="small":
        mario_rect=Rect(400,y,34,34)
        bottom=Rect(400,y+34,34,4) # its 400 because that will always be his position

   # draw.rect(screen,pink,mario_rect)
   # display.flip()
    temp_enemies=[]
    for i in range(len(Enemies)):
        temp_enemies.append(Enemies[i][1])

    collideflag=False
    if State=="Falling":     #has to be fallikng for him to kill the enemey
        if bottom.collidelist(temp_enemies)!=-1: #
            collideflag=True
            print "enemey dead"
            pos=bottom.collidelist(temp_enemies) #if the bottom collides, then the enemey is dead, add dying aniamtion
            del Enemies[pos]

    if collideflag==False:# collide flag is necesarry or else it will do both
        if mario_rect.collidelist(temp_enemies)!=-1: #if anyother part of mario collides then he's dead 
            print "dead"


            
    return mario_size 
            
            

def twodim(row,col):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append((Rect(1,1,1,1)))
        list1.append(temp)
    return list1


def Statecheck(Rectobject,siderect,siderect2):#almost like standing check except for obstacles

   # draw.rect(screen,pink,siderect)
   # draw.rect(screen,pink,siderect2)
    platforms=[]
    for plat in range(len(bothplatforms)): #makes a list called platforms which is basically all the platforms, taken out of the 2d list
       platforms.append(bothplatforms[plat][0])

    if Rectobject.collidelist(top_plats)!=-1:
        State="Moving"
    elif siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
        State="Bounce"
    elif Rectobject.collidelist(top_plats)==-1: #they are either falling or moving 
        State="Falling"

    return State


def drawObstacles(Displayflag,x,y,mx,my,deltax):
    global mushroompic
    global flowerpic
    for object1 in Obstacles:
     #   print object1
        object1[0][0]=object1[0][0]-deltax #subtract Mario's position IMPORTANT
        if object1[1]=="flower": #flowers don't move 
            
            screen.blit(flowerpic,object1[0])
        if object1[1]=="mushroom": #always subtracting Mario's original position
            siderect=Rect(object1[0][0]-3,object1[0][1],3,object1[0][3]) #at the right
            siderect2=Rect(object1[0][0]+object1[0][2],object1[0][1],3,object1[0][3]) #left...?
            draw.rect(screen,siderect,pink)
            draw.rect(screen,siderect2,pink)
            display.flip()
            
            State=Statecheck(object1[0],siderect,siderect2) #Create a SPEED VARIABLE that way if the mushroom hits a wall if will "bounce off"
            print State
            if State=="Bounce":
                object1[2]=object1[2]*-1 #reverse velocity
           
            if State=="Moving": 
                
                object1[0][0]=object1[0][0]+object1[2]
            if State=="Falling":
                object1[0][1]=object1[0][1]+7
            screen.blit(mushroompic,(object1[0][0],object1[0][1]))

def flower(px,py,x,y,mx,my,deltax,pos):
    global flowerpic
    Obstacles[pos][0]=Rect(px,py,32,32) #parameters for flower, so that it looks good 
    Obstacles[pos][1]="flower"
    drawFullscene(screen,x,y,mx,my,deltax)
    screen.blit(flowerpic,Obstacles[pos][0])


def mushroom(px,py,x,y,mx,my,deltax,pos): #pos represents the place in the Obstacle list that it will be 
    global mushroompic
    drawFullscene(screen,x,y,mx,my,deltax)
    screen.blit(mushroompic,(px,py-32))
    Obstacles[pos][0]=Rect(px,py-30,32,32)
    Obstacles[pos][1]="mushroom"
    Obstacles[pos][2]=3 #this is the speed
   # display.flip()
   # time.wait(3000)

def blockevents(name,px,py,x,y,mx,my,deltax,pos):
    if name=="mushroom":
       # print "okay"
        mushroom(px,py,x,y,mx,my,deltax,pos)
    if name=="flower":
        flower(px,py,x,y,mx,my,deltax,pos)

        


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
    drawObstacles(False,x,y,mx,my,deltax) #mushrooms and stuff
    movefireball(-5,8,-.5,deltax)
    movebadguys(deltax)
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

    #TRY TO FIX THIS!!!!!!!!!!!! PROBLEMS WITH COLISSIONS
    
    global State #having a top and bottom RECT makes it more accurate, won't "glitch" through platforms and such
   # someflag=False
    #print y
    if mario_size=="Super" or mario_size=="Fire":
        mario_rect=Rect(400,y-34,40,64)
        bottom=Rect(400,y+34,34,4) # its 400 because that will always be his position
        top=Rect(400,y-34,34,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(435,y-34,5,60)
        left_side=Rect(395,y-34,5,60) #SHORTENED THISSS

    if mario_size=="small":
        mario_rect=Rect(400,y,34,34)
        bottom=Rect(400,y+34,34,4) # its 400 because that will always be his position
        top=Rect(400,y,34,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(435,y,5,30)
        left_side=Rect(395,y,5,30) #SHORTENED THISSS


    

   
    platforms=[]
    for plat in range(len(bothplatforms)): #makes a list called platforms which is basically all the platforms, taken out of the 2d list
       platforms.append(bothplatforms[plat][0])
       
    if jumpflag==True: #if he's jumping we always see if he can stop first
        
        if bottom.collidelist(top_plats)!=-1: #CHANGED THIS TO MARIO RECT, MAYBE USING MARIO RECT IS MORE USEFUL - TRY IT! 
            State="Standing"

        elif right_side.collidelist(platforms)!=-1: 
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side

           #CHANGED THIS... 
        elif top.collidelist(barriers)!=-1 and bottom.collidelist(top_plats)==-1: # this means that he hit the underside of the platform
            State="Bounce"
            if bothplatforms[top.collidelist(barriers)][1]=="question block": # if it was a question block we set to an empty block
                bothplatforms[top.collidelist(barriers)][1]="empty block"
                blockevents( bothplatforms[top.collidelist(barriers)][2],bothplatforms[top.collidelist(barriers)][0][0],bothplatforms[top.collidelist(barriers)][0][1]-32,x,y,mx,my,deltax,top.collidelist(barriers))
  
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
    list1=[[Rect(0,600-32,2000,20),"block 1","none"],[Rect(800,450,32,500),"question block","mushroom"],[Rect(900,450,32,32),"question block","mushroom"],[Rect(1000,450,32,32),"question block","mushroom"],[Rect(1100,450,32,32),"question block","flower"],[Rect(200,450,32,450),"question block",None],[Rect(1500,450,32,500),"question block",None]] #bottom most layer, 
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
            


    

def jump(x,y,intial_velocity,delta_x,gravity_change,pictures,boolean,mx,my,oldx,mario_size):  #mario size represents what stage he's in # make intial velocity negative, boolean represents left jump image
    gravity=0
    #ALWAYS CHECK TO SEE IF HE'S SUPER OR SMALL 
    while True:
        #event.get()
        #if key.get_pressed()[K_RIGHT]==True: #ABILITY TO TURN AROUND IN THE AIR
        #  #  delta_x+=.07
          #  if delta_x==4: #SET PARAMETERSSS, so he can 't mvoe like 57105815 metres
            #    delta_x=3.5
          #  boolean=False
       # if key.get_pressed()[K_LEFT]==True:
           # delta_x-=.07
            #if delta_x==-4:
             #   delta_x=-4
           # boolean=True
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase

        #for i in range here...divide delta x by ratio?
        y+=change #change the  y
        x+=delta_x #change the x
      #  time.wait(10)
        mx=mx-delta_x
        drawMario(screen,x,y,pictures,boolean,mx,my,delta_x,mario_size) #draw mario, use the delta_x to indiciate the change
    #for i in range...maybe make a range and go through it, might make collisions better 
        standingCheck(True,x,y,mx,my,deltax)
        if State=="Standing":
            pictures=pictureCheck(mario_size,"Standing")
            mario_size=drawMario(screen,x,y,pictures,boolean,mx,my,delta_x,mario_size) #if standing then we stop, possible program w/ this  
            return mx,my,x,y,mario_size           
        #print State
        if State=="Bounce": # if he hit the underside then we just jump again but this time with no velocity,a nd high gravity to make him fall#
            pictures=pictureCheck(mario_size,"Jumping Right")
            return jump(x,y,3,delta_x,.4,pictures,boolean,mx,my,oldx,mario_size) #GRAVITY STAYS THE SAME REVERSE VELOCITY
        if State=="Bounce2" or State=="Bounce3":
            pictures=pictureCheck(mario_size,"Standing")
            return jump(x,y,5,0,.4,pictures,boolean,mx,my,oldx,mario_size) #mGRAVITY STYAS THE SAME, REVERSE VELOCTIY
    
        Deathcheck(x,y)
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax,mario_size): #draws mario with various animations
  #  global mario_rect
    if mario_size=="small":
       mario_rect=Rect(400,y,34,34)  #maybe give it a length...each time it changes draws a new one?
    if mario_size=="Super" or mario_size=="Fire":
        mario_rect=Rect(400,y-34,40,64)
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first
    mario_size=Interactions(mario_rect,mario_size,y)

    for pic in pic_list:
    
        if leftflag==True: #flips the image if its on the left side 
            pic=transform.flip(pic,True,False)
    
        screen.blit(updated_screen,(0,0)) #blits the updated screen

        screen.blit(pic,mario_rect) #blits mario
        display.flip()
 
        screen.fill(black)

    return mario_size

############

fireball_list=[None,None]
fireballgravity1=0
fireballgraivty2=0
fireballcount=0



########

Enemies=[["koopa",Rect(450,300,32,48),6,(32,48),False],["goomba",Rect(300,300,32,32),3,(32,32),False]]        #[name,rectangle,speed,dimensions,reverseflag]


Obstacles=twodim(10,3) #change this to 3 so that you can control the speed 


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
    
  #  print "moose"
    event.get()
    standingCheck(platforms,x,y,mx,my,deltax) #only need to do this once, PERHAPS, TRY EXPERIMENTING W/ THIS 

    if Facing=="Right": #make a function, this determines the facing
        leftflag=False
    if Facing=="Left":
        leftflag=True

    horizontal_movement,speed=movementcheck(State,Facing)

    Deathcheck(x,y)
    
    if key.get_pressed()[27]==True:
        quit()

    #PUT ALL THIS INTO A FUNCTION
    if State=="Falling":
        y=y+10
        #Sizecheck(screen,x,y,standing,False,mx,my,"Standing")
       # drawMario(screen,x,y,standing,False,mx,my,0,mario_size)#changed this to zero 
    
    if State=="Standing" or State=="Bounce2" or State=="Bounce3": #Bounce2 and Bounce3 are collision states
        
            
        if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
           # changemusic(0,1)  #ask sir about this
           
           standingCheck(platforms,x+horizontal_movement,y,mx,my,deltax) #to make sure he can't jump through platforms
          # print State
           if State=="Standing":
               Facing="Right"
               pictures=pictureCheck(mario_size,"Jumping Right")
               mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement,gravityforce,pictures,False,mx,my,deltax,mario_size) #boolen is for left flag
               
        elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
           # changemusic(0,1)
            standingCheck(platforms,x-horizontal_movement,y,mx,my,deltax) #to make sure he can't jump through things
            Facing="Left"
            if State=="Standing":
                pictures=pictureCheck(mario_size,"Jumping Left")
                mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement*(-1),gravityforce,pictures,True,mx,my,deltax,mario_size)
                
        elif key.get_pressed()[K_SPACE]==True:# jumping straight up
           # changemusic(0,1)
            Facing=Facing #special case...where we check the facing to see how he jumps 
            if Facing=="Right": #CHANGET HIS BECAUSE HE CAN JUMP THROUGH PLATFORMSSS
                leftflag=False
                movement=1 #works because its positive/negative
                pictures=pictureCheck(mario_size,"Neutral Jumping")
                mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size)
            if Facing=="Left":
                leftflag=True
                movement=-1 
                pictures=pictureCheck(mario_size,"Neutral Jumping")
                mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size)
            
        elif key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
            Facing="Right"
            standingCheck(platforms,x+speed,y,mx,my,deltax) #MAKE THIS NON GLOBAL
            if State=="Bounce3": #if he would collide, then we speed to zero because that can'
                speed=0
            x+=speed
            mx=mx-speed
            deltax=x-oldx
            pictures=pictureCheck(mario_size,"Moving Right")
          #  pictures=running_list
            mario_size=drawMario(screen,x,y,pictures,False,mx,my,deltax,mario_size) #for run animation

        elif key.get_pressed()[K_LEFT]==True:
            Facing="Left"
            standingCheck(platforms,x-speed,y,mx,my,deltax)
            if State=="Bounce2": #if he would collide we set his sppeed to zero cause he can't, but he can move hte other way
                speed=0
            x=x-speed
            mx=mx+speed
            deltax=x-oldx
            pictures=pictureCheck(mario_size,"Moving Left")
            mario_size=drawMario(screen,x,y,pictures,True,mx,my,deltax,mario_size) #for run animation

        elif key.get_pressed()[K_f]==True and mario_size=="Fire": #have a counter for this
            print "Fire" #if evnt.type == KEYDOWN: ...then figure out the number value of the key
            fireball_list[0]=Rect(438,y,16,16)
            drawMario(screen,x,y,throwanimation,leftflag,mx,my,0,mario_size)
           # fireballcount+=1
        #    movefireball(                    # (intial_velocity,horizontal_movement,gravity)
            
   # print deltax
    if x==oldx: #if he's not moving we just draw it, this ways the obstacles can move tooo
        #print "gay"
        pictures=pictureCheck(mario_size,"Standing")
        mario_size=drawMario(screen,x,y,pictures,leftflag,mx,my,0,mario_size)


    oldx=x
    oldy=y


    
            
    myClock.tick(30)
    

    
