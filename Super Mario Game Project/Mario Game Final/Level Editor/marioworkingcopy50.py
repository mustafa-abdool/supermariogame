#Agenda...

#problems w/ mario jumping just like "warps" to the top...

#for Interactions just ask if INvinble flag is false befoe ANY CHECKS...might reduce lag(not that there is any, yo)

#make mario throw hammers

#koopa shell can kill you sometimes when you try to "kick it" ---> only when going ONE WAY

#MAKE MARIO NOT BE INVINCIBLE ONCE THE GAME "RESTARS", JUJT MAKE AN ELSE STATEMENT,

#temp enemies too


#MAKE THE ONSCREEN CHECK LIKE -100, 700 SO THEY CAN STILL "KIND OF" MOVE...HAVE TO CHECK ACTUAL GAME FOR THIS 

#MAKE A LIST OF ALL TEMP PLATFORMS THAT CAN BE SEEN...IT'LL BE EASIER TO EHCK FOR COLLISIONS IF YOU HAVE LIKE 50285285 PLATFORMS

#MAKE A LIST OF ALL THE PLAFORMS TAHT ARE CURRENTLY ON SCREEN, IT'LL BE EASIER THAT WAY..

#bowser SHOOTS fireballs and HAMMERS, ADD IN AN EXTRA VARIABLE NUB


#FIX ALL ABILITY FOR THINGS TO BE ON SCREEN...ITS LIKE RECT[0]+RECT[2]-MARIO_POS<0 OR RECT[0]-MARIO_POS>600

#MAKE BRICK SHATTER!!






#enenemy animations


#problem w/ shell collision...will still mess up


#always check if seeflag is true before you can start drawing/moving the enemies...will probably save time later on 


#speed of projectile must be greater than speed of enemey


#CREATE SOME KIND OF DELAY TIMER FOR THE ENEMIES WHEN THEY ARE SQUISHED (LIKE THE GOOMBA)



#always check for active/inactive...? Maybe less work..you won't be moving it if they are not on the screen..?



#break things up into more functions 



#pipes



#coins out of blocks


#level editor
#move screens, just add a variable, +600*scren, etc,etc onto the x coord
#use paint program stuff to do so 




#What's left to do...


#bowser etc

#enemy animations
#piranha plants
#pipes



#beanstalks?




####################################



from pygame import*
from random import*
from colours import *
from math import *
from glob import *

init()
size=width,height=600,600
screen=display.set_mode(size)



font_type=font.SysFont("Times New Roman",40) #gets the Times New Roman Font


#my_screen=Rect(0,0,600,600)
#screen.set_clip(my_screen)
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

standing=[image.load("Mario Stand.png"),image.load("Mario Stand.png"),image.load("Mario Stand.png"),image.load("Mario Stand.png")]

big_standing=[image.load("Super Mario Stand.png"),image.load("Super Mario Stand.png"),image.load("Super Mario Stand.png"),image.load("Super Mario Stand.png")]

fire_standing=[image.load("Fiery Mario Stand.png"),image.load("Fiery Mario Stand.png"),image.load("Fiery Mario Stand.png"),image.load("Fiery Mario Stand.png")]

########################################################

running_list=[mario1,mario2,mario3,mario4] # list of running animation

big_running_list=[mario5,mario6,mario7]

fire_running_list=[mario8,mario9,mario10]

#################################################

jumplist=[image.load("Mario Jump.png"),image.load("Mario Jump.png"),image.load("Mario Jump.png"),image.load("Mario Jump.png")] #jumping animation

big_jumplist=[image.load("Super Mario Jump.png"),image.load("Super Mario Jump.png"),image.load("Super Mario Jump.png"),image.load("Super Mario Jump.png")]

fire_jumplist=[image.load("Fiery Mario Jump.png"),image.load("Fiery Mario Jump.png"),image.load("Fiery Mario Jump.png"),image.load("Fiery Mario Jump.png")]


################

throwanimation=[image.load("Fiery Mario Throw.png"),image.load("Fiery Mario Throw.png"),image.load("Fiery Mario Throw.png"),image.load("Fiery Mario Throw.png")]

##############################

hammer_running_list=[image.load("hammer run 1 copy.PNG"),image.load("hammer run 2 copy.PNG"),image.load("hammer run 3 copy.PNG"),image.load("hammer run 4 copy.PNG")]

hammer_jumplist=[image.load("hammer jump 1 copy.PNG"),image.load("hammer jump 1 copy.PNG") ,image.load("hammer jump 1 copy.PNG") ,image.load("hammer jump 1 copy.PNG") ]                    
    

hammer_standing=[image.load("hammer run 1 copy.PNG"),image.load("hammer run 1 copy.PNG"),image.load("hammer run 1 copy.PNG"),image.load("hammer run 1 copy.PNG")]






####################################################


Enemiesdictionary={}

Enemiesdictionary['goomba']=image.load("Goomba 2 w-2.png")

Enemiesdictionary['koopa']=image.load("Green Koopa 1.png")

Enemiesdictionary['goomba dead']=image.load("Goomba Dead w-2.PNG")

Enemiesdictionary['flying koopa']=image.load("sm-koopaparatroopa.GIF")

Enemiesdictionary['flying koopa dead']=image.load("Green Shell.PNG")

Enemiesdictionary['hammer bros']=image.load("um-hammerbros.GIF")

Enemiesdictionary['koopa dead']=image.load("Green Shell.PNG")

Enemiesdictionary['birdo']=image.load("silver_birdo_sheet92.PNG")

Enemiesdictionary['bowser']=image.load("sm-bowser.GIF")

Enemiesdictionary['dry bones']=image.load("um-drybones.GIF")

Enemiesdictionary['buzzy beetle']=image.load("sm-buzzybeetle.GIF")

Enemiesdictionary['cheep cheep']=image.load("sm-cheepcheep.GIF")

Enemiesdictionary['lakitu']=image.load("sm-lakitu.GIF") #how to do lakitu...?

Enemiesdictionary['piranha plant']=image.load("sm-piranhaplant.GIF")

Enemiesdictionary['podoboo']=image.load("sm-podoboo.GIF") #put this in obstacles maybe..?

Enemiesdictionary['kuribos goomba']=image.load("um-kuribosgoomba.GIF")

Enemiesdictionary['spark']=image.load("mw-spark.GIF")

Enemiesdictionary['snifit']=image.load("mw-snifit.GIF")

Enemiesdictionary['cobrat']=image.load("mw-cobrat.GIF") 





###############################################

image.load("Block World 1.PNG")

Scenerylist=[(image.load("Block World 1.PNG")),(image.load("Grass Middle.PNG")),(image.load("Cloud.PNG")),(image.load("Question Block 1.PNG"))]

Scenerydictionary={}
Scenerydictionary["block 1"]=image.load("Block World 1.PNG")
Scenerydictionary["grass"]=image.load("Grass Middle.PNG")
Scenerydictionary["cloud"]=image.load("Cloud.PNG")
Scenerydictionary["question block"]=image.load("Question Block 1.PNG")
Scenerydictionary["empty block"]=image.load("Empty Block.PNG")
Scenerydictionary['trampoline']=image.load("trampoline.PNG")
Scenerydictionary['moving platform']=image.load("Platform Large.PNG")

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
Obstaclesdictionary={}

Obstaclesdictionary['flower']=image.load("Fire Flower 1.png")
Obstaclesdictionary['mushroom']=image.load("Mushroom.png")
Obstaclesdictionary['coin']=image.load("Coin 1.png")
Obstaclesdictionary['koopa shell']=image.load("Green Shell.png")
Obstaclesdictionary['trampoline']=image.load("trampoline.png")
Obstaclesdictionary['bullet bill']=image.load("sm-bulletbill.GIF")


beanstalkimage=image.load("beanstalk copy.png") #MAKE THIS A DICTIONARY THEN YOU WON'T HAVE TO GLOBAL STUFFF
mushroompic=image.load("Mushroom.png")
screen2=Rect(0,0,600,600) #rectangles which represents the screen
flowerpic=image.load("Fire Flower 1.png")
fireballpic=image.load("Fireball.png")
#coin1=image.load("Coin 1.png")

#########################################################


projectile_hammer=image.load("um-hammer.GIF") #make dictionary

projectile_fireball=image.load("fireball_image.PNG")

#####################################################


Otherdictionary={}

Otherdictionary['lives icon']=image.load("Lives Icon.PNG")
Otherdictionary['coin']=image.load("Coin 1.png")



#####################################################


def twodimcopy(twodlist): #makes a copy of two dimensional list...this was some hard stuff to do mannnn
    length1=len(twodlist)
    length2=len(twodlist[0])
    new=twodim(length1,length2) #fisrt makes a new twod list with the same paramters as the original
    for i in range(len(twodlist)):
        for j in range(len(twodlist[i])):
            value=twodlist[i][j]
            if str(twodlist[i][j])[1:5]=='rect': #if its a rect then we have to make a whole new rect thingy, cause it will write to the same spot in mem
                value=Rect(twodlist[i][j][0],twodlist[i][j][1],twodlist[i][j][2],twodlist[i][j][3]) #ory 
            new[i][j]=value
    return new


def reset(): #don't global stuff....
    global Dynamic_Enemies
    global Presets
    global Dynamic_Projectiles
    global bothplatforms
    global Obstacles
    global Obstaclevariable
    global barriers
    global top_plats
    global platforms
 
    Presets=twodimcopy(DEFAULT_PRESETS) #revert everything to defaults 
    Dynamic_Enemies=twodimcopy(DEFAULT_ENEMIES)
    Dynamic_Projectiles=twodim(10,6)
    bothplatforms=twodimcopy(DEFAULT_PLATFORMS)
    Obstacles=twodimcopy(DEFAULT_OBSTACLES)
    barriers=twodimcopy(DEFAULT_BARRIERS)
    top_plats=twodimcopy(DEFAULT_TOP_PLATS)
    platforms=twodimcopy(DEFAULT_PLATFORMSNORM)
    Obstaclevariable=0

    

#DEFAULT_PLATFORMSNORM=twodimcopy(platforms)
 #   print Dynamic_Projectiles


    #stuff to do
    # -obstacles
    # projectiles
    # yeppp...


def drawMenu():
    screen.blit(Otherdictionary['lives icon'],(50,25))
    Drawtext("x"+" "+str(LIVES),40,(80,10),red)
    screen.blit(Otherdictionary['coin'],(240,25))
    Drawtext("x"+" "+str(coincount),40,(270,10),red)
    Drawtext("TIME"+" "*3+str(TIMER),40,(400,10),red)


def Drawtext(words,size,(x,y),colour): #function that gets text size and a position from the user and draws it to the screen

    #SIZE DOESN'T MATTER...CAUSE I CHANGED AROUND THE FUNCTION AND STUFF
    text=font_type.render(words,True,colour) #writes the text
    screen.blit(text,(x,y)) #blits text to the screen

            


def sizeCheck(mario_size):#tell if he gets hit
 #   global mario_size
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer":
        return "small"
    elif mario_size=="small":
        return "death"

    
def seeCheck(x,y,Rectobject):
    flag=False
    mario_pos=x-400 #changed this
    if not Rectobject[0]+Rectobject[2]-mario_pos<0 and not Rectobject[0]-mario_pos>600:
        flag=True
    return flag
    


def movedynamic_enemies(x,y):

    global projectilevariable
    global Obstaclevariable

    mario_pos=x-400 #looks like [name,rect,speed,dimensions,jump height,horizontal jump movement,acc gravity,state,
    
    for i in range(len(Dynamic_Enemies)):
        name=Dynamic_Enemies[i][0]
        dimensions=Dynamic_Enemies[i][3]
        jump_height=Dynamic_Enemies[i][4]
        horizontal_movement=Dynamic_Enemies[i][5]
        siderect=Rect(Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][3][0],Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)# represents rectangle at the side
        siderect2=Rect(Dynamic_Enemies[i][1][0]-3,Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)
        Dynamic_Enemies[i][1][1],State=EnemeyStatecheck(Dynamic_Enemies[i][1],siderect,siderect2,Dynamic_Enemies[i][1][1],Dynamic_Enemies[i][7])
      #  print State


        
        if seeCheck(x,y,Dynamic_Enemies[i][1])==True:
        

            if Dynamic_Enemies[i][13]==300:
                Dynamic_Enemies[i][13]=0


            if projectilevariable==10: #probably won't have more than 10 projectiles at a time...but just incase, y'know 
                projectilevariable=0
           
            if Dynamic_Enemies[i][1][1]>600: #death check
                del Dynamic_Enemies[i]
                break


            if Dynamic_Enemies[i][7]=="flying":

                if abs(Dynamic_Enemies[i][16])>Dynamic_Enemies[i][17]: #if hit wall reverse velocity
                    Dynamic_Enemies[i][2]*=-1


                if Dynamic_Enemies[i][13]%Dynamic_Enemies[i][11]==0: # WALKING/MOVING...elif so he won't like fall sideways and stuff
                       Dynamic_Enemies[i][1][1]+=Dynamic_Enemies[i][2]
                       Dynamic_Enemies[i][16]+=Dynamic_Enemies[i][2]

                pic=Enemiesdictionary[Dynamic_Enemies[i][0]]

                

            if Dynamic_Enemies[i][7]=="alive":
                if State=="Bounce" or abs(Dynamic_Enemies[i][16])>Dynamic_Enemies[i][17]: #if hit wall reverse velocity 
                    Dynamic_Enemies[i][2]=Dynamic_Enemies[i][2]*-1
                    Dynamic_Enemies[i][5]*=-1
                    State="Moving"
                    
                    if Dynamic_Enemies[i][15]==True: #reverse direction he's facing...upon bounce thing?
                        Dynamic_Enemies[i][15]=False
                    elif Dynamic_Enemies[i][15]==False:
                        Dynamic_Enemies[i][15]=True

                        
                if State=="Moving": #jumping
                    Dynamic_Enemies[i][6]=0
                    Dynamic_Enemies[i][8]=False
                    Dynamic_Enemies[i][13]+=1

                    if Dynamic_Enemies[i][13]%Dynamic_Enemies[i][12]==0: #SHOOTING
                        constant=1
                        if Dynamic_Enemies[i][2]<0: #makes the projectile go the other way depending on how he is facing
                            constant=-1
                        if Dynamic_Enemies[i][14]=="parabolic":
                            Dynamic_Projectiles[projectilevariable][0]=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],54,54) #changed for hammer
                            Dynamic_Projectiles[projectilevariable][1]=0 #make a variable for this
                            Dynamic_Projectiles[projectilevariable][2]=randint(-20,-6)  #intial velocity...?
                            Dynamic_Projectiles[projectilevariable][3]=-3*constant #movement horizontally, adds in an element of randomness
                            Dynamic_Projectiles[projectilevariable][4]="parabolic"
                            Dynamic_Projectiles[projectilevariable][5]=0 #angle representation
                            projectilevariable+=1
                        if Dynamic_Enemies[i][14]=="straight":
                            Dynamic_Projectiles[projectilevariable][0]=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],16,16)
                            Dynamic_Projectiles[projectilevariable][1]=-5*constant #make a constant...such as 1, -1, change this as the bounce flag triggers
                            Dynamic_Projectiles[projectilevariable][4]="straight"
                            projectilevariable+=1
                

                if  Dynamic_Enemies[i][13]%Dynamic_Enemies[i][10]==0: # JUMPING

                    change=jump_height+Dynamic_Enemies[i][6] #jump height has to be negative
                    Dynamic_Enemies[i][6]+=.4 #increase gravity
                    Dynamic_Enemies[i][1][1]+=change
                    Dynamic_Enemies[i][1][0]+=horizontal_movement
                    Dynamic_Enemies[i][8]=True
                    Dynamic_Enemies[i][16]+=horizontal_movement

                if State=="Falling":
                    Dynamic_Enemies[i][1][1]+=5
                    
                elif Dynamic_Enemies[i][13]%Dynamic_Enemies[i][11]==0: # WALKING/MOVING...elif so he won't like fall sideways and stuff
                       Dynamic_Enemies[i][1][0]+=Dynamic_Enemies[i][2]
                       Dynamic_Enemies[i][16]+=Dynamic_Enemies[i][2]
                       
                        
                            

                                        
            

                pic=Enemiesdictionary[Dynamic_Enemies[i][0]]
                
                if Dynamic_Enemies[i][15]==True: #flips it if the direction is reversed 
                    pic=transform.flip(pic,True,False) 
        

            elif Dynamic_Enemies[i][7]=="dead": #check if they are dead
               # print Enemies[i][0]
                if Dynamic_Enemies[i][0]=="koopa dead" or Dynamic_Enemies[i][0]=="flying koopa dead":
                    Obstacles[8][0]=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],32,32) #a bit lower so it doesn't collide with everything 
                    Obstacles[8][1]="koopa shell"
                    Obstacles[8][2]=0
                    Obstaclevariable+=1
                else:
                    pic=Enemiesdictionary[Dynamic_Enemies[i][0]]

                del Dynamic_Enemies[i]
                break

            elif Dynamic_Enemies[i][7]=="fire dead":
                pic=Enemiesdictionary[Dynamic_Enemies[i][0]]
                pic=transform.flip(pic,False,True)
                Dynamic_Enemies[i][1][1]+=3
                
            if not Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][1][2]-mario_pos<0 and not Dynamic_Enemies[i][1][0]-mario_pos>600: #checks if the enemey can be seen onscreen
                screen.blit(pic,(Dynamic_Enemies[i][1][0]-mario_pos,Dynamic_Enemies[i][1][1])) #if they can be then we draw them

          #  print Dynamic_Enemies[i][16]
            
    
        

        
    
    

def move_dynamicprojectiles(x,y): #[rect, acc gravity, intial_v,horizontalmovement
    mario_pos=x-400
    for i in range(len(Dynamic_Projectiles)):
        if Dynamic_Projectiles[i][0]!=None:
            
            pic=projectile_hammer #incase it goes through anyways, but it would be tooo high up to seeeeee =D =( =)

            if Dynamic_Projectiles[i][4]=="straight":
                
                pic=projectile_fireball

                if Dynamic_Projectiles[i][1]>0:
                    pic=transform.flip(pic,True,True)

               # pic=projectile_fireball
                Dynamic_Projectiles[i][0][0]+=Dynamic_Projectiles[i][1] #increase speed

            if Dynamic_Projectiles[i][4]=="parabolic":
                
                pic=projectile_hammer
            
                siderect=Rect(Dynamic_Projectiles[i][0][0]-6,Dynamic_Projectiles[i][0][1],6,10)
                siderect2=Rect(Dynamic_Projectiles[i][0][0]+14,Dynamic_Projectiles[i][0][1],6,10)
                State=Statecheck2(Dynamic_Projectiles[i][0],siderect,siderect2)                                            
                change=Dynamic_Projectiles[i][2]+Dynamic_Projectiles[i][1]
                Dynamic_Projectiles[i][1]+=.4 #increase gravity
                Dynamic_Projectiles[i][0][1]+=change
                Dynamic_Projectiles[i][0][0]+=Dynamic_Projectiles[i][3] #horizontal movement
                Dynamic_Projectiles[i][5]+=5 #angle increase
                if Dynamic_Projectiles[i][5]==360:
                    Dynamic_Projectiles[i][5]=0
                pic=transform.rotate(pic,Dynamic_Projectiles[i][5]) #rotate by angle
                
            if not Dynamic_Projectiles[i][0][0]+Dynamic_Projectiles[i][0][2]-mario_pos<0 and not Dynamic_Projectiles[i][0][0]-mario_pos>600:

                screen.blit(pic,(Dynamic_Projectiles[i][0][0]-mario_pos,Dynamic_Projectiles[i][0][1]))
            

        
        

        
def movefireball(intial_v,gravity,x): #moves fireballs, 
    global fireballcount
    mario_pos=x-400
    for i in range(len(fireball_list)):
     #   print fireball_list[fire]
        if fireball_list[i][0]!=None:
            fireball_list[i][2]+=gravity #increase gravity
            change=intial_v-fireball_list[i][2] #calculaet change
            fireball_list[i][0][1]+=change #increase y
            fireball_list[i][0][0]+=fireball_list[i][1]# increase x

            siderect=Rect(fireball_list[i][0][0]-6,fireball_list[i][0][1],6,10)
            siderect2=Rect(fireball_list[i][0][0]+14,fireball_list[i][0][1],6,10)
            
            
                
            State=Statecheck2(fireball_list[i][0],siderect,siderect2) #check the state, for FIREBALLS
          #  print State
            if State=="Moving":
                fireball_list[i][2]=0 #don't need the line below this if we're already blitting it..?
                screen.blit(fireballpic,(fireball_list[i][0][0]-mario_pos,fireball_list[i][0][1])) #OUT OF RANGE ERRORS 
            if State=="Bounce" or fireball_list[i][0][1]>600:
                del fireball_list[i] #delete the old one
                fireball_list.insert(0,[None,None,None]) #insert the new one
                #fireball_list[i][0]=None
               # fireball_list[i][1]=None
               # fireball_list[i][2]=None
                fireballcount=0 # set it back to zero which would be the blank one 
                break   #CHECK IF THE FIREBALLS ARE ON SCREEN
            screen.blit(fireballpic,(fireball_list[i][0][0]-mario_pos,fireball_list[i][0][1])) #OUT OF RANGE ERRORS 
            


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
    if mario_size=="Hammer":
        if Action=="Jumping Right" or Action=="Jumping Left" or Action=="Neutral Jumping":
            return hammer_jumplist
        if Action=="Moving Right" or Action=="Moving Left":
            return hammer_running_list
        if Action=="Standing":
            return hammer_standing        


def Interactions(Rectobject,mario_size,y,x,deltax,leftflag,mx,my,oldx): #pass in mario_size, if nothing happens then we return it, PASS IN STATE AND FACING LATER
    global State
    global coincount
    global Facing
    global fireballcount
    global Invincibleflag
    global Invinciblecounter
    global LIVES
    global Dynamic_Enemies



    collideflag=False
    
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer":
        mario_rect=Rect(x,y-34,40,64)
        bottom=Rect(x,y+34,34,4) 


    if mario_size=="small":
        mario_rect=Rect(x,y,34,34)
        bottom=Rect(x,y+34,34,4) 

    temp_obstacles=[]
    for i in range(len(Obstacles)): #fix THIS, SO THAT ONLY THE ONES THAT CAN BE SEEN GET INCLUDED
        temp_obstacles.append(Obstacles[i][0])
        
    temp_presets=[] #get all the preset stuff
    for i in range(len(Presets)):
        temp_presets.append(Presets[i][0])

    if Rectobject.collidelist(temp_presets)!=-1: #check for pre set collisions
        pos=Rectobject.collidelist(temp_presets)
        if Presets[pos][1]=="coin": #check if its a coin
           coincount+=10
           if coincount>100:
               LIVES+=1
               coincount=coincount%100
           del Presets[pos]
        elif Presets[pos][1]=="trampoline":
          #  print "trampoline collide"
            if bottom.collidelist(temp_presets)!=-1:
                #print "trampoline collide"
                return jump(x,y,-10,deltax,.4,jumplist,False,mx,my,oldx,mario_size,fireballcount) #if he hits it he bounces off
                    #BWHAHHAHA SO COOL
        elif Presets[pos][1]=="bullet bill" and Invincibleflag==False:
                mario_size=sizeCheck(mario_size)
                if mario_size=="death":
                    LIVES-=1
                    if LIVES==0:
                        quit()
                    x=400
                    y=400
                    mx=-100
                    my=0
                    mario_size="small"
                    State="Falling"
                    reset()
                else:
                    Invincibleflag=True
                    Invinciblecounter=0

        
    if Rectobject.collidelist(temp_obstacles)!=-1: #checks for temp obstacles collisions 
        pos=Rectobject.collidelist(temp_obstacles)
        if Obstacles[pos][1]=="coin":
            del Obstacles[pos]
            coincount+=1
        elif Obstacles[pos][1]=="flower":
            #if State=="Standing":
            del Obstacles[pos]
            mario_size="Fire"
        elif Obstacles[pos][1]=="koopa shell":

            if State=="Falling": #don't delete make it none
                return jump(x,y,-7,deltax,.4,jumplist,False,mx,my,oldx,mario_size,fireballcount) #if he hits it he bounces off
            elif State=="Standing": #if he hits it when he's running
                if Obstacles[pos][2]==0: #and it hasn't been moved yet
                    if Facing=="Right": #we make it have some speed
                        Obstacles[pos][2]=Koopashellspeed
                        Obstacles[pos][0][0]+=Koopashellspeed #we have to moev it so it won't collide right away
                    elif Facing=="Left":
                        Obstacles[pos][2]=Koopashellspeed*(-1)
               #     Invincibleflag=True 
                        Obstacles[pos][0][0]+=Koopashellspeed*-1 #we have to moev it so it won't collide right away
                else: #else he's deadddd mannn deadddd =(
                    if Invincibleflag==False:
                        mario_size=sizeCheck(mario_size)
                        if mario_size=="death":
                            LIVES-=1
                            if LIVES==0:
                                quit()
                            x=400
                            y=400
                            mx=-100
                            my=0
                            mario_size="small"
                            State="Falling"
                            reset()
                        else:
                            Invincibleflag=True
                            Invinciblecounter=0
                                
        elif Obstacles[pos][1]=="mushroom":
            del Obstacles[pos]
            mario_size="Super"


    temp_enemies=[]

    #CHECK IF THEY ARE ONSCREEEEN
    for i in range(len(Dynamic_Enemies)):
        if Dynamic_Enemies[i][7]=="alive" or Dynamic_Enemies[i][7]=="flying": #he can only collide and stuff if he's flying/alive
            temp_enemies.append(Dynamic_Enemies[i][1])


   # collideflag=False
    if State=="Falling":     #has to be fallikng for him to kill the enemey
        if bottom.collidelist(temp_enemies)!=-1: #
            collideflag=True
            pos=bottom.collidelist(temp_enemies) #if the bottom collides, then the enemey is dead, add dying aniamtion
            if Dynamic_Enemies[pos][18]==True: #sees if he can be killed by jumping on  
                Dynamic_Enemies[pos][7]="dead" #make his state dead
                Dynamic_Enemies[pos][0]=Dynamic_Enemies[pos][0]+" "+"dead"  #koopa can fall
                drawFullscene(screen,x,y,mx,my,deltax)  #draw scene
       #         display.flip() #update
           #     time.wait(50) #delay
                mx,my,x,y,mario_size=jump(x,y,-5,deltax,.4,jumplist,leftflag,mx,my,oldx,mario_size,fireballcount) #gets picutres for this
            
            
    if collideflag==False:
        if mario_rect.collidelist(temp_enemies)!=-1 and Invincibleflag==False: #if anyother part of mario collides then he's dead
         #   print ""
            mario_size=sizeCheck(mario_size)
            if mario_size=="death":
                LIVES-=1
                if LIVES==0:
                    quit()
                x=400
                y=400
                mx=-100
                my=0
                mario_size="small"
                State="Falling"

                reset()
                
              #  oldenemies=twodimcopy(DEFAULTS,new)
              #  return oldenemies
             #   Dynamic_Enemies=reset("Enemies")
            else:
                 Invincibleflag=True
                 Invinciblecounter=0
            


    for i in range(len(fireball_list)): #checks if the fireball collides with an eenmey
        if fireball_list[i][0]!=None:
            if fireball_list[i][0].collidelist(temp_enemies)!=-1:
                pos=fireball_list[i][0].collidelist(temp_enemies)

                if Dynamic_Enemies[pos][19]==0: #checks if they can be killed by fireballs
                        Dynamic_Enemies[pos][7]="fire dead"

                else: #if they can't be killed yet we decrease this by one and delete the fireball 
                    Dynamic_Enemies[pos][19]-=1
                    
                del fireball_list[i]
                fireball_list.insert(0,[None,None,None])
                fireballcount=0



    temp_projectiles=[]
    for i in range(len(Dynamic_Projectiles)):
        if Dynamic_Projectiles[i][0]!=None:
            temp_projectiles.append(Dynamic_Projectiles[i][0])

    if mario_rect.collidelist(temp_projectiles)!=-1 and Invincibleflag==False: #PROJECTILE COLLISONS
        print 'projectile collision'
        mario_size=sizeCheck(mario_size)
        if mario_size=="death":
            LIVES-=1 #lowers lives
            if LIVES==0:
                quit()
            x=400# set defaults
            y=400
            mx=-100
            my=0
            mario_size="small" # set size/state
            State="Falling"

            reset()
        else:
            Invincibleflag=True
            Invinciblecounter=0

    if mario_rect.collidelist(roto_rects)!=-1 and Invincibleflag==False:  #ROTO DISK COLLISIONS
        print 'roto collision'
        mario_size=sizeCheck(mario_size)
        if mario_size=="death":
            LIVES-=1 #lowers lives
            if LIVES==0:
                quit()
            x=400# set defaults
            y=400
            mx=-100
            my=0
            mario_size="small" # set size/state
            State="Falling"

            reset()
        else:
            Invincibleflag=True
            Invinciblecounter=0
        
                
            
    return mx,my,x,y,mario_size 
            
            
def twodimvalue(row,col,value):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append(value) 
        list1.append(temp)
    return list1

    
def twodim(row,col):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append((Rect(1,-500,1,1))) 
        list1.append(temp)
    return list1

def Statecheck2(Rectobject,siderect,siderect2):# FOR FIREBALLS, WE WANT TO CHECK IF IT HITS THE WALL FIRST YO


    if siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
        State="Bounce"
    elif Rectobject.collidelist(top_plats)==-1: #they are either falling or moving 
        State="Falling"
    else:
        State="Moving"

    return State

def EnemeyStatecheck(Rectobject,siderect,siderect2,ycoord,State):

    if State!='fire dead':

        if Rectobject.collidelist(platforms)!=-1: # set his y coord to the 
           pos=Rectobject.collidelist(platforms)
           ycoord=platforms[pos][1]-Rectobject[3]+1 #its not really 48...its the size or w/e
           State="Moving"

        elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
            State="Falling"
        elif siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
            State="Bounce"
     #   else:
          #  State="Moving"

    return ycoord,State

def Statecheck(Rectobject,siderect,siderect2):#almost like standing check except for obstacles, and is much less complicated

    if Rectobject.collidelist(top_plats)==-1: #they are either falling or moving 
        State="Falling"
    elif siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
        State="Bounce"
    else:
        State="Moving"

    return State

def drawPresets(x,y):
    mario_pos=x-400
    mario_pos=round(mario_pos)
   # temp_presents=[]
    for object1 in Presets:
        if object1[1]=="coin" or object1[1]=="trampoline":
            if not object1[0][0]-mario_pos<0 and not object1[0][0]-mario_pos+object1[0][2]>600:
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))
        if object1[1]=="bullet bill":
            object1[0][0]+=-5
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600: #checks if its on screen
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))
            if object1[0][0]-mario_pos<0:
                object1[0]=Rect(randint(mario_pos+600,mario_pos+2000),randint(1,580),54,48) #if it goes off we draw a new one, yo, cause thats how I roll
                object1[1]="bullet bill"
            



def drawObstacles(Displayflag,x,y,mx,my,deltax): #what is displayflag...?
    global Jumpflag
    for object1 in Obstacles:
        mario_pos=x-400
        if object1[1]=="flower": #flowers don't move  #CHECK IF THE OBJCET IS ONSCREEN
            if not object1[0][0]-mario_pos<0 and not object1[0][0]-mario_pos+object1[0][2]>600:
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))
                
        if object1[1]=="mushroom" or object1[1]=="koopa shell": #always subtracting Mario's original position
                if object1[0][1]>600: #checks if the object needs to be deleted
                    del object1
                    break
                siderect=Rect(object1[0][0]-5,object1[0][1],5,object1[0][3]) #at the right
                siderect2=Rect(object1[0][0]+object1[0][2],object1[0][1],5,object1[0][3]) #left...?

                
                State=Statecheck(object1[0],siderect,siderect2) #Create a SPEED VARIABLE that way if the mushroom hits a wall if will "bounce off"
      
                if State=="Bounce":
                    object1[2]=object1[2]*-1 #reverse velocity
                    State="Moving" #then make it move
               
                if State=="Moving":
                    if Jumpflag==True:
                        object1[0][0]=object1[0][0]+object1[2]
                    else:
                        object1[0][0]=object1[0][0]+object1[2]
                if State=="Falling":
                    object1[0][1]=object1[0][1]+7 #CHECK IF THE OBSTACLE IS ACTUALLY ON SCREEN
                if not object1[0][0]-mario_pos<0 and not object1[0][0]-mario_pos+object1[0][2]>600:
                    screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))

def flower(px,py,x,y,mx,my,deltax,pos):
    global Obstaclevariable
    Obstacles[Obstaclevariable][0]=Rect(px,py,32,32) #parameters for flower, so that it looks good 
    Obstacles[Obstaclevariable][1]="flower"
    drawFullscene(screen,x,y,mx,my,deltax)
    Obstaclevariable+=1
  #  screen.blit(flowerpic,Obstacles[pos][0])


def mushroom(px,py,x,y,mx,my,deltax,pos): #pos represents the place in the Obstacle list that it will be 
    #global mushroompic
    global Obstaclevariable
    drawFullscene(screen,x,y,mx,my,deltax)
    screen.blit(mushroompic,(px,py-32))
    Obstacles[Obstaclevariable][0]=Rect(px,py-30,32,32)
    Obstacles[Obstaclevariable][1]="mushroom"
    Obstacles[Obstaclevariable][2]=3 #this is the speed
    Obstaclevariable+=1
   # display.flip()
   # time.wait(3000)

def blockevents(name,px,py,x,y,mx,my,deltax,pos):
   # if name=="invisible": #...make a block invisible, then if it collides we just change the variable 
    #    print "ok"
    if name=="coin":
        Obstacles[i]
    if name=="mushroom":
       # print "okay"
        mushroom(px,py,x,y,mx,my,deltax,pos)
    if name=="flower":
        flower(px,py,x,y,mx,my,deltax,pos)

        


def Deathcheck(x,y,mx,my,mario_size): #checks if mario is dead yet
    global State
    global LIVES

#    print 'ok'
    LIVES-=1 # lowers life 
    if LIVES==0:
        quit()
    reset() #rests platforms/enemies
   # changemusic(Musicdictionary["Game Over"],4) #
    x=300 # sets stuff back to default
    y=500 #if you make it too high he'll just like die and stuff
    mx=-100
    my=0
    mario_size="small" #changes mario size 
    State="Falling" #make him falling 
    return x,y,mx,my,mario_size
    

def movementcheck(State,Facing,RUNNING_SPEED,WALKING_SPEED): #checks to see if mario is running or colliding with an obstacle 

    if key.get_pressed()[K_LSHIFT]==True:
        horizontal_movement=7
        speed=RUNNING_SPEED
    else:
        horizontal_movement=4
        speed=WALKING_SPEED
    return horizontal_movement,speed

def drawFullscene(screen,x,y,mx,my,deltax): #draws the full scene, returns what it looks like
    drawScene(screen,mx,my,background6,False)
    Drawplatforms(screen,deltax,platforms,x,y)
    drawPresets(x,y)
    drawObstacles(False,x,y,mx,my,deltax) #mushrooms and stuff
    movefireball(-3,-.6,x)
    movedynamic_enemies(x,y)
    move_dynamicprojectiles(x,y)
    drawrotodisk(x,y)
    #drawMenu() #take this out when testing, other it causes it to freeze like everyother time 
    return screen.copy() #trying to return the list for roto disks too
    

def drawScene(screen,x,y,back,flipflag): #controls the screen moving, left or right, maybe some problems moving back..?
    if flipflag==True:
        screen.blit(transform.flip(back,True,False),(x,y))
    if flipflag==False:
        screen.blit(back,(x,y))



def changemusic(name,repeating): #changes the music 
    current_music=mixer.music.load( name )
    mixer.music.play(repeating,0)

def standingCheck(jumpflag,x,y,mx,my,deltax): #YOU DON'T NEED TO PASS IN PLATFORMLISTTT
    global mario_size


    
    global State #having a top and bottom RECT makes it more accurate, won't "glitch" through platforms and such
    #global y
    
   # someflag=False
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer":
        mario_rect=Rect(x,y-34,40,64)
        bottom=Rect(x,y+34,34,4) # its 400 because that will always be his position
        top=Rect(x,y-34,34,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(x+35,y-34,5,60)
        left_side=Rect(x-5,y-34,5,60) #SHORTENED THISSS
        size=35 #makes it look like he is standing on the floor...does it really? =S dont get it 

    if mario_size=="small":
        mario_rect=Rect(x,y,34,34)
        bottom=Rect(x,y+34,34,4) # its 400 because that will always be his position
        top=Rect(x,y,34,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(x+35,y,5,30)
        left_side=Rect(x-5,y,5,30) #SHORTENED THISSS
        size=35 




    if State=="Falling" and jumpflag!=True: #if hes's just falling we only want to see if he collides w/ a platform not hte bounce states


        if bottom.collidelist(platforms)!=-1: 

            pos=bottom.collidelist(platforms)

            State="Standing" #THIS SOMEWHAT WORKS....BUT MESSES UP SIDE collisions


            if y+size<platforms[pos][1]+10: #this means that he fell from above os its okay
                y=platforms[pos][1]-size #if he's standing we want him to be at the same y coordinate as the platform
            else: # else he's falling from the side so he just has to fall down 
                State="Falling"


    
        else:
            State="Falling"


    elif jumpflag==True: #if he's jumping we always see if he can stop first
        
        if bottom.collidelist(platforms)!=-1: #CHANGED THIS TO MARIO RECT, MAYBE USING MARIO RECT IS MORE USEFUL - TRY IT!
            pos=bottom.collidelist(platforms)
            y=platforms[pos][1]-size #if he's standing we want him to be at the same y coordinate as the platform
            State="Standing" #THIS SOMEWHAT WORKS....BUT MESSES UP SIDE collisions

           #CHANGED THIS... 
        elif top.collidelist(platforms)!=-1: # this means that he hit the underside of the platform
            State="Bounce"
            if bothplatforms[top.collidelist(platforms)][1]=="question block" or bothplatforms[top.collidelist(platforms)][1]=="invisible": # if it was a question block we set to an empty block
                bothplatforms[top.collidelist(platforms)][1]="empty block"
                blockevents( bothplatforms[top.collidelist(platforms)][2],bothplatforms[top.collidelist(platforms)][0][0],bothplatforms[top.collidelist(platforms)][0][1]-32,x,y,mx,my,deltax,top.collidelist(platforms))
  

        elif right_side.collidelist(platforms)!=-1: 
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side
        elif bottom.collidelist(top_plats)==-1: #change to mario_rect?
            State="Falling"




    else: #else we always check for collissions first



        if right_side.collidelist(platforms)!=-1:
            State="Bounce3"
        elif left_side.collidelist(platforms)!=-1:
            State="Bounce2" #indiciates a collision at the side 
        elif len(bottom.collidelistall(platforms))>=1:

            State="Standing"
            list1=bottom.collidelistall(platforms)
            pos=list1[0]
            if bothplatforms[pos][3]==True and abs(bothplatforms[pos][5])>0: #if on a moving left/right platform
                
               mx+=bothplatforms[pos][5]*-1 #times by -1 to reverse background
               
             
               x+=bothplatforms[pos][5]
               
            if len(list1)>1: #can only really collide with 2
                
                if bothplatforms[list1[0]][3]==True: #if its moving up...then we want to collide w/ the moving one 
                    
                    if bothplatforms[list1[0]][4]<0:
                        pos=list1[0]
                    else:
                        pos=list1[-1]


                elif bothplatforms[list1[-1]][3]==True: #same principal here
                    print 'ok2'
                    if bothplatforms[list1[0]][4]<0:
                        pos=list1[-1]
                    else:
                        pos=list1[0]
                        
                y=platforms[pos][1]-size #if he's standing we want him to be at the same y coordinate as the platform

                         
            else:
                y=platforms[list1[0]][1]-size #if he's standing we want him to be at the same y coordinate as the platform
                #just change it normally
            
     
        elif top.collidelist(platforms)!=-1 and bottom.collidelist(platforms)==-1: # this means that he hit the underside of the platform   
            State="Bounce" #Don't see how this could happen if he was standing...? =S
        elif bottom.collidelist(platforms)==-1:
                State="Falling"

            
            


    return  mx,x,y #return the new value

def makeplatforms(): #makes some platforms  - looks like [Rect,"texture","contains",movefflag,updown/movemen,leftright/movement,accmovement,limit]
    list1=[[Rect(320,100,128,32),"moving platform","none",True,0,3,0,300],[Rect(200,450,32,32),"block 1","none",True,1,0,0,100],[Rect(0,600-32,2000,20),"block 1","none",False,0,0,0],[Rect(800,450,32,500),"question block","mushroom",False,0,0,0],[Rect(900,450,32,32),"question block","mushroom",False,0,0,0],[Rect(1000,450,32,32),"question block","mushroom",False,0,0,0],[Rect(1100,450,32,32),"invisible","flower",False,0,0,0],[Rect(1500,450,32,500),"block 1",False,0,0,0]]#[Rect(300,510,32,22),"trampoline",None] #bottom most layer, 
    barriers=[]
    platforms2=[]
    platforms=[]
    for i in range(0,len(list1)): #platforms at the top...rect for side collisions, MAKE PLATFORMS A BIT BIGGER
        if list1[i][1]!="trampoline": #however, if this is a trampoline we don't want to have a collision at the top
            something4=Rect(list1[i][0][0],list1[i][0][1]-5,list1[i][0][2],32) #top platforms 
            platforms2.append(something4)
    for i in range(0,len(list1)):
        something1=Rect(list1[i][0][0],list1[i][0][1]+list1[i][0][3],list1[i][0][2],5) #appends the bottom most layer
        #something2=Rect(list1[i][0][0],list1[i][0][1],15,list1[i][0][3]) #left layer, the 10 makes it look closer
       # something3=Rect(list1[i][0][0]+list1[i][0][2]-10,list1[i][0][1],5,list1[i][0][3])     #right layer,# right layer
        barriers.append(something1)
    for i in range(len(list1)):
        something3=Rect(list1[i][0][0],list1[i][0][1],list1[i][0][2],list1[i][0][3])
        platforms.append(something3)
    return list1,barriers,platforms2,platforms

def Drawplatforms(screen,deltax,platformlist,x,y): #draws the platforms, DON'T NEED TO PAST IN PLATFORMLIST
    #newlist=filter(lambda x:# possible filtering later, if there are too many platforms
    mario_pos=x-400
    for i in range(len(bothplatforms)): #possibly check if it can be seen first then go through stuff...? might save time
        if bothplatforms[i][3]==True:

            if abs(bothplatforms[i][6])>bothplatforms[i][7]:
                bothplatforms[i][4]*=-1
                bothplatforms[i][5]*=-1
            bothplatforms[i][6]=bothplatforms[i][6]+bothplatforms[i][4]+bothplatforms[i][5]               
            bothplatforms[i][0][1]+=bothplatforms[i][4]
            bothplatforms[i][0][0]+=bothplatforms[i][5] #left/right

            barriers[i][0]+=bothplatforms[i][5]
            barriers[i][1]+=bothplatforms[i][4]

            top_plats[i][0]+=bothplatforms[i][5]
            top_plats[i][1]+=bothplatforms[i][4]

            platforms[i][0]+=bothplatforms[i][5]
            platforms[i][1]+=bothplatforms[i][4]
 
        if bothplatforms[i][1]!="trampoline" and bothplatforms[i][1]!="invisible":
            newplat=Rect(bothplatforms[i][0][0]-mario_pos,bothplatforms[i][0][1],bothplatforms[i][0][2],bothplatforms[i][0][3])

            #this doesn't make sense >>>>need mario pos
            if not newplat[0]>600 and not newplat[0]+newplat[2]<0:
                for p in range(newplat[1],newplat[1]+newplat[3]-1,32):#goes through all y values...
                    for j in range(newplat[0],newplat[0]+newplat[2]-1,32): # then go through and blit the appropirate texture
                        screen.blit(Scenerydictionary[bothplatforms[i][1]],(j,p)) #minus makes it go higher, plus makes it go lower
            


    

def jump(x,y,intial_velocity,delta_x,gravity_change,pictures,boolean,mx,my,oldx,mario_size,fireballcount):  #mario size represents what stage he's in # make intial velocity negative, boolean represents left jump image
    global Facing
    global Invincibleflag
    global Invinciblecounter
    global framecounter
    global TIMER
    global currentframe
    
    gravity=0
    jumpclock=time.Clock()



    bounceflag=False #if he collides once, then he can't do it agian, in order to keep increasing 

  #  event.get()
    #ALWAYS CHECK TO SEE IF HE'S SUPER OR SMALL 
    while True:
        for evnt in event.get(): #checks fore fireballs stuff
            if evnt.type==KEYDOWN:
                if evnt.key==102 and mario_size=="Fire":
                    fireballcount=fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount)

        framecounter+=1 #increase counter

        if framecounter%60==0: #controls time
            TIMER-=1 


        if framecounter%DELAY==0: #delay to make it look like he's walking
            currentframe+=1 #advaance frame
        
        if currentframe==3: #sets frame to zero, so it can't go over 
            currentframe=0
        
        if Invincibleflag==True:
            Invinciblecounter+=1
        if Invinciblecounter>=100:
            Invincibleflag=False

        if key.get_pressed()[K_RIGHT]==True: #ABILITY TO TURN AROUND IN THE AI
            delta_x+=.07
            boolean=False
            Facing="Right"
        if key.get_pressed()[K_LEFT]==True:
            delta_x-=.07
            boolean=True
            Facing="Left"
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase

       
        y+=change #change the  y
        x+=delta_x #change the x

        mx=mx-delta_x
        pictures=pictureCheck(mario_size,"Jumping Right")
        mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,boolean,mx,my,delta_x,mario_size) #draw mario, use the delta_x to indiciate the change
        mx,x,y=standingCheck(True,x,y,mx,my,deltax) #PROBLEMS WITH THIS AND SUPER MARIO..CAN GLITCH THROUGH PLATFORMS

        if y>600:   
            x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)
            return mx,my,x,y,mario_size


        if State=="Standing":
            pictures=pictureCheck(mario_size,"Standing")
            return mx,my,x,y,mario_size

        if State=="Bounce": # if he hit the underside then we just jump again but this time with a downwards velocity 
            #y+=7
            #call block events here
            pictures=pictureCheck(mario_size,"Jumping Right")
            return jump(x,y,3,delta_x,.4,pictures,boolean,mx,my,oldx,mario_size,fireballcount) #GRAVITY STAYS THE SAME REVERSE VELOCITY
        
        elif State=="Bounce2"  and bounceflag==False: #sides collisions
            if change<0:
                intial_velocity=intial_velocity-1 #move up a bit 
                delta_x=0            #pictures=pictureCheck(mario_size,"Standing")
                bounceflag=True
            else:
                delta_x=0

        elif State=="Bounce3" and bounceflag==False:
            if change<0:
                intial_velocity=intial_velocity-1
                delta_x=0            #pictures=pictureCheck(mario_size,"Standing")
                bounceflag=True 
            else:
                delta_x=0
    
        jumpclock.tick(60)
       # print (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax,mario_size): #draws mario with various animations
    global currentframe

    if mario_size=="small":
       mario_rect=Rect(x,y,34,34)  #maybe give it a length...each time it changes draws a new one?
       yvariable=0 #have to change this when he is big
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer": #changed this to else
        mario_rect=Rect(x,y-34,40,64)
        yvariable=29 #controls how he collides w/ the platforms...
    mx,my,x,y,mario_size=Interactions(mario_rect,mario_size,y,x,deltax,leftflag,mx,my,oldx) #this may change the screen so we check 
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first

        
    pic=pic_list[currentframe]
    
    if leftflag==True: #flips the image if its on the left side 
        pic=transform.flip(pic,True,False)
    
    screen.blit(updated_screen,(0,0)) #blits the updated screen
    
    if Invincibleflag==True: #this makes it look like he's flicking once he's been hit
        if currentframe%2==0:
            screen.blit(pic,Rect(400,y-yvariable,34,34)) #blits mario

    if Invincibleflag==False:
        screen.blit(pic,Rect(400,y-yvariable,34,34)) #blits mario
    

    display.flip()
 
    screen.fill(black)

    return mx,my,x,y,mario_size


def fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount):

                 if fireballcount<=2:
                     if Facing=="Right": #sees which way it should move 
                         fireball_list[fireballcount][1]=7 #velocity 
                         fireball_list[fireballcount][0]=Rect(x+38,y,16,16) #rectangle
                         fireball_list[fireballcount][2]=0 #acc gravity 
                         drawMario(screen,x,y,throwanimation,False,mx,my,deltax,mario_size) #delay to make it look like he's throwing
                         time.wait(100) #delay makes it look like he has that "Throw animation"
                     else:
                        fireball_list[fireballcount][1]=-7
                        fireball_list[fireballcount][0]=Rect(x,y,16,16)
                        fireball_list[fireballcount][2]=0
                        drawMario(screen,x,y,throwanimation,True,mx,my,deltax,mario_size)
                        time.wait(100)
                     fireballcount+=1
                 return fireballcount


def polarToXY(dist, ang, offx,offy):
    x= dist*cos(radians(ang))+offx
    y= dist*sin(radians(ang))+offy
    return x,y

def makerotodisk(positionx,positiony,length): #makes a rotodisk w/ the given parameters
    global rotodiskvariable
    Rotodisk_list[rotodiskvariable][0]=positionx #makes a list as long asyou want 
    Rotodisk_list[rotodiskvariable][1]=positiony
    Rotodisk_list[rotodiskvariable][2]=[]
    for i in range(0,20*length,20): #but this will have to change...?
        Rotodisk_list[rotodiskvariable][2].append([i,0])
 #   Rotodisk_list[rotodiskvariable][3]=length
    rotodiskvariable+=1


def drawrotodisk(x,y):
    global roto_rects
    mario_pos=x-400
    roto_rects=[] #need to clear the list everytime, or else you will collide w/ everything
    rec_list=[]
    for i in range(len(Rotodisk_list)): #draws all teh rects and stuff and returns the list
        if Rotodisk_list[i][0]>0: 
            for fire in Rotodisk_list[i][2]:
                fire[1]=fire[1]+3 % 360 #increase angle
                x,y=polarToXY(fire[0],fire[1],Rotodisk_list[i][0],Rotodisk_list[i][1]) #get x,y coordinate
                rec=Rect(x,y,10,10) #mjake a rect
                roto_rects.append(rec) #draw it 
                if not rec[0]+rec[2]-mario_pos>600 and not rec[0]-mario_pos<0:
                    screen.blit(fireballpic,(rec[0]-mario_pos,rec[1])) #blit it w/ fireball
                
                    
                
        


######################################

#Rotodisk stuff

    #[[disk positionx,disk posotiony,[list of dist/angs]],disk postion2,[list of dist/angs]],

#return disk_position[0]+x
#return disk_position[1]+y

Rotodisk_list=twodimvalue(10,4,None)

roto_rects=[]
#print Rotodisk_list

rotodiskvariable=0 #where to put it in the list


makerotodisk(100,400,10)
makerotodisk(1000,500,10)

#print Rotodisk_list
    

#Rotodisk_list=makerotodisk(position,length)



###################################################


Dynamic_Projectiles=twodim(10,6) #looks like [rect,accgravity,intial_v,horizontalmovement]
for i in range(len(Dynamic_Projectiles)):
    for j in range(5):
        Dynamic_Projectiles[i][j]=None



############################################

choice=0

Projectiles=twodim(10,2) #make them none
projectilevariable=0
for i in range(len(Projectiles)):
    for j in range(2):
        Projectiles[i][j]=None
#Projectiles[0][0]=Rect(300,450,32,32)        
#Projectiles[0][1]=-2
                




###############

Invincible_flag=False # we're going to make it count down through the loop if this is true
Invinciblecount=30 # keep counting EVEN when he's jumping, because that does something in its own right
# set invincible_flag to true
# count down
# then set it to back to false when its done


#####################

coincount=0    

##############################
Jumpflag=False

############

fireball_list=[[None,None,None],[None,None,None],[None,None,None]] #looks like [Rect,direction,acc gravity]
fireballcount=0



###################333

# limit (accumulated,limit)
#last thing represents limit


#make a function that can set paramets for the limit...add and subtract by itself

DEFAULT_ENEMIES=[["kuribos goomba",Rect(450,300,54,78),5,(54,78),-15,1.5,0,"alive",False,False,3,5,301,1,"parabolic",True,0,10000,True,0]]

Dynamic_Enemies=twodimcopy(DEFAULT_ENEMIES)


#maybe make like very fast, fast, med, slow,v ery slow...assign values..then you could just use that instead of numbers?

#looks like [name,rect,speed,dimensions,jump height,horizontal jump movement,acc gravity,state,jumpflag,reverseflag
# jumpfrequency,walkfrequency,shootfrequency,counter,projectiletype,reverseflag,accmovement,limit,jump_invulnerability,fire_invulnerability]

#stright projectile, parabolic one 
#have variables for what the projectile created will be


Koopashellspeed=10

#["koopa",Rect(450,300,32,48),2,(32,48),False,"alive",500,450]



##########
Obstacles=twodim(10,3) # looks like Rectangle,item,velocity

DEFAULT_OBSTACLES=twodimcopy(Obstacles)


Presets=twodim(5,3)


Obstaclevariable=0 #THIS CONTROLS WHAT POSITION EACH THING IS BEING PLACEDIN
#YOU CAN GET MORE THINGS IN OBSTACLES IF YOU WANT JUST REMEMBER TO INCREASE THE VARIABLE

#IMPORTANT: TO ME OBSTACLES ARE DEFINED AS THINGS THAT CAN COME OUT OF "NO WHERE" IN THE GAME, AND DO NOT HAVE PRESET POSITIONS
#THAT MOVE


##########################################


Presets[0][0]=Rect(300,450,32,32)
Presets[0][1]="coin" #perhaps make this a different list, because it takes up the platforms, things might get confusing =\
#Presets[1][0]=Rect(300,500,32,32)
#Presets[1][1]="trampoline"

Presets[1][0]=Rect(1000,randint(1,600),54,48)
Presets[1][1]="bullet bill"

Presets[2][0]=Presets[1][0]=Rect(1000,randint(1,600),54,48)
Presets[2][1]="bullet bill"

DEFAULT_PRESETS=twodimcopy(Presets)




###########################################
leftflag=False  
changemusic(Musicdictionary["SMB3 Theme"],4)


speed=10
gravityforce=.4

############################
#jumpingheight=-10
RUNNING_SPEED=10
WALKING_SPEED=5
horizontal_movement=4
deltax=2
mario_size="Hammer"

bothplatforms,barriers,top_plats,platforms=makeplatforms() #both platforms contains both the rect and the texture in a 2d list 

DEFAULT_PLATFORMS=twodimcopy(bothplatforms)
DEFAULT_BARRIERS=twodimcopy(barriers)
DEFAULT_TOP_PLATS=twodimcopy(top_plats)
DEFAULT_PLATFORMSNORM=twodimcopy(platforms)

flipvariable=False

Facing="Right"

oldx=2
mx=-100 #make screen movement schronized with mario 
my=0

x=400
y=400


intial_force=5
mario_gravity=0
##########################

#Counters and stuff

framecounter=0 #if divisible by some number then advance the frame possibly?
currentframe=0


Invincibleflag=False
Invinciblecounter=0

DELAY=5



###############

LIVES=5
TIMER=300
################################################
running=True
State="Falling"
#Facing="Right"
myClock=time.Clock()
while running:

    drawFlag=False

    if key.get_pressed()[27]==True:
        quit()

    if abs(horizontal_movement)>4: #to make it look like he's moving faster when he's running...and stuff
        DELAY=3
    if abs(horizontal_movement)<=4:
        DELAY=5


    if framecounter%60==0: #controls time, every 60 frames is a second so it make sense, that it goes down by seconds, since the FPS is 60
        TIMER-=1 

    if framecounter%DELAY==0: #delay to make it look like he's walking
        currentframe+=1 #advaance frame
        
    if currentframe==3:
        currentframe=0
    framecounter+=1 #counter that keeps track of frames

    if framecounter>=360:
        framecounter=0

    if Invincibleflag==True: #keeps track of if he can be killed or not
        Invinciblecounter+=1 #increases
    if Invinciblecounter>=100: #if 100 he can be killed again
        Invincibleflag=False

    
    if Facing=="Right": #make a function, this determines the facing
        leftflag=False
    if Facing=="Left":
        leftflag=True

    horizontal_movement,speed=movementcheck(State,Facing,RUNNING_SPEED,WALKING_SPEED)

    if y>600: #if he fell below the level, lolol

        x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)


    #PUT ALL THIS INTO A FUNCTION
    if State=="Falling": #increase gravity... #theres your automatic jumping...are you happy now?, just change variables now, and its easy
        #for evnt in event.get():
            #if key.get_pressed()[K_RIGHT]==True: #allows him to kind of move when falling
                #print "Ok"
               # x+=2
              #  mx=mx-.5
             #   Facing="Right"
            #elif key.get_pressed()[K_LEFT]==True:
                #x=x-.5
                #mx+=.5
                #Facing="Left"
        mario_gravity+=.4
        gforce=intial_force+mario_gravity
      #  x+=2 #make this variable
        y+=gforce
       # mx=mx-2
        pictures=pictureCheck(mario_size,"Standing")
            


    mx,x,y=standingCheck(platforms,x,y,mx,my,deltax) #only need to do this once, PERHAPS, TRY EXPERIMENTING W/ THIS


    
    if State=="Bounce3" or State=="Bounce2": # set mmovement to zero if he is colliding with a wall 
        horizontal_movement=0

        
    if State!="Falling": #gravity goes to 0 
        mario_gravity=0
        
    
    if State=="Standing" or State=="Bounce2" or State=="Bounce3": #Bounce2 and Bounce3 are collision states


        for evnt in event.get():

    
            if evnt.type==KEYDOWN:

                if evnt.key==102 and mario_size=="Fire": #checks if he can throw fireballs

                    fireballcount=fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount)
            
                if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True:
                   # changemusic(0,1)  #ask sir about this
                       drawFlag=True


                       Facing="Right"
                       pictures=pictureCheck(mario_size,"Jumping Right")
                      # State="Falling"
                       mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement,gravityforce,pictures,False,mx,my,deltax,mario_size,fireballcount) #boolen is for left flag
                       
                elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
                        drawFlag=True
                        Facing="Left"
                        pictures=pictureCheck(mario_size,"Jumping Left")
                        mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement*(-1),gravityforce,pictures,True,mx,my,deltax,mario_size,fireballcount)
                        
                elif key.get_pressed()[K_SPACE]==True:# jumping straight up
                   # changemusic(0,1)
                    drawFlag=True                   
                    Facing=Facing #special case...where we check the facing to see how he jumps
                    if Facing=="Right": #CHANGET HIS BECAUSE HE CAN JUMP THROUGH PLATFORMSSS
                        leftflag=False
                        movement=1 #works because its positive/negative
                        standingCheck(platforms,x+5,y,mx,my,deltax)
                        #print State
                        if State=="Bounce3":
                            movement=0
                        pictures=pictureCheck(mario_size,"Neutral Jumping")
                        mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size,fireballcount)
                    elif Facing=="Left": #elif so he can't jump twice
                        drawFlag=True     
                        leftflag=True
                        movement=-1
                        standingCheck(platforms,x-5,y,mx,my,deltax)
                        if State=="Bounce2":
                            movement=0
                        pictures=pictureCheck(mario_size,"Neutral Jumping")
                        mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size,fireballcount)
                       # print "returned"
                
        if key.get_pressed()[K_RIGHT]==True: #and key.get_pressed()[K_LSHIFT]==True:
            drawFlag=True     
            Facing="Right"
            standingCheck(platforms,x+speed/2,y,mx,my,deltax) #MAKE THIS NON GLOBAL
            if State=="Bounce3": #if he would collide, then we speed to zero because that can'
                speed=0
            x+=speed
            mx=mx-speed
            deltax=x-oldx
            pictures=pictureCheck(mario_size,"Moving Right")
          #  pictures=running_list
            mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,False,mx,my,deltax,mario_size) #for run animation

        elif key.get_pressed()[K_LEFT]==True:
            drawFlag=True     
            Facing="Left"
            standingCheck(platforms,x-speed/2,y,mx,my,deltax)
            if State=="Bounce2": #if he would collide we set his sppeed to zero cause he can't, but he can move hte other way
                speed=0
            x=x-speed
            mx=mx+speed
            deltax=x-oldx
            pictures=pictureCheck(mario_size,"Moving Left")
            mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,True,mx,my,deltax,mario_size) #for run animation
        

    if drawFlag==False: #if nothign to drawn then we have to just draw it anyways, so it won't look like you can't see him or w/e
        pictures=pictureCheck(mario_size,"Standing")
        mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,leftflag,mx,my,0,mario_size)


    oldx=x
    oldy=y


    
            
    myClock.tick(60)
    

    
