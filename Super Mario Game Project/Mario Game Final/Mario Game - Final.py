
#########Mario Project - Final Version ##################


#By Moose =D


###GLITCHES#####

#mario jumping through platforms becuase of the bounce state
#mario falling through platforms sometime...shoudl be using similar triangesl to check graivty but I'm not so he'll miss

#sometimes stuck in platforms...if colldide at hte right angle

#if you bounce off a plaform the tope you'll just go through something else...though I never made a level like htis b/c of this reason
#and I didn't have enough time to fix it

#sometimes gravity is too much and he'll fall into the platform if jumping from a really great height 

####################################


 #setup stuff 
from pygame import*
from random import*
from colours import *
from math import *
from glob import *
import cPickle
import os

init()
size=width,height=600,600
screen=display.set_mode(size)



font_type=font.SysFont("Times New Roman",40) #gets the Times New Roman Font


#my_screen=Rect(0,0,600,600)
#screen.set_clip(my_screen)
############################################


#load music stuff 
mixer.init()


Musicdictionary={}

Musicdictionary["Game Over"]="Game Over.OGG"
Musicdictionary["Jump Sound"]="Jump.wav"
Musicdictionary["Game Over.OGG"]="Game Over.OGG"
Musicdictionary["Basic Theme"]="World 1.OGG"
Musicdictionary["SMB3 Theme"]="sm3wd3.mid"
Musicdictionary['Power Up']="Power Up.wav"
Musicdictionary['Fireball']="Fireball.wav"
Musicdictionary['Coin']="Coin.wav"
Musicdictionary['1 up sound']="1 up.wav"
Musicdictionary['Power Down']='Power Down.wav'
Musicdictionary['super mario world level 1']="smwwd1.mid"
Musicdictionary['underwater']="sm3undw.mid"
Musicdictionary['smb3 overworld']="sm3ow2.mid"
Musicdictionary['ocean']="ocean.MID"
Musicdictionary['desert']='desert.MID'
Musicdictionary['grass']='grass.MID'
Musicdictionary['fortress']='fortress.MID'
Musicdictionary['jazz guitar']="marioworldjazzguitar.MID"
Musicdictionary['level-2']='level-2.MID'
Musicdictionary['mario world level 1']='smw_level_1.MID'
Musicdictionary['mario intro']='smwintro.MID'
Musicdictionary['world one']='smwwd1.MID'
Musicdictionary['world two']='smwwd2.MID'


overworld_music=mixer.Channel(1) #channel for overworld music
sounds=mixer.Channel(2) #channel for sounds
jumpsounds=mixer.Channel(3) #channel for jump sounds...since jumping is so frequent it has its own channel 



###############################################




mario1=image.load("Mario Run 1.png") #images of mario 
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


Enemiesdictionary={} #dictionary of enemey images 


Enemiesdictionary['goomba']=image.load("goomba 1 copy copy.PNG"),image.load("goomba 2 copy.PNG"),image.load("goomba 1 copy copy.PNG"),image.load("goomba 2 copy.PNG")

Enemiesdictionary['koopa']=image.load("green koopa 1 copy.PNG"),image.load("green koopa 2 copy.PNG"),image.load("green koopa 1 copy.PNG"),image.load("green koopa 2 copy.PNG")


Enemiesdictionary['fast koopa']=image.load("green koopa 1 copy.PNG"),image.load("green koopa 2 copy.PNG"),image.load("green koopa 1 copy.PNG"),image.load("green koopa 2 copy.PNG")

Enemiesdictionary['flying koopa green']=image.load("flying green koopa 1 copy.PNG"),image.load("flying green koopa 2 copy.PNG"),image.load("flying green koopa 1 copy.PNG"),image.load("flying green koopa 2 copy.PNG")
Enemiesdictionary['red koopa']=image.load("red koopa 1 copy.PNG"),image.load("red koopa 2 copy.PNG"),image.load("red koopa 1 copy.PNG"),image.load("red koopa 2 copy.PNG")

Enemiesdictionary['hammer bros']=image.load("Hammer Brother.GIF"),image.load("Hammer Brother - Throw1.GIF"),image.load("Hammer Brother - Throw2.GIF")

Enemiesdictionary['birdo']=image.load("silver_birdo_sheet93.PNG"),image.load("silver_birdo_sheet93.PNG"),image.load("silver_birdo_sheet93.PNG"),image.load("silver_birdo_sheet93.PNG")

Enemiesdictionary['bowser']=image.load("sm-bowser.GIF"),image.load("sm-bowser.GIF"),image.load("sm-bowser.GIF"),image.load("sm-bowser.GIF")


Enemiesdictionary['dry bones']=image.load("um-drybones.GIF"),image.load("um-drybones.GIF"),image.load("um-drybones.GIF"),image.load("um-drybones.GIF")

Enemiesdictionary['buzzy beetle']=image.load("buzzy beetle 1 copy.PNG"),image.load("buzzy beetle 2 copy.PNG"),image.load("buzzy beetle 1 copy.PNG"),image.load("buzzy beetle 2 copy.PNG")

Enemiesdictionary['cheep cheep']=image.load("cheep cheep 1 copy.PNG"),image.load("cheep cheep 2 copy.PNG"),image.load("cheep cheep 1 copy.PNG"),image.load("cheep cheep 2 copy.PNG")

Enemiesdictionary['lakitu']=image.load("Lakitu1.GIF"),image.load("Lakitu1.GIF"),image.load("Lakitu1.GIF"),image.load("Lakitu1.GIF")

Enemiesdictionary['piranha plant']=image.load("piranha 1 copy.PNG"),image.load("piranha 2 copy.PNG"),image.load("piranha 1 copy.PNG"),image.load("piranha 2 copy.PNG")

Enemiesdictionary['podoboo']=image.load("Podoboo.GIF"),image.load("Podoboo.GIF"),image.load("Podoboo.GIF"),image.load("Podoboo.GIF")

Enemiesdictionary['kuribos goomba']=image.load("um-kuribosgoomba.GIF"),image.load("um-kuribosgoomba.GIF"),image.load("um-kuribosgoomba.GIF"),image.load("um-kuribosgoomba.GIF")

Enemiesdictionary['spark']=image.load("mw-spark.GIF"),image.load("mw-spark.GIF"),image.load("mw-spark.GIF"),image.load("mw-spark.GIF")

Enemiesdictionary['snifit']=image.load("mw-snifit.GIF"),image.load("mw-snifit.GIF"),image.load("mw-snifit.GIF"),image.load("mw-snifit.GIF")

Enemiesdictionary['cobrat']=image.load("mw-cobrat.GIF"),image.load("mw-cobrat.GIF"),image.load("mw-cobrat.GIF"),image.load("mw-cobrat.GIF")

Enemiesdictionary['spiny thing']=image.load("spiny 1 copy.PNG"),image.load("spiny 2 copy.PNG"),image.load("spiny 1 copy.PNG"),image.load("spiny 2 copy.PNG")

Enemiesdictionary['red koopa flying']=image.load("red koopa flying 1 copy.PNG"),image.load("red koopa flying 2 copy.PNG"),image.load("red koopa flying 1 copy.PNG"),image.load("red koopa flying 2 copy.PNG")




###############################################

image.load("Block World 1.PNG") #dictionary of textures 

Scenerylist=[(image.load("Block World 1.PNG")),(image.load("Grass Middle.PNG")),(image.load("Cloud.PNG")),(image.load("Question Block 1.PNG"))]


Scenerydictionary={}
Scenerydictionary["block 1"]=image.load("Block World 1.PNG"),32,32
Scenerydictionary["grass"]=image.load("Grass Middle.PNG"),32,32
Scenerydictionary["cloud"]=image.load("Cloud.PNG"),32,32
Scenerydictionary["question block"]=image.load("Question Block 1.PNG"),32,32
Scenerydictionary["empty block"]=image.load("Empty Block.PNG"),32,32
Scenerydictionary['moving platform']=image.load("Moving Platform1.GIF"),48,16
Scenerydictionary['lava']=image.load("Lava.PNG"),32,32
Scenerydictionary['pipe']=image.load("Pipe.GIF"),64,64
Scenerydictionary['pipe middle']=image.load("Pipe Middle.PNG"),64,32 #make transparent
Scenerydictionary['pipe top']=image.load("Pipe Top.PNG"),64,32
Scenerydictionary['brick 1']=image.load("Brick World 1.PNG"),32,32
Scenerydictionary['brick 2']=image.load("Brick World 2.PNG"),32,32
Scenerydictionary['brick 3']=image.load("Brick World 3.PNG"),32,32
Scenerydictionary['brick 4']=image.load("Brick World 4.PNG"),32,32
Scenerydictionary['ground 1']=image.load("Ground World 1.PNG"),32,32
Scenerydictionary['ground 2']=image.load("Ground World 2.PNG"),32,32
Scenerydictionary['ground 3']=image.load("Ground World 3.PNG"),32,32
Scenerydictionary['ground 4']=image.load("Ground World 4.PNG"),32,32
Scenerydictionary['moving platform 2']=image.load("Moving Platform2.GIF"),64,16
Scenerydictionary['moving platform 3']=image.load("Moving Platform3.GIF"),96,16
Scenerydictionary['trampoline']=image.load("trampoline2.GIF"),32,32
Scenerydictionary['mushroom platform']=image.load("Giant Mushroom.GIF"),96,128
#################################################


Background_dictionary={} #textures of backgrounds 


Background_dictionary['sky']=image.load("Sky.bmp").convert()
Background_dictionary['sky2']=image.load("mario.jpg").convert()
Background_dictionary['underwater']=image.load("underwater.jpg").convert()
Background_dictionary['cloud background']=image.load("cloud background.jpg").convert()
Background_dictionary['forest']=image.load("laura's background fixed.png").convert()
Background_dictionary['sunset']=image.load("bg.PNG").convert()
Background_dictionary['forest night']=image.load("yee fan thing.JPG").convert()
Background_dictionary['desert']=image.load('desert(1).JPG').convert()
Background_dictionary['darkness']=image.load("darkness.BMP").convert()

##############################33

#Beanstalk and obstacles stuff

Obstaclesdictionary={} #dictionary of obstacles 

Obstaclesdictionary['flower']=image.load('fire flower 1 copy.png'),image.load('fire flower 2 copy.png'),image.load('fire flower 3 copy.png'),image.load('fire flower 1 copy.png')
Obstaclesdictionary['mushroom']=image.load("Mushroom.png")
Obstaclesdictionary['coin']=image.load("coin 1 copy.PNG"),image.load("coin 2 copy.PNG"),image.load("Coin 3.JPG"),image.load("Coin 4 copy.PNG")
Obstaclesdictionary['koopa shell']=image.load("Green Shell.png")
Obstaclesdictionary['red koopa shell']=image.load("Red Koopa Troopa - Shell1.GIF")
Obstaclesdictionary['buzzy beetle shell']=image.load("Buzzy Beetle - Blue - Shell.GIF")
Obstaclesdictionary['trampoline']=image.load("trampoline.png")
Obstaclesdictionary['bullet bill']=image.load("Bullet Bill - Black.GIF")
Obstaclesdictionary['green mushroom']=image.load("1-Up Mushroom.GIF")
Obstaclesdictionary['hammer']=image.load("um-hammer.GIF") # set this to 32x32
Obstaclesdictionary['small hammer']=image.load("Hammer.GIF")
Obstaclesdictionary['spark']=image.load("mw-spark.GIF")
Obstaclesdictionary['cheep cheep']=image.load("Cheep Cheep - Red.GIF")
Obstaclesdictionary['fireball']=image.load("fireball 1 copy.png"),image.load("fireball 2 copy.png"),image.load("fireball 1 copy.png"),image.load("fireball 2 copy.png")
Obstaclesdictionary['flag']=image.load("Flag.PNG"),image.load("Flag.PNG"),image.load("Flag.PNG"),image.load("Flag.PNG")


fireballpic=image.load("Fireball.png")

credits_pic=image.load("credits.PNG")

#########################################################


projectile_hammer=image.load("Hammer.GIF") #other random stuff 

projectile_fireball=image.load("Fireball.GIF")

#####################################################


Otherdictionary={} #dictionary of other stuff 

Otherdictionary['lives icon']=image.load("Lives Icon.PNG")
Otherdictionary['coin']=image.load("Coin 1.png")
Otherdictionary['title screen']=image.load("mario title screen.BMP")
Otherdictionary['level screen']=image.load("level screen.JPG")
Otherdictionary['game over scren']=image.load("gameover.JPG")


#####################################################

def bgm_music(filename): #plays background music...
    #file1=filename+".MID"
    filename=Musicdictionary[filename]
    mixer.music.stop()
    mixer.music.load(filename)
    mixer.music.play(-1,0)

def drawlevel(name): #draws the pre level screen 
    screen.fill(black)
    screen.blit(Otherdictionary['level screen'],(150,150))
    drawMenu()
    Drawtext(name,40,(220,100),white)
    display.flip()
    running2=True  #waits for user to hit something 
    while running2:
        for evnt in event.get():
            if evnt.type==KEYDOWN:
                running2=False
   # time.wait(1500)


def twodimcopy(twodlist): #makes a copy of two dimensional list...

    
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


def deathrestart(): # if they die this ist eh game over screen 
    global LIVES
    global LEVEL
    global WORLD
    global coincount
    mixer.music.stop()
    changemusic("Game Over",sounds)
    screen.blit(Otherdictionary['game over scren'],(0,0))
    display.flip()
    time.wait(2000)
    running2=True
    coincount=0
    while running2: #wait for input 
        for evnt in event.get():
            if evnt.type==KEYDOWN:
                running2=False
    sounds.stop()
    LIVES=5
    LEVEL=1
    name="World"+" "+str(WORLD)+"-"+str(LEVEL)
    loadlevel(name)
    
def reset(): #resets the level 
    global Dynamic_Enemies
    global Presets
    global Dynamic_Projectiles
    global bothplatforms
    global Obstacles
    global Obstaclevariable
    global barriers
    global top_plats
    global platforms
    global x
    global y
    global TIMER
    global selected_music
    #changemusic("Basic Theme",overworld_music) #music back to defualt

    mixer.music.stop()
   # changemusic("Game Over",sounds)
  #  time.wait(5000)
    
    bgm_music(selected_music)

    
    Presets=twodimcopy(DEFAULT_PRESETS) #revert everything to defaults 
    Dynamic_Enemies=twodimcopy(DEFAULT_ENEMIES)
    Dynamic_Projectiles=twodim(10,6)
    bothplatforms=twodimcopy(DEFAULT_PLATFORMS)
    Obstacles=[]
    barriers=twodimcopy(DEFAULT_BARRIERS)
    top_plats=twodimcopy(DEFAULT_TOP_PLATS)
    platforms=twodimcopy(DEFAULT_PLATFORMSNORM)
    Obstaclevariable=0
    TIMER=300

    



def drawMenu(): #draws the menu at the top 
    screen.blit(Otherdictionary['lives icon'],(50,25))
    Drawtext("x"+" "+str(LIVES),40,(80,10),red)
    screen.blit(Otherdictionary['coin'],(240,25))
    Drawtext("x"+" "+str(coincount),40,(270,10),red)
    Drawtext("TIME"+" "*3+str(TIMER),40,(400,10),red)


def Drawtext(words,size,(x,y),colour): #function that gets text size and a position from the user and draws it to the screen

    #SIZE DOESN'T MATTER...CAUSE I CHANGED AROUND THE FUNCTION AND STUFF
    text=font_type.render(words,True,colour) #writes the text
    screen.blit(text,(x,y)) #blits text to the screen

            


def sizeCheck(mario_size):#function which returns mario's stae after he got hit 
 #   global mario_size
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer":
        return "small"
    elif mario_size=="small":
        return "death"

    
def seeCheck(x,y,Rectobject): #check if an object is on screen 
    flag=False
    mario_pos=x-400 
    if not Rectobject[0]+Rectobject[2]-mario_pos<0 and not Rectobject[0]-mario_pos>600:
        flag=True
    return flag
    


def movedynamic_enemies(x,y): #function which moves the enemies 

    global currentenemeyframe
  
    currentframe=currentenemeyframe #controls enemey framne 


    mario_pos=x-400 
    
    for i in range(len(Dynamic_Enemies)):
        Jumpflag=False #indicates if enemey is jumping
        
        name=Dynamic_Enemies[i][0]
        dimensions=Dynamic_Enemies[i][3]
        horizontal_movement=Dynamic_Enemies[i][5]
        intial_v=Dynamic_Enemies[i][6]
        #siderect is right
        #siderect2 is left
        siderect=Rect(Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][3][0],Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)# represents rectangle at the side
        siderect2=Rect(Dynamic_Enemies[i][1][0]-3,Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)
        Dynamic_Enemies[i][1][1],State,jump_height=EnemeyStatecheck(Dynamic_Enemies[i][1],siderect,siderect2,Dynamic_Enemies[i][1][1],Dynamic_Enemies[i][7],Dynamic_Enemies[i][2],Dynamic_Enemies[i][4])

        if Dynamic_Enemies[i][0]=="red koopa": #red koopas can't fall off platforms so if it does then we just reverse and make it turn around
            if State=="Falling":
                if abs(Dynamic_Enemies[i][16])>10: #as longa she's moving, and he's falling he reserves direction 
                  Dynamic_Enemies[i][2]*=-1

                  if Dynamic_Enemies[i][15]==True: #reverse direction he's facing.....
                   Dynamic_Enemies[i][15]=False
                  elif Dynamic_Enemies[i][15]==False:
                    Dynamic_Enemies[i][15]=True
                  Dynamic_Enemies[i][1][0]+=Dynamic_Enemies[i][2]
                  State="Moving"
                


            
        if seeCheck(x,y,Dynamic_Enemies[i][1])==True: #sees if they are onscreen

            if State!="Falling":

                temp_rects=[] 
                for enemey in Dynamic_Enemies: #get all the rects except the rectangle for that enemey
                    if enemey[0]!="podoboo" and enemey!=Dynamic_Enemies[i] and enemey[0]!="piranha":
                        temp_rects.append(enemey[1])
                        
                for obstacle in Obstacles: #if hit by an inactive shell
                    if obstacle[1]=="buzzy beetle shell" or obstacle[1]=="red koopa shell" or obstacle[1]=="koopa shell" and obstacle[2]==0:
                        temp_rects.append(obstacle[0])                   
                
                if Dynamic_Enemies[i][1].collidelist(temp_rects)!=-1: #if he collides w/ one of the other guys then we set to
                    State="Bounce" #bounce so that his velocity is reveresed      



            if Dynamic_Enemies[i][13]==300: #counter that keeps track of what the enemey is doing...jump/walk/shoot
                Dynamic_Enemies[i][13]=0


           
            if Dynamic_Enemies[i][1][1]>600: #death check
                del Dynamic_Enemies[i]
                break


            if Dynamic_Enemies[i][7]=="flying": #if they are flying 

                if abs(Dynamic_Enemies[i][16])>Dynamic_Enemies[i][17]: 
                    Dynamic_Enemies[i][2]*=-1
                    Dynamic_Enemies[i][16]=0
                    if Dynamic_Enemies[i][0]=="podoboo": #only fireballs reverse directions

                        if Dynamic_Enemies[i][15]==True: 
                            Dynamic_Enemies[i][15]=False
                        elif Dynamic_Enemies[i][15]==False:
                            Dynamic_Enemies[i][15]=True



                Dynamic_Enemies[i][1][1]+=Dynamic_Enemies[i][2] #moving + speed 
                Dynamic_Enemies[i][16]+=Dynamic_Enemies[i][2] #acc movement

                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][currentframe]
                
                if Dynamic_Enemies[i][15]==True: #flips it if the direction is reversed

                    pic=transform.flip(pic,False,True) 
                

            if Dynamic_Enemies[i][7]=="alive" or Dynamic_Enemies[i][7]=="jumping": #if they are alive


                
                Dynamic_Enemies[i][9]+=1 #increase shoot counter
                if Dynamic_Enemies[i][9]>=100:
                    Dynamic_Enemies[i][9]=2


                if State=="Falling":
                    Dynamic_Enemies[i][1][1]+=5
                    
                if State=="Bounce" or abs(Dynamic_Enemies[i][16])>Dynamic_Enemies[i][17]: #if hit wall reverse velocity

                        
                         
                        Dynamic_Enemies[i][2]=Dynamic_Enemies[i][2]*-1
                        Dynamic_Enemies[i][5]*=-1



                                


                        if Dynamic_Enemies[i][15]==True: #reverse direction he's facing...upon bounce thing?
                            Dynamic_Enemies[i][15]=False
                        elif Dynamic_Enemies[i][15]==False:
                            Dynamic_Enemies[i][15]=True


                if State=="Moving": #i fhe's moving we set the gravity to zero and increase the counter 
                    Dynamic_Enemies[i][6]=0
                    Dynamic_Enemies[i][8]=False
                    Dynamic_Enemies[i][13]+=1        
                
                

                if Dynamic_Enemies[i][9]%Dynamic_Enemies[i][12]==0: #SHOOTING shoot counter%shoot frequency, can shoot if jumping 
                    constant=1 #depends on what way is he facing 
                    if Dynamic_Enemies[i][2]>0: #makes the projectile go the other way depending on how he is facing
                        constant=-1
                    if Dynamic_Enemies[i][14]=="parabolic":
                        list1=[None,None,None,None,None,None]
                        list1[0]=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],16,32) #changed for hammer
                        list1[1]=0 #acc gravity 
                        list1[2]=randint(-12,-6)  #intial velocity kind of random 
                        list1[3]=-3*constant #movement horizontally, 
                        list1[4]="parabolic"
                        list1[5]=0 #angle representation
                        Dynamic_Projectiles.append(list1) #append to list 
                    if Dynamic_Enemies[i][14]=="straight": #never got a chance to use this...
                        list1=[None,None,None,None,None,None]
                        list1[0]=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],48,16) #rect
                        list1[1]=-5*constant  #movement
                        list1[4]="straight" # type 
                        Dynamic_Projectiles.append(list1)
    
                

                
                if  Dynamic_Enemies[i][13]%Dynamic_Enemies[i][11]==0: # JUMPING, counter%jump frequency

                  
                    change=jump_height+intial_v #jump height has to be negative
                    Dynamic_Enemies[i][6]+=.4 #increase gravity
                    Dynamic_Enemies[i][1][1]+=change #idelta y  
                    Dynamic_Enemies[i][1][0]+=Dynamic_Enemies[i][5] #change x
                    Dynamic_Enemies[i][8]=True #indicates he's jumping
                    Dynamic_Enemies[i][16]+=Dynamic_Enemies[i][5]  #acc movement 
                    Jumpflag=True #didnt need this?

                    
                if Dynamic_Enemies[i][13]%Dynamic_Enemies[i][10]==0 and Jumpflag==False: # walking/moving if he's doing one of the above
                       Dynamic_Enemies[i][1][0]+=Dynamic_Enemies[i][2]
                       Dynamic_Enemies[i][16]+=Dynamic_Enemies[i][2] #moving twice...? so confused

                       
                        
                            


                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][currentframe] #just blit to the current frame
                
                if Dynamic_Enemies[i][15]==True: #flips it if the direction is reversed 
                    pic=transform.flip(pic,True,False) 



            

            if Dynamic_Enemies[i][7]=="dead": #if they are dead 

               
                if Dynamic_Enemies[i][0]=="koopa" or Dynamic_Enemies[i][0]=="flying koopa green": #if its a koopa they turn into a shell
                    list1=[Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],32,32),"koopa shell",0]
                    Obstacles.append(list1)
                    del Dynamic_Enemies[i]
                    break #have to break or else it will keep going and crash
                
                if Dynamic_Enemies[i][0]=="buzzy beetle": #if its a koopa they turn into a shell
                    list1=[Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],32,30),"buzzy beetle shell",0]
                    Obstacles.append(list1)
                    del Dynamic_Enemies[i]
                    break #have to break or else it will keep going and crash
        
                if Dynamic_Enemies[i][0]=="red koopa" or Dynamic_Enemies[i][0]=="red koopa flying":
                    list1=[Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],32,28),"red koopa shell",0]
                    Obstacles.append(list1)
                    del Dynamic_Enemies[i]
                    break #have to break or else it will keep going and crash
                
                     
                else: #else they simply fall
                    pic=Enemiesdictionary[Dynamic_Enemies[i][0]][currentframe]
                    pic=transform.flip(pic,False,True)
                    Dynamic_Enemies[i][1][1]+=3


            if Dynamic_Enemies[i][7]=="fire dead": #same thing basically, excpet hit by fireballa nd can't turn into a shell 
                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][currentframe]
                pic=transform.flip(pic,False,True)
                Dynamic_Enemies[i][1][1]+=3

            #blit to the screen, don't need this, because I already checked if they're onscreen         
          #  if not Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][1][2]-mario_pos<0 and not Dynamic_Enemies[i][1][0]-mario_pos>600: #checks if the enemey can be seen onscreen
            screen.blit(pic,(Dynamic_Enemies[i][1][0]-mario_pos,Dynamic_Enemies[i][1][1])) #if they can be then we draw them


            
    
        

        
    
    

def move_dynamicprojectiles(x,y): #moves projectiles 
    mario_pos=x-400
    for i in range(len(Dynamic_Projectiles)):
        if Dynamic_Projectiles[i][0]!=None:

            pic=projectile_hammer
            
            if Dynamic_Projectiles[i][4]=="straight":  #if its straight you just move it, pretty simple 
                
                pic=projectile_fireball

                if Dynamic_Projectiles[i][1]>0:
                    pic=transform.flip(pic,True,True)

               # pic=projectile_fireball
                Dynamic_Projectiles[i][0][0]+=Dynamic_Projectiles[i][1] #increase speed

            if Dynamic_Projectiles[i][4]=="parabolic":
                
                pic=projectile_hammer
            
                siderect=Rect(Dynamic_Projectiles[i][0][0]-6,Dynamic_Projectiles[i][0][1],6,10) #get sidrect 
                siderect2=Rect(Dynamic_Projectiles[i][0][0]+14,Dynamic_Projectiles[i][0][1],6,10)
                State=Statecheck2(Dynamic_Projectiles[i][0],siderect,siderect2)

                #I honestly have no clue what the state is for...?, probably something from a while ago
                
                change=Dynamic_Projectiles[i][2]+Dynamic_Projectiles[i][1]  #find delta y 
                Dynamic_Projectiles[i][1]+=.4 #increase gravity
                Dynamic_Projectiles[i][0][1]+=change
                Dynamic_Projectiles[i][0][0]+=Dynamic_Projectiles[i][3] #horizontal movement
                Dynamic_Projectiles[i][5]+=5 #angle increase
                if Dynamic_Projectiles[i][5]==360:
                    Dynamic_Projectiles[i][5]=0
                pic=transform.rotate(pic,Dynamic_Projectiles[i][5]) #rotate by angle

                if Dynamic_Projectiles[i][0][1]>600: ##test this 
                    del Dynamic_Projectiles[i]
                    break


            #I should have probably made a wa to delte it                 
            if not Dynamic_Projectiles[i][0][0]+Dynamic_Projectiles[i][0][2]-mario_pos<0 and not Dynamic_Projectiles[i][0][0]-mario_pos>600:

                screen.blit(pic,(Dynamic_Projectiles[i][0][0]-mario_pos,Dynamic_Projectiles[i][0][1]))
            

        
        

        
def movefireball(intial_v,gravity,x): #moves fireballs, 
    global fireballcount
    mario_pos=x-400
    for i in range(len(fireball_list)):
        if fireball_list[i][0]!=None:
            fireball_list[i][2]+=gravity #increase gravity
            change=intial_v-fireball_list[i][2] #calculaet change
            fireball_list[i][0][1]+=change #increase y
            fireball_list[i][0][0]+=fireball_list[i][1]# increase x

            siderect=Rect(fireball_list[i][0][0]-6,fireball_list[i][0][1],6,10) #get rectangle for states 
            siderect2=Rect(fireball_list[i][0][0]+14,fireball_list[i][0][1],6,10)
            
            
                
            State=Statecheck2(fireball_list[i][0],siderect,siderect2) #check the state, for FIREBALLS

            if State=="Moving":
                fireball_list[i][2]=0 # set gravity to zero 
                screen.blit(fireballpic,(fireball_list[i][0][0]-mario_pos,fireball_list[i][0][1])) #OUT OF RANGE ERRORS 
            if State=="Bounce" or fireball_list[i][0][1]>600:
                del fireball_list[i] #delete the old one
                fireball_list.insert(0,[None,None,None]) #insert the new one

                fireballcount=0 # set it back to zero which would be the blank one 
                break
            #onscreen checks?
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


def get_temporary(): #makes a list of all the temporary stuff that we need for f
    
    
    temp_obstacles=[]
    for i in range(len(Obstacles)): #fix THIS, SO THAT ONLY THE ONES THAT CAN BE SEEN GET INCLUDED
        if Obstacles[i][0]!=None:
            temp_obstacles.append(Obstacles[i][0])
        
    temp_presets=[] #get all the preset stuff
    for i in range(len(Presets)):
        if Presets[i][1]=="spark":

            temp_presets.append(Presets[i][7])
        else:
            
            temp_presets.append(Presets[i][0])


    temp_enemies=[]
    temp_enemies_top=[]
    #CHECK IF THEY ARE ONSCREEEEN
    for i in range(len(Dynamic_Enemies)):
        if Dynamic_Enemies[i][7]=="alive" or Dynamic_Enemies[i][7]=="flying": #he can only collide and stuff if he's flying/alive
            temp_enemies.append(Dynamic_Enemies[i][1])
            something=Rect(Dynamic_Enemies[i][1][0],Dynamic_Enemies[i][1][1],Dynamic_Enemies[i][1][2],15)
            temp_enemies_top.append(something)
            

    temp_projectiles=[]
    for i in range(len(Dynamic_Projectiles)):
        if Dynamic_Projectiles[i][0]!=None:
            temp_projectiles.append(Dynamic_Projectiles[i][0])


    temp_hammers=[]
    for i in range(len(my_hammers)):
        if my_hammers[i][0]!=None:
            temp_hammers.append(my_hammers[i][0])

    return temp_obstacles,temp_presets,temp_enemies,temp_projectiles,temp_hammers,temp_enemies_top

def Interactions(Rectobject,mario_size,y,x,deltax,leftflag,mx,my,oldx): #pass in mario_size, if nothing happens then we return it, PASS IN STATE AND FACING LATER
    global State
    global coincount
    global Facing
    global fireballcount
    global Invincibleflag
    global Invinciblecounter
    global LIVES
    global Dynamic_Enemies
    global SPAWNX
    global SPAWNY
    global LEVEL
    global Levelchange
    global WORLD
    global TIMER
    global Deathflag


    collideflag=False
    
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer": #gets basic rects that I need 
        mario_rect=Rect(x,y-34,40,64)
        bottom=Rect(x,y+34,34,4) 


    if mario_size=="small":
        mario_rect=Rect(x,y,34,34)
        bottom=Rect(x,y+34,34,4) 

    temp_obstacles,temp_presets,temp_enemies,temp_projectiles,temp_hammers,temp_enemies_top=get_temporary()


    for i in range(len(temp_obstacles)): #sees if the buzzy beetle shell/koopa shell hit any enemies
        #fix this won't collide
        if Obstacles[i][1]=="koopa shell" or Obstacles[i][1]=="buzzy beetle shell" or Obstacles[i][1]=="red koopa shell": #and abs(Obstacles[i][2])>0:
            if abs(Obstacles[i][2])>0:
                if temp_obstacles[i].collidelist(temp_enemies)!=-1:
                    pos=temp_obstacles[i].collidelist(temp_enemies)
                    Dynamic_Enemies[pos][7]="fire dead" #make his state fire dead so that like...koopas won't turn into shells agian, y'know



    if Rectobject.collidelist(temp_presets)!=-1: #check for pre set collisions, like with teh flag 
        pos=Rectobject.collidelist(temp_presets)
        if Presets[pos][1]=="flag":
            LEVEL+=1 #increase level 
            if LEVEL==5: #can't go past level 4
                WORLD+=1
                LEVEL=1
            name="World"+" "+str(WORLD)+"-"+str(LEVEL)
            if name=="World 4-1":
                mixer.music.stop()
                bgm_music('jazz guitar')
                screen.blit(credits_pic,(-100,0))
                display.flip()
                running3=True
                while running3:
                    for evnt in event.get():
                        if evnt.type==KEYDOWN:
                            running3=False
                quit()
            loadlevel(name) #loads that level 
            x=SPAWNX
            y=SPAWNY
            Levelchange=True
            TIMER=300
            mx=-100-(SPAWNX-400)
            drawlevel(name)


            
        elif Presets[pos][1]=="spark": #collisions w/ the spark 
                if Invincibleflag==False: #basic death thing
                    mario_size=sizeCheck(mario_size)
                    if mario_size=="death":
                        LIVES-=1
                        if LIVES==0:
                            deathrestart()
                        x=SPAWNX
                        y=SPAWNY
                        mx=-100-(SPAWNX-400)
                        my=0
                        mario_size="small"
                        State="Falling"
                        Deathflag=True
                        reset()
                        name="World"+" "+str(WORLD)+"-"+str(LEVEL)
                        drawlevel(name)                        
                    else:
                        Invincibleflag=True
                        Invinciblecounter=0
                        changemusic("Power Down",sounds)
                        
        elif Presets[pos][1]=="cheep cheep": #with cheep cheep....
                if bottom.colliderect(Presets[pos][0])==True and Presets[pos][5]=="alive":
                    Presets[pos][5]='dead'
                    Presets[pos][3]=0
                elif Invincibleflag==False and Presets[pos][5]=="alive": #basic death thing
                    mario_size=sizeCheck(mario_size)
                    if mario_size=="death":
                        LIVES-=1
                        if LIVES==0:
                            deathrestart()
                        x=SPAWNX
                        y=SPAWNY
                        mx=-100-(SPAWNX-400)
                        my=0
                        mario_size="small"
                        State="Falling"
                        Deathflag=True
                        reset()
                        name="World"+" "+str(WORLD)+"-"+str(LEVEL)
                        drawlevel(name)                        
                        
                    else:
                        Invincibleflag=True
                        Invinciblecounter=0
                        changemusic("Power Down",sounds)
                        
        elif Presets[pos][1]=="coin": #check if its a coin
           
           coincount+=5
           if coincount>100: #if its over 100 you get a life 
               LIVES+=1
               changemusic("1 up sound",sounds)
               coincount=coincount%100 #can't go past 100
           del Presets[pos]
           changemusic("Coin",sounds)
        elif Presets[pos][1]=="trampoline":
 
            if bottom.collidelist(temp_presets)!=-1:

                changemusic("Jump Sound",jumpsounds)
                return jump(x,y,-10,deltax,.4,jumplist,False,mx,my,oldx,mario_size,fireballcount) #if he hits it he bounces off
                   
            
        elif Presets[pos][1]=="bullet bill" or Presets[pos][1]=="fireball" and Invincibleflag==False:
                mario_size=sizeCheck(mario_size)
                if mario_size=="death":
                    LIVES-=1
                    if LIVES==0:
                        deathrestart()
                    x=SPAWNX
                    y=SPAWNY
                    mx=-100-(SPAWNX-400)
                    my=0
                    mario_size="small"
                    Deathflag=True
                    State="Falling"
                    reset()
                    name="World"+" "+str(WORLD)+"-"+str(LEVEL)
                    drawlevel(name)                        
                    
                else:
                    Invincibleflag=True
                    Invinciblecounter=0
                    changemusic("Power Down",sounds)

        
    if Rectobject.collidelist(temp_obstacles)!=-1: #checks for temp obstacles collisions 
        pos=Rectobject.collidelist(temp_obstacles)


        if Obstacles[pos][1]=="green mushroom": #gain a life
            del Obstacles[pos]
            LIVES+=1#if green/1 up mushroom
            changemusic("1 up sound",sounds)
            
        elif Obstacles[pos][1]=="flower": #change state 
            #if State=="Standing":
            del Obstacles[pos]
            mario_size="Fire"
            changemusic("Power Up",sounds)

        elif Obstacles[pos][1]=="hammer": #change state 
            del Obstacles[pos]
            mario_size="Hammer"
            changemusic("Power Up",sounds)

        elif Obstacles[pos][1]=="mushroom":
            del Obstacles[pos]
            mario_size="Super"
            changemusic("Power Up",sounds)
            
        elif Obstacles[pos][1]=="koopa shell" or Obstacles[pos][1]=="buzzy beetle shell" or Obstacles[i][1]=="red koopa shell":


            if State=="Falling": #if mario jumped on the shell 
                changemusic("Jump Sound",jumpsounds)
                Obstacles[pos][2]=0 #makes it stop if he jumped on it 
                return jump(x,y,-7,deltax,.4,jumplist,False,mx,my,oldx,mario_size,fireballcount) #if he hits it he bounces off
            elif State=="Standing": #if he hits it when he's running
            #    print Obstacles[pos]
                if Obstacles[pos][2]==0: #and it hasn't been moved yet
                    print 'call'
                    if Facing=="Right": #we make it have some speed
                        Obstacles[pos][2]=Koopashellspeed
                        Obstacles[pos][0][0]+=Koopashellspeed #we have to moev it so it won't collide right away
                    elif Facing=="Left":
                        Obstacles[pos][2]=Koopashellspeed*(-1)
               #     Invincibleflag=True 
                        Obstacles[pos][0][0]+=Koopashellspeed*-1 #we have to moev it so it won't collide right away
                else: #else he's dead 
                    if Invincibleflag==False:
                        mario_size=sizeCheck(mario_size)
                        if mario_size=="death":
                            LIVES-=1
                            if LIVES==0:
                                deathrestart()
                            x=SPAWNX
                            y=SPAWNY
                            mx=-100-(SPAWNX-400)
                            my=0
                            mario_size="small"
                            State="Falling"
                            reset()
                            Deathflag=True
                            name="World"+" "+str(WORLD)+"-"+str(LEVEL)
                            drawlevel(name)                        
                                
                        else:
                            Invincibleflag=True
                            Invinciblecounter=0
                            changemusic("Power Down",sounds)
                                





   # collideflag=False
    if State=="Falling":     #has to be fallikng for him to kill the enemey
        if bottom.collidelist(temp_enemies_top)!=-1: #bottom of him has to collide w/ top of enemey 
            pos=bottom.collidelist(temp_enemies) #if the bottom collides, then the enemey is dead,
            if Dynamic_Enemies[pos][18]==True: #sees if he can be killed by jumping on
                collideflag=True#changed position of this 
                Dynamic_Enemies[pos][7]="dead" #make his state dead
                drawFullscene(screen,x,y,mx,my,deltax)  #draw scene
                mx,my,x,y,mario_size=jump(x,y,-7,deltax/2,.4,jumplist,leftflag,mx,my,oldx,mario_size,fireballcount) #gets picutres for this
            
            
    if collideflag==False: #if he collided but didn't kill them then he's dead 
        if mario_rect.collidelist(temp_enemies)!=-1 and Invincibleflag==False: #if anyother part of mario collides then he's dead
            #check if its alive too?
           # print 'died'
            mario_size=sizeCheck(mario_size)
            if mario_size=="death":
                LIVES-=1
                if LIVES==0:
                    deathrestart()
                x=SPAWNX
                y=SPAWNY
                mx=-100-(SPAWNX-400)

                my=0
                mario_size="small"
                State="Falling"
                Deathflag=True
                reset()
                name="World"+" "+str(WORLD)+"-"+str(LEVEL)
                drawlevel(name)                        
                

            else:
                 Invincibleflag=True
                 Invinciblecounter=0
                 changemusic("Power Down",sounds)
            


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





    if mario_rect.collidelist(temp_projectiles)!=-1 and Invincibleflag==False: #PROJECTILE COLLISONS

        mario_size=sizeCheck(mario_size)
        if mario_size=="death":
            LIVES-=1 #lowers lives
            if LIVES==0:
                deathrestart()
            x=SPAWNX
            y=SPAWNY
            mx=-100-(SPAWNX-400)

            my=0
            mario_size="small" # set size/state
            State="Falling"
            Deathflag=True
            reset()
            name="World"+" "+str(WORLD)+"-"+str(LEVEL)
            drawlevel(name)                        

        else:
            Invincibleflag=True
            Invinciblecounter=0
            changemusic("Power Down",sounds)

    if mario_rect.collidelist(roto_rects)!=-1 and Invincibleflag==False:  #ROTO DISK COLLISIONS

        mario_size=sizeCheck(mario_size)
        if mario_size=="death":
            LIVES-=1 #lowers lives
            if LIVES==0:
                quit()
            x=SPAWNX
            y=SPAWNY
            mx=-100-(SPAWNX-400)

            my=0
            mario_size="small" # set size/state
            State="Falling"
            Deathflag=True
            reset()
            name="World"+" "+str(WORLD)+"-"+str(LEVEL)
            drawlevel(name)                        

            
        else:
            Invincibleflag=True
            Invinciblecounter=0
            changemusic("Power Down",sounds)


    for hammer in temp_hammers: #checks if the hammer hits an enemey
        if hammer.collidelist(temp_enemies)!=-1:
            pos=hammer.collidelist(temp_enemies)
            Dynamic_Enemies[pos][7]="dead" #make his state dead            



            
    return mx,my,x,y,mario_size 
            
            
def twodimvalue(row,col,value): # returns all values of a 2d list?
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append(value) 
        list1.append(temp)
    return list1

    
def twodim(row,col): #makes a two d list 
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append((Rect(1,-500,1,1))) 
        list1.append(temp)
    return list1

def Statecheck2(Rectobject,siderect,siderect2):# FOR FIREBALLS, WE WANT TO CHECK IF IT HITS THE WALL FIRST 


    if siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
        State="Bounce"
    elif Rectobject.collidelist(top_plats)==-1: #they are either falling or moving 
        State="Falling"
    else:
        State="Moving"

    return State

def EnemeyStatecheck(Rectobject,siderect,siderect2,ycoord,State,speed,intial_v):
    


#siderect is right
#side rect 2 is left
    if State!='fire dead' and State!='dead': #we don't care if the enemey is dead 


        if speed>0:

        
            if Rectobject.collidelist(barriers)!=-1: #lets him bounce off tthe top if he's jumping 
               Rectobject[1]+=10 #moves him down a bit
               intial_v=0 # don't let him move up anymore 
               State="Falling"
                
            if siderect.collidelist(platforms)!=-1:
                
                State="Bounce" #they hit a wall 
                
            
                
            elif Rectobject.collidelist(platforms)!=-1: # set his y coord to the plaform 
               pos=Rectobject.collidelist(platforms)
               if bothplatforms[pos][3]==True: #if the platform was moving, we need to add a little bit
                   ycoord=platforms[pos][1]-Rectobject[3]+5
               else:
                   ycoord=platforms[pos][1]-Rectobject[3]+1 
               State="Moving"

            elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
                State="Falling"


        if speed<0: #if he's goign right we only care about if the right side collides...other than that its the same thing 
            

            if Rectobject.collidelist(barriers)!=-1: #lets him bounce off teh top if he's jumping
               Rectobject[1]+=10
               intial_v=0
               State="Falling"
                


            if siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
                State="Bounce"
            
            
                            
            elif Rectobject.collidelist(platforms)!=-1: # set his y coord to the 
               pos=Rectobject.collidelist(platforms)
               if bothplatforms[pos][3]==True:
                   ycoord=platforms[pos][1]-Rectobject[3]+5
               else:
                   ycoord=platforms[pos][1]-Rectobject[3]+1 #its not really 48...its the size or w/e
               State="Moving"

            elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
                State="Falling"

        if speed==0: #for inactive koopa stuff
            if Rectobject.collidelist(platforms)!=-1: # set his y coord to the 
               pos=Rectobject.collidelist(platforms)
               if bothplatforms[pos][3]==True:
                   ycoord=platforms[pos][1]-Rectobject[3]+5
               else:
                   ycoord=platforms[pos][1]-Rectobject[3]+1 #its not really 48...its the size or w/e
               State="Moving"
            else:
                State="Falling"

    return ycoord,State,intial_v

def Statecheck(Rectobject,siderect,siderect2,ycoord):#almost like standing check except for obstacles, and is much less complicated

    if Rectobject.collidelist(top_plats)==-1: #if ti didn't collide w/ a platform then its falling
        State="Falling"
        
    elif siderect.collidelist(platforms)!=-1:  # if it collides w/ a platform from the side its moving 
        
        State="Bounce"

        
    elif siderect2.collidelist(platforms)!=-1:
        State="Bounce"

        
    elif Rectobject.collidelist(platforms)!=-1:  #if it collided with a platform its moving
        pos=siderect.collidelist(platforms)
        if bothplatforms[pos][3]==True:#moving platform s
        
            ycoord=platforms[pos][1]-Rectobject[3]-10 #makes it set to the platform

        else:
            ycoord=platforms[pos][1]-Rectobject[3]+5
            
        State="Moving"

    return State,ycoord


#firstflag=True #FIX SPARKS
def drawPresets(x,y):
    global currentpresetframe
   # global firstflag
    mario_pos=x-400
    mario_pos=round(mario_pos) #FOR BULLET BILL, doesn't like integers, cause I used randint
    for object1 in Presets:
 

        if object1[1]=="cheep cheep":

            change=object1[3]+object1[2] #increase y
            object1[0][0]+=object1[4] #increaase x
            object1[0][1]+=change 
            object1[2]+=.4 #increase grav
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600 and object1[5]=='alive': #checks if its on screen, like enemies
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600 and object1[5]=='dead': #checks if its on screen, like enemies
                pic=Obstaclesdictionary[object1[1]]
                pic=transform.flip(pic,False,True)
                screen.blit(pic,(object1[0][0]-mario_pos,object1[0][1]))
                
            if object1[0][1]>600: #if it goes below we make a new one
                object1[0]=Rect(randint(mario_pos+300,mario_pos+600),randint(400,600),32,32)
                object1[1]="cheep cheep"
                object1[2]=0
                object1[3]=-20
                object1[4]=-3
                object1[5]='alive'
            
        if object1[1]=="spark":
            if object1[8]==True: # set it to the x,y position of platform, only ONCE 
                object1[7][0]=object1[0][0]
                object1[7][1]=object1[0][1]
                object1[8]=False #flag which indicates that its been set or not 
                
            if object1[6]==True: #if flag which indicates that its been set or not is true then .....
                if abs(object1[4])>object1[0][2]: #sees if acc x is greater htan length 
                    object1[2]*=-1 #reverse x
                    object1[6]=False #do y now
                    object1[4]=0 # set acc to zero
                else:
                    object1[7][0]+=object1[2] # just move it and increase acc x
                    object1[4]+=object1[2]
                    
            if object1[6]==False:
                if abs(object1[5])>object1[0][3]: #ses if acc y is greater than height 
                    object1[3]*=-1 #reverse y
                    object1[6]=True
                    object1[5]=0
                else:
                    object1[7][1]+=object1[3]
                    object1[5]+=object1[3]
  
            if not object1[7][0]+object1[7][2]-mario_pos<0 and not object1[7][0]-mario_pos>600: #checks if its on screen
                screen.blit(Obstaclesdictionary[object1[1]],(object1[7][0]-mario_pos,object1[7][1]))
                
        if object1[1]=="trampoline":

            newplat=object1[0] #
            if not object1[0][0]-mario_pos<0 and not object1[0][0]-mario_pos>600: #checks if it it onscreen 
                for p in range(newplat[1],newplat[1]+newplat[3]-1,32):#goes through all y values...
                    for j in range(newplat[0],newplat[0]+newplat[2]-1,32): # then go through and blit the appropirate texture
                        screen.blit(Scenerydictionary['trampoline'][0],(j-mario_pos,p)) #minus makes it go higher, plus makes it go lower
        
        if object1[1]=="coin" or object1[1]=="flag" : #just blit it to screen, no big deal 
            
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600:
                screen.blit(Obstaclesdictionary[object1[1]][currentpresetframe],(object1[0][0]-mario_pos,object1[0][1]))
                
        if object1[1]=="bullet bill":
            object1[0][0]+=-5 # increase by a speed of 5 to make it move 
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600: #checks if its on screen
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))
            if object1[0][0]-mario_pos<0:
                object1[0]=Rect(randint(mario_pos+600,mario_pos+2000),randint(1,580),32,28) #if it goes off we draw a new one,  randint makes them not all spawn in at the same time            object1[1]="bullet bill"
        if object1[1]=="fireball": #same thing as bulle bill 
            object1[0][0]+=-3 
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600: #checks if its on screen
                screen.blit(Obstaclesdictionary[object1[1]][currentpresetframe],(object1[0][0]-mario_pos,object1[0][1]))
            if object1[0][0]-mario_pos<0:
                object1[0]=Rect(randint(mario_pos+600,mario_pos+2000),randint(1,580),16,48) #if it goes off we draw a new one, yo, cause thats how I roll
                object1[1]="fireball"            



def drawObstacles(Displayflag,x,y,mx,my,deltax): #Draws obstacles on screen/don't need displayflag, whatever it is 
    global Jumpflag
    global currentpresetframe
    
    for object1 in Obstacles:



        
        mario_pos=x-400
        if object1[1]=="flower": #just draw these 
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600:
                screen.blit(Obstaclesdictionary[object1[1]][currentpresetframe],(object1[0][0]-mario_pos,object1[0][1]))
            
        if object1[1]=="hammer": 
            if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600:
                screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))



                
        if object1[1]=="mushroom" or object1[1]=="koopa shell" or object1[1]=="green mushroom" or object1[1]=="buzzy beetle shell" or object1[1]=="red koopa shell": #always subtracting Mario's original position
                if object1[0][1]>600: #checks if the object needs to be deleted...what is this for/just delete it
                    object1[0]=Rect(1,1,1,1) #this is just to make the relaetd lists work or else it will mess up..BIG TIME!
                    object1[1]=None
                    object1[2]=None
                    break

                
                intial_v=0 
                siderect=Rect(object1[0][0]+object1[0][2],object1[0][1],5,object1[0][3]-5) #right
                siderect2=Rect(object1[0][0]-3,object1[0][1],3,object1[0][3]-5) #left
                speed=object1[2]

                            
                object1[0][1],State,intial_v=EnemeyStatecheck(object1[0],siderect,siderect2,object1[0][1],None,speed,0) #Create a SPEED VARIABLE that way if the mushroom hits a wall if will "bounce off"
#                   
                shells=[]#sees if the object hit a shell then it'll reverse direction 
                for thingy in Obstacles:
                    if thingy!=object1:
                        if thingy[1]=="koopa shell" or thingy[1]=="buzzy beetle shell" or thingy[1]=="red koopa shell":
                            shells.append(thingy[0])
                            
                if object1[0].collidelist(shells)!=-1:
                    object1[2]*=-1
                        
                if State=="Bounce":
                    object1[2]=object1[2]*-1 #reverse velocity
                    #State="Moving" #then make it move
               
                if State=="Moving":
                    object1[0][0]=object1[0][0]+object1[2]
                        
                if State=="Falling": #5 works but six doesnt...
                    object1[0][1]=object1[0][1]+5 #CHECK IF THE OBSTACLE IS ACTUALLY ON SCREEN
                    object1[0][0]+=object1[2]/4 #makes it move somewhat horizontal
                    
                if not object1[0][0]+object1[0][2]-mario_pos<0 and not object1[0][0]-mario_pos>600: #changed 
                    screen.blit(Obstaclesdictionary[object1[1]],(object1[0][0]-mario_pos,object1[0][1]))

def flower(px,py,x,y,mx,my,deltax,pos): #makes a flower, appends to list 
    list1=[Rect(px,py,32,32),"flower",0]
    Obstacles.append(list1) #not sure if


def mushroom(px,py,x,y,mx,my,deltax,pos,type1): #draws mushroom on screen either normal/1up, appends to list 

    if type1=="green mushroom":
        list1=[Rect(px,py-32,32,32),"green mushroom",3]     #appends to list 
    if type1=="mushroom":
        list1=[Rect(px,py-32,32,32),"mushroom",3] #appends to list 

    Obstacles.append(list1)

def hammer(px,py,x,y,mx,my,deltax,pos): #same as flower basically 
    list1=[Rect(px-15,py-20,54,54),"hammer",0]
    Obstacles.append(list1) #not sure if    

def blockevents(name,px,py,x,y,mx,my,deltax,pos): #gets whats in the block, and sees if anything happens

    if name=="mushroom":

        mushroom(px,py,x,y,mx,my,deltax,pos,"mushroom")
    if name=="green mushroom":
        mushroom(px,py,x,y,mx,my,deltax,pos,"green mushroom")
    if name=="flower":
        flower(px,py,x,y,mx,my,deltax,pos)
    if name=="hammer":
        hammer(px,py,x,y,mx,my,deltax,pos)

        


def Deathcheck(x,y,mx,my,mario_size): #controls what happens after mario dies
    global State
    global LIVES
    global SPAWNX
    global SPAWNY
    global WORLD
    global LIVES


    LIVES-=1 # lowers life 
    if LIVES==0:
        deathrestart()

        
    else:
        name="World"+" "+str(WORLD)+"-"+str(LEVEL)
        drawlevel(name)
        reset() #rests platforms/enemies
      #  changemusic("Game Over",sounds) 
        x=SPAWNX # sets stuff back to default
        y=SPAWNY #if you make it too high he'll just like die and stuff
        mx=-100-(SPAWNX-400) # set it back to whatever -100 is default subtract mario's pos, moves in oppistie directions 
        my=0
        mario_size="small" #changes mario size 
        State="Falling" #make him falling

    return x,y,mx,my,mario_size
    

def movementcheck(State,Facing,RUNNING_SPEED,WALKING_SPEED): #checks to see if mario is running 

    if key.get_pressed()[K_LSHIFT]==True:
        horizontal_movement=7 #jump speed 
        speed=RUNNING_SPEED # set speed
    else:
        horizontal_movement=4
        speed=WALKING_SPEED
    return horizontal_movement,speed

def drawFullscene(screen,x,y,mx,my,deltax): #draws the full scene, returns what it looks like
    global selected_background
    drawScene(screen,mx,my,selected_background,False) #draws background
    Drawplatforms(screen,deltax,platforms,x,y) #draws/moves platforms
    drawPresets(x,y) #draws/moves prestes
    drawObstacles(False,x,y,mx,my,deltax) #mushrooms and stuff
    movefireball(-3,-.6,x) #draws/moves fireballs 
    movedynamic_enemies(x,y) #draws/moves enemies
    move_dynamicprojectiles(x,y) #draws/moves projectiles 
    drawrotodisk(x,y)#draws/moves rotodisks
    move_myhammers(x,y) #draws/moves enemies
    drawMenu() #draws menu at top
    return screen.copy() #trying to return the list for roto disks too
    

def drawScene(screen,x,y,back,flipflag): #controls the screen moving, left or right, maybe some problems moving back..?
    if flipflag==True: #flipflag has no meaning, it was something I was trying to use before but it iddn't work out
        screen.blit(transform.flip(Background_dictionary[back],True,False),(x,y))
    if flipflag==False:
        screen.blit(Background_dictionary[back],(x,y))


def changemusic(soundname,channel,loops=0): #takes a soundname and channle, then plays it 
    current_music=mixer.Sound(Musicdictionary[soundname]) #load the current music
    channel.play(current_music,loops) #play it on the appropriate channel

bounceflag=False
def standingCheck(jumpflag,x,y,mx,my,deltax,mario_size): #FUnction that checks what mario's state is 
    global Invincibleflag
    global Deathflag
    global Facing
    global State #having a top and bottom RECT makes it more accurate, won't "glitch" through platforms and such
    global bounceflag

    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer":
        mario_rect=Rect(x,y-34,40,64)
        bottom=Rect(x+10,y+34,24,4) # SHORTENED THIS 
        top=Rect(x+10,y-34,25,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(x+35,y-34,5,60)
        left_side=Rect(x-5,y-34,5,60) 
        size=35 #guess and check method...?

    if mario_size=="small":
        mario_rect=Rect(x,y,34,34)
        bottom=Rect(x+5,y+34,25,4) # shortened this
        top=Rect(x+10,y,24,4) #all rectangles surrounding mario, like "walls" sort of 
        right_side=Rect(x+35,y,5,30)
        left_side=Rect(x-5,y,5,30) 
        size=35 



    if State=="Falling" and jumpflag!=True: #if hes's just falling we only want to see if he collides w/ a platform not hte bounce states


        if bottom.collidelist(platforms)!=-1:  #if his bottom didn't collide w/ anythign 

            pos=bottom.collidelist(platforms)

            State="Standing" #THIS SOMEWHAT WORKS....BUT MESSES UP SIDE collisions


            if y+size<platforms[pos][1]+10: #this means that he fell from above os its okay,+10 to make him not fall through 
                y=platforms[pos][1]-size #if he's standing we want him to be at the same y coordinate as the platform
            else: # else he's falling from the side so he just has to fall down 
                State="Falling"


    
        else:
            State="Falling"


    elif jumpflag==True: #if he's jumping we always see if he can stop first



        if bottom.collidelist(top_plats)!=-1: #sees if he landed on a platform, maybe use platforms instead?

            State="Standing" 


 
        elif top.collidelist(barriers)!=-1: # this means that he hit the underside of the platform
            pos=top.collidelist(barriers)
            State="Bounce" #check is there was anythign in whatever he hit 
            if bothplatforms[top.collidelist(platforms)][1]=="question block" or bothplatforms[top.collidelist(platforms)][1]=="invisible": # if it was a question block we set to an empty block
                bothplatforms[top.collidelist(platforms)][1]="empty block"
                blockevents( bothplatforms[top.collidelist(platforms)][2],bothplatforms[top.collidelist(platforms)][0][0],bothplatforms[top.collidelist(platforms)][0][1]-32,x,y,mx,my,deltax,top.collidelist(platforms))


        elif right_side.collidelist(platforms)!=-1 and deltax>=0:  #only if he's moving to the....left
            State="Bounce3"
            pos=right_side.collidelist(platforms)  
            change=x-(platforms[pos][0]-mario_rect[2]-5) # set his x coord to the platforms side 
            x-=change
            mx+=change

        elif left_side.collidelist(platforms)!=-1: #and deltax<0: #don't need it here, cause he's obviously moving the other wa y
            State="Bounce2" #indiciates a collision at the side
            pos=left_side.collidelist(platforms) #makes sure that he can't go into teh platform more 
            newxcoord=platforms[pos][0]+platforms[pos][2]+5 #too close must add 5
            change=newxcoord-x
           #change=x-(platforms[pos][0]+platforms[pos][2]+mario_rect[2]) #oldx coord - new x coord
            x+=change
            mx-=change


        elif bottom.collidelist(top_plats)==-1: #change to mario_rect?
            State="Falling"

        



    else: #else we always check for collissions first, if he's just standing



        if right_side.collidelist(platforms)!=-1 and Facing=="Right": #sees if he hit the walls 
            State="Bounce3"
            
        elif left_side.collidelist(platforms)!=-1 and Facing=="Left":
            State="Bounce2" #indiciates a collision at the side
            
        elif len(bottom.collidelistall(platforms))>=1:

            State="Standing"
            list1=bottom.collidelistall(platforms)
            pos=list1[0]
            if bothplatforms[pos][3]==True and abs(bothplatforms[pos][5])>0: #if on a moving left/right platform
               print 'ok'
                
               mx+=bothplatforms[pos][5]*-1 #times by -1 to reverse background
               
             
               x+=bothplatforms[pos][5]
               
            if len(list1)>1: #can only really collide with 2
                
                if bothplatforms[list1[0]][3]==True: #if its moving up...then we want to collide w/ the moving one 
                    
                    if bothplatforms[list1[0]][4]<0:
                        pos=list1[0]
                    else:
                        pos=list1[-1]


                elif bothplatforms[list1[-1]][3]==True: #same principal here
                    if bothplatforms[list1[0]][4]<0:
                        pos=list1[-1]
                    else:
                        pos=list1[0]
                        
                y=platforms[pos][1]-size #if he's standing we want him to be at the same y coordinate as the platform

                         
            else:
                y=platforms[list1[0]][1]-size #if he's standing we want him to be at the same y coordinate as the platform
                #just change it normally
            
     
       # elif top.collidelist(platforms)!=-1 and bottom.collidelist(platforms)==-1: # this means that he hit the underside of the platform   
        #    State="Bounce" #Don't see how this could happen if he was standing...? =S
        #    print 'ok'
            
        elif bottom.collidelist(platforms)==-1:
            State="Falling"

        if State=="Standing" and bothplatforms[pos][1]=="lava" and Invincibleflag==False: #if he's standing in lave he's dead...obvioulsy 
            Deathflag=True
            x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)


                        


    return  x,y,mx,my,mario_size#return the new value

def makeplatforms(list1): #makes some platforms  - looks like [Rect,"texture","contains",movefflag,updown/movemen,leftright/movement,accmovement,limit]

    barriers=[]
    platforms2=[]
    platforms=[]
    for i in range(0,len(list1)): #platforms at the top...rect for side collisions, MAKE PLATFORMS A BIT BIGGER
        if list1[i][1]!="trampoline": #however, if this is a trampoline we don't want to have a collision at the top
            something4=Rect(list1[i][0][0],list1[i][0][1]-5,list1[i][0][2],32) #top platforms 
            platforms2.append(something4)
    for i in range(0,len(list1)):
        something1=Rect(list1[i][0][0],list1[i][0][1]+list1[i][0][3]-20,list1[i][0][2],20) #appends the bottom most layer
        #something2=Rect(list1[i][0][0],list1[i][0][1],15,list1[i][0][3]) #left layer, the 10 makes it look closer
       # something3=Rect(list1[i][0][0]+list1[i][0][2]-10,list1[i][0][1],5,list1[i][0][3])     #right layer,# right layer
        barriers.append(something1)
    for i in range(len(list1)): #makes the general platform 
        something3=Rect(list1[i][0][0],list1[i][0][1],list1[i][0][2],list1[i][0][3])
        platforms.append(something3)
    return list1,barriers,platforms2,platforms


def Drawplatforms(screen,deltax,platformlist,x,y): #draws/moves the platforms 

    mario_pos=x-400
    for i in range(len(bothplatforms)): #possibly check if it can be seen first then go through stuff...? might save time
        if bothplatforms[i][3]==True: #if its moving 

            if abs(bothplatforms[i][6])>bothplatforms[i][7]: #sees when it moves back 
                bothplatforms[i][4]*=-1
                bothplatforms[i][5]*=-1
            bothplatforms[i][6]=bothplatforms[i][6]+bothplatforms[i][4]+bothplatforms[i][5]
            
            bothplatforms[i][0][1]+=bothplatforms[i][4]
            bothplatforms[i][0][0]+=bothplatforms[i][5] #left/right

            barriers[i][0]+=bothplatforms[i][5] #moves the barrier 
            barriers[i][1]+=bothplatforms[i][4]

            top_plats[i][0]+=bothplatforms[i][5] #move the top pla t
            top_plats[i][1]+=bothplatforms[i][4]

            platforms[i][0]+=bothplatforms[i][5]
            platforms[i][1]+=bothplatforms[i][4]
 
        if bothplatforms[i][1]!="trampoline" and bothplatforms[i][1]!="invisible": #trampolines aren't drawn here 
            newplat=Rect(bothplatforms[i][0][0]-mario_pos,bothplatforms[i][0][1],bothplatforms[i][0][2],bothplatforms[i][0][3])

            #this doesn't make sense >>>>need mario pos
            if not newplat[0]>600 and not newplat[0]+newplat[2]<0:
                for p in range(newplat[1],newplat[1]+newplat[3]-1,Scenerydictionary[bothplatforms[i][1]][2]):#goes through all y values...
                    for j in range(newplat[0],newplat[0]+newplat[2]-1,Scenerydictionary[bothplatforms[i][1]][1]): #goes through x # then go through and blit the appropirate texture
                        screen.blit(Scenerydictionary[bothplatforms[i][1]][0],(j,p)) #blit texture to position 
            


    

def jump(x,y,intial_velocity,delta_x,gravity_change,pictures,boolean,mx,my,oldx,mario_size,fireballcount):  #mario size represents what stage he's in # make intial velocity negative, boolean represents left jump image
    global Facing
    global Invincibleflag
    global Invinciblecounter
    global framecounter
    global TIMER
    global currentframe
    global hammer_variable #maybe pass this in
    global Levelchange
    global enemeyframecounter
    global currentenemeyframe
    global TIMECOUNTER
    global presetframecounter
    global currentpresetframe
    global PRESET_DELAY
    global Deathflag
    gravity=0
    jumpclock=time.Clock()



    bounceflag=False #if he collides once, then he can't do it agian, in order to keep increasing, DON'T NEED THIS ANYMORE 
    deathflag=False

    while True:
        
        for evnt in event.get(): #checks fore fireballs/hammer events 
            if evnt.type==KEYDOWN:
                if evnt.key==102 and mario_size=="Fire":
                    fireballcount=fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount)
                    
                if evnt.key==102 and mario_size=="Hammer":

                    hammer_variable=hammercheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,hammer_variable)
###############################################                    
        if presetframecounter%ENEMEY_DELAY==0: #delay to make it look like he's walking
            currentpresetframe+=1 #advaance frame
            
        if currentpresetframe==4:
            currentpresetframe=0
        presetframecounter+=1 #counter that keeps track of frames

        if presetframecounter>=360: #can't go past this...
            presetframecounter=0    
################################
        if enemeyframecounter%ENEMEY_DELAY==0: #delay to make it look like he's walking
            currentenemeyframe+=1 #advaance frame
            
        if currentenemeyframe==3:
            currentenemeyframe=0
        enemeyframecounter+=1 #counter that keeps track of frames

        if enemeyframecounter>=360:
            enemeyframecounter=0    

#########################################3                    
        framecounter+=1 #increase counter


        if Levelchange==True: #if the level changes we don't want him to keep jumping 
            intial_v=0
            delta_x=0
            Levelchange=False

            
        if TIMECOUNTER%60==0: #controls time
            TIMER-=1 


        if framecounter%DELAY==0: #delay to make it look like he's walking
            currentframe+=1 #advaance frame
        
        if currentframe==3: #sets frame to zero, so it can't go over 
            currentframe=0
        
        if Invincibleflag==True:
            Invinciblecounter+=1
        if Invinciblecounter>=100:
            Invincibleflag=False

        if key.get_pressed()[K_RIGHT]==True: #ABILITY TO TURN AROUND IN THE AIR
            delta_x+=.07 #slightly increaes in this direction
            boolean=False
            Facing="Right"
        if key.get_pressed()[K_LEFT]==True:
            delta_x-=.07 #same thing here 
            boolean=True
            Facing="Left"

        TIMECOUNTER+=1
        
        if Deathflag==True: #if he just died then he doesn't keep his velocity 
            delta_x=0
            intial_velocity=0
            
        gravity+=gravity_change #gravity increases 
        change=intial_velocity+gravity #find the amount of increase

        #Bounce2 is from the lerft
        #Bounce 3 is from the right

        if State=="Bounce2" and Facing=="Left":  #if he hit a wall or something we don't want him to move forward anymore 
            delta_x=0
        if State=="Bounce3" and Facing=="Right":
            delta_x=0

       # print Deathflag


        y+=change #change the  y
        x+=delta_x #change the x

        

        mx=mx-delta_x
        pictures=pictureCheck(mario_size,"Jumping Right") #get pictures 
        mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,boolean,mx,my,delta_x,mario_size) #draws mario
        x,y,mx,my,mario_size=standingCheck(True,x,y,mx,my,deltax,mario_size)#gets state...
        
#I probaly should have drawn mario after all this, but oh well....

        
        if y>600:   #means that he went below the screen 
            x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)
            Deathflag=True

            gravity=0 # set gravity back to zero
            intial_velocity=3 #make him fall a tad 
            deathflag=True #we don't want him to move again


        if State=="Standing": #if he's standing we just return his position/size 
            pictures=pictureCheck(mario_size,"Standing")
            return mx,my,x,y,mario_size

        if State=="Bounce" and change<0: # if he hit the underside then we just jump again but this time with a downwards velocity 
            pictures=pictureCheck(mario_size,"Jumping Right")
            intial_velocity+=3
            
        
        elif State=="Bounce2"  and bounceflag==False: #sides collisions
            if change<0: #if he hit it going up...
                intial_velocity=intial_velocity-1 #move up a bit 
                delta_x=0           #don't him to move anymore
                bounceflag=True #dont' want him to move up more than once, so we make a flag 
                delta_x=0
            else:
                bounceflag=True

        elif State=="Bounce3" and bounceflag==False:
            if change<0:
                intial_velocity=intial_velocity-1
                delta_x=0            #pictures=pictureCheck(mario_size,"Standing")
                bounceflag=True 
                delta_x=0
            else:
                bounceflag=True
                
    
        jumpclock.tick(60) #controls FPS 
       # f (x,y)
    
        

def drawMario(screen,x,y,pic_list,leftflag,mx,my,deltax,mario_size): #draws mario with various animations
    global currentframe

    if mario_size=="small": #makes rectangle
       mario_rect=Rect(x,y,34,34)  
       yvariable=0 
    if mario_size=="Super" or mario_size=="Fire" or mario_size=="Hammer": #changed this to else
        mario_rect=Rect(x,y-34,40,64)
        yvariable=29 #controls how he collides w/ the platforms...cause he's bigger in this state
        
    mx,my,x,y,mario_size=Interactions(mario_rect,mario_size,y,x,deltax,leftflag,mx,my,oldx) #this may change the screen so we check 
    updated_screen=drawFullscene(screen,x,y,mx,my,deltax) #draws what the screen is going to look like first

        
    pic=pic_list[currentframe] #gets picture 
    
    if leftflag==True: #flips the image if its on the left side 
        pic=transform.flip(pic,True,False)
    
    screen.blit(updated_screen,(0,0)) #blits the updated screen
    
    if Invincibleflag==True: #this makes it look like he's flicking once he's been hit
        if currentframe%2==0: #so we draw him every other time 
            screen.blit(pic,Rect(400,y-yvariable,34,34)) #blits mario

    if Invincibleflag==False:
        screen.blit(pic,Rect(400,y-yvariable,34,34)) #blits mario
    

    display.flip()
 
    screen.fill(black)

    return mx,my,x,y,mario_size


def fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount):

                 if fireballcount<=2:
                     changemusic("Fireball",sounds)
                     if Facing=="Right": #sees which way it should move 
                         fireball_list[fireballcount][1]=7 #velocity 
                         fireball_list[fireballcount][0]=Rect(x+38,y,16,16) #rectangle
                         fireball_list[fireballcount][2]=0 #acc gravity 
                         drawMario(screen,x,y,throwanimation,False,mx,my,deltax,mario_size) #delay to make it look like he's throwing
                         time.wait(100) #delay makes it look like he has that "Throw animation"
                     else:
                        fireball_list[fireballcount][1]=-7 # same thing just facing left 
                        fireball_list[fireballcount][0]=Rect(x,y,16,16)
                        fireball_list[fireballcount][2]=0
                        drawMario(screen,x,y,throwanimation,True,mx,my,deltax,mario_size)
                        time.wait(100)
                     fireballcount+=1
                 return fireballcount


def polarToXY(dist, ang, offx,offy): #Mr Mckenzie made this when I needed help for the fireballs rotating =D! Thanky you sir!
    x= dist*cos(radians(ang))+offx #converts polar coordinate to x,y
    y= dist*sin(radians(ang))+offy
    return x,y

def makerotodisk(positionx,positiony,length): #mak es a rotodisk w/ the given parameters
    global rotodiskvariable#indicates what spot the firedisk will be at 
    Rotodisk_list[rotodiskvariable][0]=positionx #position of hte x 
    Rotodisk_list[rotodiskvariable][1]=positiony #postiion of the y
    Rotodisk_list[rotodiskvariable][2]=[]#indicates what 
    for i in range(0,20*length,20): #makes the fireballs of a certain length 
        Rotodisk_list[rotodiskvariable][2].append([i,0])
    rotodiskvariable+=1 #increase variable 


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
                

def move_myhammers(x,y): #[rect, acc gravity, intial_v,horizontalmovement
    global hammer_variable

    
    mario_pos=x-400
    for i in range(len(my_hammers)):
        if my_hammers[i][0]!=None:
            
            pic=projectile_hammer 


            if my_hammers[i][4]=="parabolic":

                if my_hammers[i][0][1]>600:
                    del my_hammers[i] #delete the old one
                    my_hammers.insert(0,[None,None,None,None,None,None]) #insert the new one
                    hammer_variable=0 # set it back to zero which would be the blank one 
                    break   
                
                pic=projectile_hammer
                
                #siderect=Rect(my_hammers[i][0][0]-6,my_hammers[i][0][1],6,10) #don't need this...
                #siderect2=Rect(my_hammers[i][0][0]+14,my_hammers[i][0][1],6,10)
               # State=Statecheck2(my_hammers[i][0],siderect,siderect2)                                            
                change=my_hammers[i][2]+my_hammers[i][1]
                my_hammers[i][1]+=.4 #increase gravity
                my_hammers[i][0][1]+=change #calculate change in the y 
                my_hammers[i][0][0]+=my_hammers[i][3] #horizontal movement
                my_hammers[i][5]+=5 #angle increase
                if my_hammers[i][5]==360:
                    my_hammers[i][5]=0
                pic=transform.rotate(pic,my_hammers[i][5]) #rotate by angle
                
            if not my_hammers[i][0][0]+my_hammers[i][0][2]-mario_pos<0 and not my_hammers[i][0][0]-mario_pos>600:

                screen.blit(pic,(my_hammers[i][0][0]-mario_pos,my_hammers[i][0][1]))

                
#WE'LL SET IT TO NONE DURING THE MOVE HAMMERS PART 

def hammercheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,hammer_variable):
                 if hammer_variable<=2:
                     if Facing=="Right": #sees which way it should move
                        my_hammers[hammer_variable][0]=Rect(x,y-30,54,54) #changed for hammer
                        my_hammers[hammer_variable][1]=0 #make a variable for this
                        my_hammers[hammer_variable][2]=randint(-12,-6)  #intial velocity...?
                        my_hammers[hammer_variable][3]=3 #movement horizontally, adds in an element of randomness
                        my_hammers[hammer_variable][4]="parabolic"
                        my_hammers[hammer_variable][5]=0 #angle representation
                        time.wait(100) #delay makes it look like he has that "Throw animation"
                        
                     if Facing=="Left":
                        my_hammers[hammer_variable][0]=Rect(x,y-30,54,54) #changed for hammer
                        my_hammers[hammer_variable][1]=0 #make a variable for this
                        my_hammers[hammer_variable][2]=randint(-12,-6)  #intial velocity...?
                        my_hammers[hammer_variable][3]=-3 #movement horizontally, adds in an element of randomness
                        my_hammers[hammer_variable][4]="parabolic"
                        my_hammers[hammer_variable][5]=0 #angle representation
                        time.wait(100)
                     hammer_variable+=1
                 return hammer_variable



#############################################


selected_background=None
selected_music='super mario world level 1'

def loadlevel(name): #loads a level from the given name 
    global my_hammers
    global hammer_variable
    global Rotodisk_list
    global roto_rects
    global Dynamic_Projectiles
    global Invincible_flag
    global Invinciblecount
    global fireball_list
    global fireballcount
    global DEFAULT_ENEMIES
    global Dynamic_Enemies
    global Presets
    global DEFAULT_PRESETS
    global Obstacles
    global bothplatforms
    global barriers
    global platforms
    global top_plats    
    global DEFAULT_PLATFORMS
    global DEFAULT_BARRIERS
    global DEFAULT_TOP_PLATS
    global DEFAULT_PLATFORMSNORM
    global x
    global y
    global mx
    global SPAWNX
    global SPAWNY
    global Levelchange #variable which indicates if the level has changed
    global selected_background
    global selected_music
    
    platform_file=open(name+"platforms.txt","r") # contains data for platforms 
    enemey_file=open(name+"enemies.txt","r") #data for where the enemies are
    roto_file=open(name+"rotodisks.txt","r") #data for where the rotodisks are
    preset_file=open(name+"presets.txt","r") #data for whre the preset items are
    variable_file=open(name+"othervariables.txt","r") #contains other things like spawn points, backgrond, music
    my_hammers=twodim(5,6)      # list for hammers 
    for i in range(len(my_hammers)):
        for j in range(len(my_hammers[i])):
            my_hammers[i][j]=None
    hammer_variable=0

    ########################
    Rotodisk_list=cPickle.load(roto_file) #reads from file 

    for roto in Rotodisk_list:
        roto[1]-=300 #has to be in sync 

    roto_rects=[]
    

    rotodiskvariable=0 #where to put it in the list

    Dynamic_Projectiles=twodim(10,6) #looks like [rect,accgravity,intial_v,horizontalmovement]
    for i in range(len(Dynamic_Projectiles)):
        for j in range(len(Dynamic_Projectiles[i])):
            Dynamic_Projectiles[i][j]=None

    Invincible_flag=False #
    Invinciblecount=30 
 

    ##############################

    ############

    fireball_list=[[None,None,None],[None,None,None],[None,None,None]] #looks like [Rect,direction,acc gravity]
    fireballcount=0

    enemey_data=cPickle.load(enemey_file)

    for enemey in enemey_data:
        enemey[1][1]-=300#caused by level editor


    DEFAULT_ENEMIES=enemey_data

    Dynamic_Enemies=twodimcopy(DEFAULT_ENEMIES)

    Presets=cPickle.load(preset_file) #loads presets from data file...

    for preset in Presets:
        preset[0][1]-=300#caused by level editor



    DEFAULT_PRESETS=twodimcopy(Presets)
    Obstacles=[] # looks like Rectangle,item,velocity

    data_platforms=cPickle.load(platform_file)

    for platform in data_platforms:
        platform[0][1]-=300 #caused by level editor

    bothplatforms,barriers,top_plats,platforms=makeplatforms(data_platforms) #both platforms contains both the rect and the texture in a 2d list 



    DEFAULT_PLATFORMS=twodimcopy(bothplatforms) #makes defaults 
    DEFAULT_BARRIERS=twodimcopy(barriers)
    DEFAULT_TOP_PLATS=twodimcopy(top_plats)
    DEFAULT_PLATFORMSNORM=twodimcopy(platforms)



    
    variable_list=variable_file.readlines()
    pos=variable_list[0].index("a")
    SPAWNX=int(variable_list[0][0:pos])
    SPAWNY=int( variable_list[0][pos+3:])-300
    selected_background=variable_list[1][:-1] #to get rid of the \n

    x=SPAWNX
    y=SPAWNY
    mx=-100-(SPAWNX-400) #make screen movement schronized with mario
    #changemusic('super mario world level 1',overworld_music,5)
    selected_music=variable_list[2]
    bgm_music(selected_music)
    mixer.music.set_volume(.1)
    Levelchange=False


########################


coincount=0   #keeps track of how many coins mario has


Jumpflag=False



Koopashellspeed=10






leftflag=False  



speed=10
gravityforce=.4

############################
#jumpingheight=-10
RUNNING_SPEED=10
WALKING_SPEED=5
horizontal_movement=4
deltax=2
mario_size="Fire"

#list1=[[Rect(320,400,97,16),"moving platform","none",True,0,3,0,300],[Rect(200,450,32,32),"block 1","none",True,1,0,0,100],[Rect(0,600-32,2000,20),"block 1","none",False,0,0,0],[Rect(800,450,32,500),"question block","mushroom",False,0,0,0],[Rect(900,450,32,32),"question block","mushroom",False,0,0,0],[Rect(1000,450,32,32),"question block","green mushroom",False,0,0,0],[Rect(1100,450,32,32),"invisible","flower",False,0,0,0],[Rect(1500,450,32,500),"block 1",False,0,0,0]]



flipvariable=False

Facing="Right"






intial_force=5
mario_gravity=0
##########################

#Counters and stuff

framecounter=0 #if divisible by some number then advance the frame possibly?
currentframe=0

enemeyframecounter=0
currentenemeyframe=0

ENEMEY_DELAY=7


Invincibleflag=False
Invinciblecounter=0

DELAY=5

TIMECOUNTER=0

###############

LIVES=5
TIMER=200


oldx=2

my=0

PRESET_DELAY=10
presetframecounter=0
currentpresetframe=0


################### MUSIC ###############




############LOAD LEVEL######################

screen.blit(Otherdictionary['title screen'],(0,0)) #blits title screen 
display.flip()
running2=True
while running2==True:
    for evnt in event.get():
        if evnt.type==KEYDOWN:
            running2=False

WORLD=2
LEVEL=4

name="World"+" "+str(WORLD)+"-"+str(LEVEL)
loadlevel(name)


################################################
running=True
State="Falling"
#Facing="Right"
myClock=time.Clock()


while running:

    Deathflag=False
    drawFlag=False


    if key.get_pressed()[27]==True: # checks for exit 
        quit()
################################################
    if presetframecounter%PRESET_DELAY==0: #delay to make it look like he's walking
        currentpresetframe+=1 #advaance frame
        
    if currentpresetframe==4:
        currentpresetframe=0
    presetframecounter+=1 #counter that keeps track of frames

    if presetframecounter>=360: #don't want to the counter to get too big 
        presetframecounter=0    


        
#########################################
        

    if enemeyframecounter%ENEMEY_DELAY==0: #delay to make it look like he's walking
        currentenemeyframe+=1 #advaance frame
        
    if currentenemeyframe==3:
        currentenemeyframe=0
    enemeyframecounter+=1 #counter that keeps track of frames

    if enemeyframecounter>=360:
        enemeyframecounter=0    


########################
    if abs(horizontal_movement)>4: #to make it look like he's moving faster when he's running...and stuff
        DELAY=3 #faster while running 
    if abs(horizontal_movement)<=4:
        DELAY=5


    if TIMECOUNTER%60==0: #controls time, every 60 frames is a second so it make sense, that it goes down by seconds, since the FPS is 60
        TIMER-=1  #PROBLEM...DELAY IS MESSED UP

    if framecounter%DELAY==0: #delay to make it look like he's walking
        currentframe+=1 #advaance frame
        
    if currentframe==3:
        currentframe=0
    framecounter+=1 #counter that keeps track of frames

    if framecounter>=360:
        framecounter=0

    TIMECOUNTER+=1

    if Invincibleflag==True: #keeps track of if he can be killed or not
        Invinciblecounter+=1 #increases
    if Invinciblecounter>=100: #if 100 he can be killed again
        Invincibleflag=False

    
    if Facing=="Right": #make a function, this determines the facing
        leftflag=False
    if Facing=="Left":
        leftflag=True

    horizontal_movement,speed=movementcheck(State,Facing,RUNNING_SPEED,WALKING_SPEED)

    if TIMER<=0:
        x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)
        
    if y>600: #if he fell below the level, lolol

        x,y,mx,my,mario_size=Deathcheck(x,y,mx,my,mario_size)

    


    #PUT ALL THIS INTO A FUNCTION...sorry sir, not enough time =(

         
    if State=="Falling": 
        if key.get_pressed()[K_RIGHT]==True: #allows him to kind of move when falling

                x+=1
                mx=mx-1
                Facing="Right"
        elif key.get_pressed()[K_LEFT]==True:
            x=x-1
            mx+=1
            Facing="Left"
        mario_gravity+=.1 #increase gravity 
        gforce=intial_force+mario_gravity
      #  x+=2 #make this variable
        y+=gforce
       # mx=mx-2
        pictures=pictureCheck(mario_size,"Standing")
            


    x,y,mx,my,mario_size=standingCheck(platforms,x,y,mx,my,deltax,mario_size) #only need to do this once, PERHAPS, TRY EXPERIMENTING W/ THIS


    
    if State=="Bounce3" or State=="Bounce2": # set mmovement to zero if he is colliding with a wall 
        horizontal_movement=0

        
    if State!="Falling": #gravity goes to 0 
        mario_gravity=0
        
    
    if State=="Standing" or State=="Bounce2" or State=="Bounce3": #Bounce2 and Bounce3 are collision states


        for evnt in event.get():

    
            if evnt.type==KEYDOWN:

                if evnt.key==102 and mario_size=="Hammer": #checks if he can throw fireballs/hammers

                    hammer_variable=hammercheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,hammer_variable)


                if evnt.key==102 and mario_size=="Fire": #checks if he can throw fireballs/hammers

                    fireballcount=fireballcheck(Facing,x,y,throwanimation,mx,my,deltax,mario_size,fireballcount)
            
                if key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_RIGHT]==True: #jumping to the right
                       drawFlag=True


                       Facing="Right"
                       pictures=pictureCheck(mario_size,"Jumping Right")
                       changemusic("Jump Sound",jumpsounds)
                       mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement,gravityforce,pictures,False,mx,my,deltax,mario_size,fireballcount) #boolen is for left flag
                       
                elif key.get_pressed()[K_SPACE]==True and key.get_pressed()[K_LEFT]==True:
                        drawFlag=True
                        Facing="Left"
                        pictures=pictureCheck(mario_size,"Jumping Left")
                        changemusic("Jump Sound",jumpsounds) 
                        mx,my,x,y,mario_size=jump(x,y,-10,horizontal_movement*(-1),gravityforce,pictures,True,mx,my,deltax,mario_size,fireballcount)
                        
                elif key.get_pressed()[K_SPACE]==True:# jumping straight up
                   # changemusic(0,1)
                    drawFlag=True                   
                    Facing=Facing #special case...where we check the facing to see how he jumps
                    if Facing=="Right": 
                        leftflag=False
                        movement=1 #works because its positive/negative
                        standingCheck(platforms,x+speed,y,mx,my,deltax,mario_size)
    
                        if State=="Bounce3" or State=="Bounce2": #if he jump against a wall...only need bounce3 here?
                            movement=0
                        pictures=pictureCheck(mario_size,"Neutral Jumping")
                        changemusic("Jump Sound",jumpsounds)
                        mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size,fireballcount)
                    elif Facing=="Left": #elif so he can't jump twice
                        drawFlag=True     
                        leftflag=True
                        movement=-1
                        standingCheck(platforms,x-speed,y,mx,my,deltax,mario_size)
                        if State=="Bounce2":
                            movement=0
                        pictures=pictureCheck(mario_size,"Neutral Jumping")
                        changemusic("Jump Sound",jumpsounds)
                        mx,my,x,y,mario_size=jump(x,y,-10,movement,gravityforce,pictures,leftflag,mx,my,oldx,mario_size,fireballcount)
                       # print "returned"
                
        if key.get_pressed()[K_RIGHT]==True: #movement to the right 
            drawFlag=True     
            Facing="Right"
            standingCheck(platforms,x+speed,y,mx,my,deltax,mario_size) #MAKE THIS NON GLOBAL
            if State=="Bounce3": #if he would collide, then we speed to zero because he can't move anymore, but he can move the other way
                speed=0
            x+=speed
            mx=mx-speed
            deltax=x-oldx
            pictures=pictureCheck(mario_size,"Moving Right")
          #  pictures=running_list
            mx,my,x,y,mario_size=drawMario(screen,x,y,pictures,False,mx,my,deltax,mario_size) #for run animation

        elif key.get_pressed()[K_LEFT]==True: #movement ot the left 
            drawFlag=True     
            Facing="Left"
            standingCheck(platforms,x-speed,y,mx,my,deltax,mario_size)

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


    oldx=x # set x to oldx...why did I need this/this was from before?
    oldy=y


    
            
    myClock.tick(60) #FPS...must be the same as jump one or else it'll ook stupid



########333YES I'M DONE!!!!!!!!!#####################

#TOTAL TIME SPENT: too long =P
    

    
