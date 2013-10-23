# Level Editor

###http://www.videogamesprites.net/SuperMarioBros/ AWESOME SITE, CONTAINS ALL THE SPRITES AND MOVING ANIMATIONS!! *drools*



#someflag=False



#seteup..same as the algorithm...I'm not going to comment it again, only the things that are different 


from pygame import*
from random import*
from colours import *
import cPickle
import os
from math import *



init()
size=width,height=1000,900
screen=display.set_mode(size)

drawablearea=Rect(0,300,100000,600) #area in which they can draw
#####################################
Musicdictionary={}



Musicdictionary["Basic Theme"]="World 1.OGG"
Musicdictionary["SMB3 Theme"]="sm3wd3.mid"
Musicdictionary['underwater']="sm3undw.mid"
Musicdictionary['smb3 overworld']="sm3ow2.mid"
Musicdictionary['ocean']="ocean.MID"
Musicdictionary['desert']='desert.MID'
Musicdictionary['grass']='grass.MID'
Musicdictionary['fortress']='fortress.MID'
Musicdictionary['jazz guitar']="marioworldjazzguitar.MID"
Musicdictionary['level-2']='level-2.MID'
Musicdictionary['mario intro']='smwintro.MID'
Musicdictionary['world two']='smwwd2.MID'

musiclist=Musicdictionary.keys()

#print len(musiclist)

#################list of possible containeres#########
#containers=["mushroom","flower","hammer","coin","green mushroom","None"]
Containerdictionary={} #dictionary that holds all possible containers 
Containerdictionary['mushroom']=image.load("Mushroom.PNG"),32,32
Containerdictionary['flower']=image.load("Fire Flower 1.PNG"),32,32
Containerdictionary['hammer']=image.load("um-hammer.GIF"),54,54
Containerdictionary['green mushroom']=image.load("1-Up Mushroom.GIF"),32,32


#############################


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
Scenerydictionary['mushroom platform']=image.load("Giant Mushroom.GIF"),96,128



#############################
Enemeydict={} #dictionary that contains enemey values
#looks like [name,rect,speed,dimensions,jump height,horizontal jump movement,acc gravity,state,jumpflag,SHOOTCOUNTER ,
# WALKFREQUENCY,JUMPFREQUENCY,SHOOTFREQUENCY,counter,projectiletype,reverseflag,accmovement,limit,jump_invulnerability,fire_invulnerability]



#have to be the same valuesss
#remember to fix tuple....?

Enemeydict['bowser']=["bowser",Rect(450,300,102,102),-2,(102,102),-15,0,0,"alive",False,2,4,25,10,2,"parabolic",False,0,1000000,False,10]
#bowser moves, just very slowly


Enemeydict['koopa']=["koopa",Rect(450,300,32,48),-2,(32,48),-15,1.5,0,"alive",False,2,1,301,301,2,"parabolic",False,0,200000,True,0]
Enemeydict['red koopa flying']=["red koopa flying",Rect(450,300,32,48),-2,(32,48),-15,-1.5,0,"alive",False,2,1,40,301,2,"parabolic",False,0,200,True,0]
Enemeydict['fast koopa']=["koopa",Rect(450,300,32,48),-5,(32,48),-10,1.5,0,"alive",False,2,1,301,301,2,"parabolic",False,0,10000,True,0]
Enemeydict['kuribos goomba']=["kuribos goomba",Rect(450,300,54,78),-5,(54,78),-15,-1.5,0,"alive",False,2,301,15,301,2,"parabolic",False,0,10000,True,0]
Enemeydict['flying koopa green']=["flying koopa green",Rect(450,300,32,48),3 ,(54,75),-15,1.5,0,"flying",False,2,1,301,301,1,"parabolic",False,0,100,True,0]
#changing the flying kooopa from 5 to 3
Enemeydict['goomba']=["goomba",Rect(450,300,32,32),-2,(32,32),-15,1.5,0,"alive",False,2,1,301,301,1,"parabolic",True,0,10000,True,0]
Enemeydict['cobrat']=["cobrat",Rect(450,300,54,102),-4,(54,102),-15,1.5,0,"alive",False,2,1,301,301,1,"parabolic",False,0,10000,True,0]
Enemeydict['hammer bros']=["hammer bros",Rect(450,300,32,48),-1,(32,48),-15,0,0,"alive",False,2,99,4,13,1,"parabolic",False,0,10000,True,0]
Enemeydict['snifit']=["snifit",Rect(450,300,54,54),-1,(54,54),-15,0,0,"alive",False,2,1,301,301,2,"parabolic",False,0,10000,True,0]
Enemeydict['podoboo']=["podoboo",Rect(450,300,32,48),-3,(32,48),-15,1.5,0,"flying",False,2,1,301,301,2,"parabolic",False,0,200,False,100]
#just changed podoboo
Enemeydict['buzzy beetle']=["buzzy beetle",Rect(450,300,32,30),-1,(32,32),-15,0,0,"alive",False,2,1,301,301,2,"parabolic",False,0,10000,True,1000]
Enemeydict['red koopa']=["red koopa",Rect(450,300,32,48),-2,(32,48),-15,1.5,0,"alive",False,2,1,301,301,2,"parabolic",False,0,1000000,True,0]
Enemeydict['spiny thing']=["spiny thing",Rect(450,300,32,32),-5,(32,32),-15,0,0,"alive",False,2,1,301,301,2,"parabolic",False,0,10000,False,0]
Enemeydict['birdo']=["birdo",Rect(450,300,32,32),-2,(27,38),-15,0,0,"alive",False,2,1,301,50,2,"straight",False,0,10000,False,0]
Enemeydict['dry bones']=["dry bones",Rect(450,300,54,87),-2,(54,87),-15,0,0,"alive",False,2,1,301,301,2,"parabolic",False,0,10000,False,100]
Enemeydict['piranha plant']=["piranha plant",Rect(450,300,32,48),-2,(32,48),-15,0,0,"flying",False,2,1,301,301,2,"parabolic",False,0,100,False,100]

#fireballs can't be killed on by jumping only by hammers

#for enemey in Enemeydict:
#    print enemey, "has length of", len(Enemeydict[enemey])
    

#############################
Enemiesdictionary={} #dictionary that stores enemies names/pictures

Enemiesdictionary['goomba']=image.load("Goomba 2 w-2.png"),32,32

Enemiesdictionary['koopa']=image.load("Green Koopa 1.png"),32,32

Enemiesdictionary['fast koopa']=image.load("Green Koopa 1.png"),32,32

Enemiesdictionary['flying koopa green']=image.load("Green Koopa Paratroopa.GIF"),32,48

Enemiesdictionary['red koopa']=image.load("Red Koopa Troopa.GIF"),32,48


Enemiesdictionary['hammer bros']=image.load("Hammer Brother.GIF"),32,48

Enemiesdictionary['birdo']=image.load("silver_birdo_sheet93.PNG"),27,38

Enemiesdictionary['bowser']=image.load("sm-bowser.GIF"),102,102

Enemiesdictionary['dry bones']=image.load("um-drybones.GIF"),54,87

Enemiesdictionary['buzzy beetle']=image.load("Buzzy Beetle - Blue.GIF"),32,30

Enemiesdictionary['cheep cheep']=image.load("Cheep Cheep - Red.GIF"),32,32

Enemiesdictionary['lakitu']=image.load("Lakitu1.GIF"),32,48 #how to do lakitu...?

Enemiesdictionary['piranha plant']=image.load("Piranha Plant.GIF"),32,48

Enemiesdictionary['podoboo']=image.load("Podoboo.GIF"),28,32 #put this in obstacles maybe..?

Enemiesdictionary['kuribos goomba']=image.load("um-kuribosgoomba.GIF"),54,78

#Enemiesdictionary['spark']=image.load("mw-spark.GIF"),54,54

Enemiesdictionary['snifit']=image.load("mw-snifit.GIF"),54,54

Enemiesdictionary['cobrat']=image.load("mw-cobrat.GIF"),54,102

Enemiesdictionary['spiny thing']=image.load("Spiny.GIF"),32,32

Enemiesdictionary['red koopa flying']=image.load("Red Koopa Paratroopa.GIF"),32,48

###################### Projectiles #############

projectile_hammer=image.load("um-hammer.GIF") #make dictionary

projectile_fireball=image.load("fireball_image.PNG")
fireballpic=image.load("Fireball.png")
spawn_image=image.load("enemey_projectile.PNG")

###########PRESET DICTIONARY###############

Presetdictionary={}

Presetdictionary['bullet bill']=image.load("Bullet Bill - Black.GIF"),32,28
Presetdictionary['coin']=image.load("Coin 1.png"),32,32
Presetdictionary['trampoline']=image.load("trampoline2.GIF"),32,32
Presetdictionary['spark']=image.load("mw-spark.GIF"),54,54
Presetdictionary['cheep cheep']=image.load("Cheep Cheep - Red.GIF"),32,32
Presetdictionary['flag']=image.load("Flag.PNG"),46,305
Presetdictionary['fireball']=image.load("fireball 1 copy.png"),48,16
#######################################################
Background_dictionary={}


Background_dictionary['sky']=image.load("Sky.bmp").convert()
Background_dictionary['sky2']=image.load("mario.jpg").convert()
Background_dictionary['underwater']=image.load("underwater.jpg").convert()
Background_dictionary['cloud background']=image.load("cloud background.jpg").convert()
Background_dictionary['forest']=image.load("laura's background fixed.png").convert()
Background_dictionary['sunset']=image.load("bg.PNG").convert()
Background_dictionary['forest night']=image.load("yee fan thing.JPG").convert()
Background_dictionary['desert']=image.load('desert(1).JPG').convert()
Background_dictionary['darkness']=image.load("darkness.BMP").convert()



#######################3 OLD FUNCTIONS - From Paint Program and/or Algorithm ###################################################

############# I"m not going to the comment these because you can just look in the algorithm ###################

def bgm_music(filename):
    #file1=filename+".MID"
    filename=Musicdictionary[filename]
    mixer.music.stop()
    mixer.music.load(filename)
    mixer.music.play(-1,0)

def Drawtext(words,size,(x,y),colour): #function that gets text size and a position from the user and draws it to the screen
    font_type=font.SysFont("Times New Roman",size) #gets the Times New Roman Font
    text=font_type.render(words,True,colour) #writes the text
    screen.blit(text,(x,y)) #blits text to the screen
    display.flip()


def highlight(Rectangle,colour,width): #function which takes a rectangle,colour, and width arguement and draws a rectangle around it
    draw.rect(screen,colour,Rectangle,width) #effectively acting as a highlight

def inputtext((x,y),length2,width,colour,size,limit): #function which allows the user to use the keyboard to input text at a specified location
    global Drawflag #length2/width are for a rectangle, colour is the colour, size is the size, and limit is how many characters can be inputted
    keyspressed=""
    image=Rect(x,y,length2,width*1.5) #makes a rectangle, width*1.5 is so that it won't leave marks if you backspace
   # image2=screen.subsurface(image).copy() #gets a copy of what that rectangle looks like, then keeps on blitting it
    image3=screen.copy() #i realized that just taking a picture of the whole screen was easier...and blitting that instead 
    Drawflag=False #determines whether or not the user hit esc
    looping=True
    Capsflag=False #determines whether or not to use capitals 
    while looping:
        for evnt in event.get(): #checks event quene
            if key.get_pressed()[27]==True or len(keyspressed)>=limit: #if there are too many characters or the user hits ESc WE break
                Drawflag=False
                screen.blit(image3,(0,0)) #to clear out the text
                looping=False
            elif key.get_pressed()[K_RETURN]==True or key.get_pressed()[271]==True: #if the user hits the enter key then we stop seeing what key they pressed
                looping=False
            elif key.get_pressed()[K_BACKSPACE]==True: #if the user presses backspace then the last letter they typed is erased
                length=len(keyspressed)
                keyspressed=keyspressed[0:length-1]
            elif key.get_pressed()[K_LSHIFT]==True: #use shift to toggle between lower case and capital letters
                if Capsflag==True:  #if its true, then its false, and vice versa 
                    Capsflag=False
                elif Capsflag==False:
                    Capsflag=True
            elif evnt.type==KEYDOWN: #finds out what key the user pressed and puts it into a string
                if Capsflag==False: #lower case
                    if evnt.key<256: #makes the program not crash when you hit something stupid/not in range
                        keyspressed+=chr(evnt.key)
                if Capsflag==True: #captial s
                    if evnt.key<256: #makes the program not crash when you hit something stupid/not in range
                        letter=chr(evnt.key)
                        capital_letter=caps(letter)
                        keyspressed+=capital_letter
                Drawflag=True
            #screen.blit(image2,(x,y)) #to clear out the text
            screen.blit(image3,(0,0)) #clears out text...allows for backspacing 
            Drawtext(keyspressed,size,(x,y),colour) #draw the text
            display.flip()  #update screen
    return keyspressed #return the string 


def EnemeyStatecheck(Rectobject,siderect,siderect2,ycoord,State,platforms,speed):

    if State!='fire dead':

        if speed>0:
        
            if siderect.collidelist(platforms)!=-1: #if he's going left we only care if this side collides w/ something, so its okay if he falls
                
                State="Bounce"
                

                
            elif Rectobject.collidelist(platforms)!=-1: # set his y coord to the 
               pos=Rectobject.collidelist(platforms)
               ycoord=platforms[pos][1]-Rectobject[3]+1 #its not really 48...its the size or w/e
               State="Moving"

            elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
                State="Falling"


        if speed<0: #if he's goign right we only care about if this side collides, otherwise its okay if he's falling

            if siderect2.collidelist(platforms)!=-1:
                
                State="Bounce"
                

                
            elif Rectobject.collidelist(platforms)!=-1: # set his y coord to the 
               pos=Rectobject.collidelist(platforms)
               ycoord=platforms[pos][1]-Rectobject[3]+1 #its not really 48...its the size or w/e
               State="Moving"

            elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
                State="Falling"            
                

    return ycoord,State


def movedynamic_enemies(x,y,Dynamic_Enemies):

    global projectilevariable
    global Obstaclevariable
    global offset


#this doesn't matter we only care about the offest 
    mario_pos=x-400 #looks like [name,rect,speed,dimensions,jump height,horizontal jump movement,acc gravity,state,
    
    for i in range(len(Dynamic_Enemies)):
        name=Dynamic_Enemies[i][0]
        dimensions=Dynamic_Enemies[i][3]
        jump_height=Dynamic_Enemies[i][4]
        horizontal_movement=Dynamic_Enemies[i][5]
        siderect=Rect(Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][3][0],Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)# represents rectangle at the side
        siderect2=Rect(Dynamic_Enemies[i][1][0]-3,Dynamic_Enemies[i][1][1],3,Dynamic_Enemies[i][3][1]-10)
        Dynamic_Enemies[i][1][1],State=EnemeyStatecheck(Dynamic_Enemies[i][1],siderect,siderect2,Dynamic_Enemies[i][1][1],Dynamic_Enemies[i][7],plat_list,Dynamic_Enemies[i][2])
 


        
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

                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][0]


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
                            Dynamic_Projectiles[projectilevariable][2]=randint(-13,-6)  #intial velocity...?
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
                       
                        
                            

                                        
            

                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][0]
                
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
                    pic=Enemiesdictionary[Dynamic_Enemies[i][0]][0]

                del Dynamic_Enemies[i]
                break

            elif Dynamic_Enemies[i][7]=="fire dead":
                pic=Enemiesdictionary[Dynamic_Enemies[i][0]][0]
                pic=transform.flip(pic,False,True)
                Dynamic_Enemies[i][1][1]+=3
       #don't need to this, already checking through see check         
      #      if not Dynamic_Enemies[i][1][0]+Dynamic_Enemies[i][1][2]-mario_pos<0 and not Dynamic_Enemies[i][1][0]-mario_pos>600: #checks if the enemey can be seen onscreen
            screen.blit(pic,(Dynamic_Enemies[i][1][0]-offset,Dynamic_Enemies[i][1][1])) #if they can be then we draw them

          #  print Dynamic_Enemies[i][16]
            
    
def seeCheck(x,y,Rectobject):
    #offset instad of mario pos
    flag=False
    mario_pos=x-400 #changed this
    if not Rectobject[0]+Rectobject[2]-offset<0 and not Rectobject[0]-offset>1000: #1000 is size of screen yo
        flag=True
    return flag
    
def twodim(row,col):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append((Rect(1,-500,1,1))) 
        list1.append(temp)
    return list1

def move_dynamicprojectiles(x,y): #[rect, acc gravity, intial_v,horizontalmovement
    global offset
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
                State=Statecheck2(Dynamic_Projectiles[i][0],siderect,siderect2,plat_list)                                            
                change=Dynamic_Projectiles[i][2]+Dynamic_Projectiles[i][1]
                Dynamic_Projectiles[i][1]+=.4 #increase gravity
                Dynamic_Projectiles[i][0][1]+=change
                Dynamic_Projectiles[i][0][0]+=Dynamic_Projectiles[i][3] #horizontal movement
                Dynamic_Projectiles[i][5]+=5 #angle increase
                if Dynamic_Projectiles[i][5]==360:
                    Dynamic_Projectiles[i][5]=0
                pic=transform.rotate(pic,Dynamic_Projectiles[i][5]) #rotate by angle


            #dont need this...FIX THIS FIX THIS FIX THIS     
            if not Dynamic_Projectiles[i][0][0]+Dynamic_Projectiles[i][0][2]-mario_pos<0 and not Dynamic_Projectiles[i][0][0]-mario_pos>600:

                screen.blit(pic,(Dynamic_Projectiles[i][0][0]-offset,Dynamic_Projectiles[i][0][1]))
            

def Statecheck2(Rectobject,siderect,siderect2,platforms):# FOR FIREBALLS, WE WANT TO CHECK IF IT HITS THE WALL FIRST YO


    if siderect.collidelist(platforms)!=-1 or siderect2.collidelist(platforms)!=-1: #if either of those rects hit a platform
        State="Bounce"
    elif Rectobject.collidelist(platforms)==-1: #they are either falling or moving 
        State="Falling"
    else:
        State="Moving"

    return State


def Drawplatforms(screen,deltax,bothplatforms,x,y): ##just passing in a list, might be called something else, makes life easier
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

 
        if bothplatforms[i][1]!="trampoline" and bothplatforms[i][1]!="invisible":
            newplat=Rect(bothplatforms[i][0][0]-mario_pos,bothplatforms[i][0][1],bothplatforms[i][0][2],bothplatforms[i][0][3])

            #this doesn't make sense >>>>need mario pos
            #add in RESTRICTIONS
            for p in range(newplat[1],newplat[1]+newplat[3]-1,Scenerydictionary[bothplatforms[i][1]][2]):#goes through all y values...
                for j in range(newplat[0],newplat[0]+newplat[2]-1,Scenerydictionary[bothplatforms[i][1]][1]): #goes through x # then go through and blit the appropirate texture
                    screen.blit(Scenerydictionary[bothplatforms[i][1]][0],(j-offset,p)) #blit texture to position 
        #added in minus offset 



def makerotodisk(positionx,positiony,length,Rotodisk_list): #makes a rotodisk w/ the given parameters
    global rotodiskvariable
    newlist=[]
    newlist.append(positionx)#makes a list as long asyou want 
    newlist.append(positiony)
#    Rotodisk_list[newlist][2]=[]

    newlist2=[]
    for i in range(0,20*length,20): #but this will have to change...?
        newlist3=([i,0])
        newlist2.append(newlist3)

    newlist.append(newlist2)
    Rotodisks.append(newlist)


def drawrotodisk(x,y,Rotodisk_list):
  #  global offset

    rec_list=[]
    for i in range(len(Rotodisk_list)): #draws all teh rects and stuff and returns the list
        if Rotodisk_list[i][0]>0:
            for fire in Rotodisk_list[i][2]:
                fire[1]=fire[1]+3 % 360 #increase angle
                x,y=polarToXY(fire[0],fire[1],Rotodisk_list[i][0],Rotodisk_list[i][1]) #get x,y coordinate
                rec=Rect(x,y,10,10) #mjake a rect
         #       roto_rects.append(rec) #draw it

                if not rec[0]+rec[2]-offset>1000 and not rec[0]-offset<0:
                    screen.blit(fireballpic,(rec[0]-offset,rec[1])) #blit it w/ fireball
                
def polarToXY(dist, ang, offx,offy):
    x= dist*cos(radians(ang))+offx
    y= dist*sin(radians(ang))+offy
    return x,y

def drawScene(screen,x,y,back): #controls the screen moving, left or right, maybe some problems moving back..?
    global offset
    x+=offset*-1 #reverse
    screen.blit(Background_dictionary[back],(x,y))
#################################################################################################

###############################################################333NEW  FUNCTIONS #####################################################

def enemey_prompt(x,y,name):




  
    enemey=(Enemeydict[name])[:]
    #gets copy of what the enemey variable contains...
    # have to make a copy of hte list, or else the rect object will be overwritten

    
    value=Rect(x,y,enemey[3][0],enemey[3][1]) #then you change w/e the coordinates of the top left corner were to x,y
    enemey[1]=value # set to value...don't know if this makes a difference??
    return enemey
    

def platformprompt(list1,last_rect,selected_texture,selected_container): #asks the user if they want the platform to be moving 

    
  #  inputtext((x,y),length2,width,colour,size,limit)
    Drawtext("Movement Options",50,(200,0),pink) #ask them what they want 
    Drawtext("Do you want your platform to be moving? y/n",30,(150,75),pink)
    string=""
    string=inputtext((200,200),400,300,blue,30,50)
    


    list1.append(selected_texture)


    list1.append(selected_container)

    
    

    if string=="y" or string=="Y": #if they hit yes then we do all this input, otherwise we don't really care 
            list1.append(True)
            draw.rect(screen,black,Rect(0,0,1000,300))
            display.flip()
            Drawtext("how fast do you want it to move up/down",30,(110,0),pink) #ask them what they want   
           # up_down=input("how fast do you want it to move up/down") 
            num=inputtext((200,200),400,300,blue,30,50)
            num=int(num)
            list1.append(num)
            draw.rect(screen,black,Rect(0,0,1000,300))
            display.flip()
            Drawtext("how fast do you want it move left/right",30,(110,0),pink) #ask them what they want
         #   left_right=input("how fast do you want it move left/right")
            num=inputtext((200,200),400,300,blue,30,50)
            num=int(num)
            list1.append(num)
            acc_movement=0
            list1.append(acc_movement)
           # limit=input("how far do you want it to be able to move before it stops")
            draw.rect(screen,black,Rect(0,0,1000,300))
            display.flip()
            Drawtext("how far do you want it to be able to move before it stops",30,(110,0),pink) #ask them what they want
            num=inputtext((200,200),400,300,blue,30,50)
            num=int(num)
            list1.append(num)
            draw.rect(screen,black,Rect(0,0,1000,300))
            display.flip()
           # list1.append(limit)
    else: #if its not moving then we don't care
        list1.append(False)
        list1.append(0)
        list1.append(0)
        list1.append(0)
        list1.append(0)


    return list1
    

def getMouse(): #returns state of mouse...
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()[0]
    return mx,my,mb

clickflag=False
def make_enemies(selected_enemey):
    global clickflag
    
    x,y=mouse.get_pos()
    
    if mouse.get_pressed()[2]==1: #allows you to delete stuff 
        x+=offset
        for i in range(len(Enemies)):
            rectangle=Enemies[i][1]
            if rectangle.collidepoint(x,y)==True: #if they right clicked on the rectangle
                del Enemies[i]
                break
                       
    if mouse.get_pressed()[0]==1 and clickflag==False: #if they clicked....and it wasn't pressed before
    
        #x,y=mouse.get_pos()
        for rectangle in Enemeyreclist:
            if rectangle[0].collidepoint(x,y)==True:
                selected_enemey=rectangle[1]
                                 
        if drawablearea.collidepoint(x,y)==True and selected_enemey!=None:#if they clicked inside where the enemies can be
               
            newx=x+offset
            length=Enemiesdictionary[selected_enemey][1] #just draws them on screen 
            height=Enemiesdictionary[selected_enemey][2]
            newx=newx-length/2 #divide by 2 to be in sync w/ the mouse 
            y=y-height/2
            enemey=enemey_prompt(newx,y,selected_enemey)
            Enemies.append(enemey)
            clickflag=True #variable which indicates whether the mouse has been pressed or not 
            #now they did press it so its true


    if selected_enemey!=None:
        length=Enemiesdictionary[selected_enemey][1] #just draws them on screen 
        height=Enemiesdictionary[selected_enemey][2]
        screen.blit(Enemiesdictionary[selected_enemey][0],(x-(length/2),y-(height/2)))

    return selected_enemey


def divisible32(n): #we wnat to round it off to 32, so he can't like fall off
	remainder=n%32
	if remainder>=16:
		remainder=32-remainder
		n+=remainder
	else:
		n=n-remainder
	return n

        
 
def drawplatforms(selected_texture,selected_container):  #draws platforms 
    global offset
    x,y=mouse.get_pos()
    mouse_status="up"

    if mouse.get_pressed()[2]==1: #allows you to delete platforms or w/e
        x+=offset
        for i in range(len(Platforms)):
            rectangle=Platforms[i][0]
            if rectangle.collidepoint(x,y)==True: #if they right clicked on the rectangle
                del Platforms[i]
                break
                       
    if mouse.get_pressed()[0]==0 and selected_texture!=None and drawablearea.collidepoint(x,y): #if he's able to draw it...
        mx,my=mouse.get_pos()
        

        screen.blit(Scenerydictionary[selected_texture][0],(mx-16,my-16))

    if mouse.get_pressed()[0]==1:
        for rect in Platformrectlist: #sees what texture they clicked 
            x,y=mouse.get_pos()
            rectangle=rect[0] 
            if rectangle.collidepoint(x,y)==True:
                selected_texture=rect[1]
        for container in Container_rectlist:
            x,y=mouse.get_pos()
            rectangle=container[0]
            if rectangle.collidepoint(x,y)==True:
                selected_container=container[1]
            
    if mouse.get_pressed()[0]==1 and drawablearea.collidepoint(x,y)==True: 
        x,y=mouse.get_pos()
        x=x+offset
        previous_screen=screen.copy() #gets what it looks like before I start drawing stuff
        mouse_status="down"
        while mouse_status=="down":
            rectangleflag=False #flag which indicates if they clicked the mouse and didn't hold it down
            screen.blit(previous_screen,(0,0))
            event.get()

            mx,my=mouse.get_pos()
            mx=mx+offset
            delta_x=mx-x

            event.get()

            if key.get_pressed()[K_LEFT]==True: #able to increase offset while drawing 
                offset=offset-10
                    
            if key.get_pressed()[K_RIGHT]==True:
                offset+=10
            

 ##############333 COPY AND PASTE FROM PAINT PROGRAM ########################3
            
            if delta_x<0:
                delta_x=delta_x*(-1) #we don't want it to be negative, so if it is we make it positive
            delta_y=my-y
            if delta_y<0: #find the change in the y values
                delta_y=delta_y*(-1)
            if mx<x and my<y: #draw a rectangle to the TOP LEFT
                last_rect=Rect(x-delta_x,y-delta_y,delta_x,delta_y) #REMEMBERS WHAT THE RECTANGLE IS , maybe just subtract offsets here
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2) #have to subtract offsets
                rectangleflag=True
            if mx>x and my<y: #draws a rectangle to the BOTTOM RIGHT
                last_rect=Rect(x,y-delta_y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
                rectangleflag=True
            if mx>x and my>y: #BOTTOM LEFT
                last_rect=Rect(x,y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
                rectangleflag=True
            if mx<x and my>y: #TOP RIGHT
                last_rect=Rect(x-delta_x,y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
                rectangleflag=True
            display.flip()
            
            if mouse.get_pressed()[0]==0 and mouse_status=="down" and rectangleflag==True: 
                mouse_status="up"
                last_rect[2]=divisible32(last_rect[2]) #to make it even, for him to walk on
                last_rect[3]=divisible32(last_rect[3]) #see above =P
                
                if last_rect[2]!=0 and last_rect[3]!=0: #if its zero that means that they drew it too small and I don't care 
                    list1=[] # list that holds the platform and other information that you have to input, 
                    list1.append(last_rect) #just prompts for other information
    
                    newlist=platformprompt(list1,last_rect,selected_texture,selected_container)
                    
                    
                    Platforms.append(newlist) #ADDS THE RECTANGLE THAT YOU JUST DREW TO THE LIST, 

            if mouse.get_pressed()[0]==0 and mouse_status=="down" and rectangleflag==False: #if they just clicked then we don't care
               #just draw it where it was
                list1=[]
                #...shoudln't be -16, cause not all platforms are like that but w/e....I should really get the width/height
                last_rect=Rect(mx-16,my-16,Scenerydictionary[selected_texture][1],Scenerydictionary[selected_texture][2])
                list1.append(last_rect)
                
                newlist=platformprompt(list1,last_rect,selected_texture,selected_container)
                Platforms.append(newlist)

                mouse_status="up"

               
    return selected_texture,selected_container

def rotodiskcreator():
    if mouse.get_pressed()[2]==1:
        x,y=mouse.get_pos()
        x+=offset
        for i in range(len(Rotodisks)): #deletion...finds rect...checks collidepoint
            for j in range(len(Rotodisks[i][2])):

                x,y=polarToXY(Rotodisks[i][2][j][0],Rotodisks[i][2][j][1],Rotodisks[i][0],Rotodisks[i][1]) #get x,y coordinate
                rec=Rect(x,y,10,10) #mjake a rect
                if rec.collidepoint(x,y)==True:
                    del Rotodisks[i]
                    break                #dist, angle, offx, offy

                
    if mouse.get_pressed()[0]==1:
        x,y=mouse.get_pos()
        x=x+offset
        
        Drawtext("How long do you want the rotodisk to be?",30,(150,75),pink) # ask them for length input 
        length=""
        length=inputtext((200,200),400,300,blue,30,50)
        length=int(length)
        makerotodisk(x,y,length,Rotodisks)
        
          

def presetprompt(x,y,name):
    list1=[]

    length=Presetdictionary[name][1]
    height=Presetdictionary[name][2]
    rectobject=Rect(x-length/2,y-height/2,length,height)
    list1.append(rectobject)    
    list1.append(name)
    someflag=False
    if name=="trampoline": #tramplines also must be appened to platforms 
        list2=[Rect(x,y+5,Presetdictionary[name][1],Presetdictionary[name][2]-5),"trampoline",None,False,0,0,0,0]
        Platforms.append(list2)


    if name=="cheep cheep": #cheep cheep looks like (rect,name,acc gravity,intial v,horizontal_movement)
        list1.append(0)
        list1.append(-20)
        list1.append(-3)
        list1.append('alive')
        list1.append(None)
        list1.append(None)
        list1.append(None)
        someflag=True

        
    if someflag==False:
        list1.append(None)
        list1.append(None)
        list1.append(None)
        list1.append(None)
        list1.append(None)
        list1.append(None)
        list1.append(None)
    return list1

                
def makePresets(offset,selected_preset):
    global clickflag
    x,y=mouse.get_pos()
    
    if mouse.get_pressed()[2]==1: #allows you to delete presets or w/e
        x+=offset
        for i in range(len(Presets)):
            rectangle=Presets[i][0]
            if rectangle.collidepoint(x,y)==True: #if they right clicked on the rectangle
                del Presets[i]
                break
            
    if selected_preset!=None:
        length=Presetdictionary[selected_preset][1] #just draws them on screen 
        height=Presetdictionary[selected_preset][2]
        screen.blit(Presetdictionary[selected_preset][0],(x-(length/2),y-(height/2)))    
    
    if mouse.get_pressed()[0]==1 and clickflag==False: #only get one evnt 
        x,y=mouse.get_pos()
        for rect in Presetrectlist:
            rectangle=rect[0]
            if rectangle.collidepoint(x,y)==True:
                selected_preset=rect[1]
                
        if selected_preset!=None and drawablearea.collidepoint(x,y)==True:
            mx,my=mouse.get_pos()
            mx+=offset
            if selected_preset=="spark": #use clickflag hereee
                temp_plats=[]
                for plat in Platforms:
                    temp_plats.append(plat[0])
                for rect in temp_plats: #get the rectanglet hat you want it to rotate around 
                    if rect.collidepoint(mx,my)==True:
                        list1=[Rect(rect[0],rect[1]-32,rect[2],rect[3]),'spark',2,2,0,0,True,Rect(mx,my,54,54),True]
                        Presets.append(list1)
            else:
                        
                
                list1=presetprompt(mx,my,selected_preset)
                Presets.append(list1)
            clickflag=True
            
    return selected_preset
     #   x+=offset
      #  list1=presetprompt(x,y)
      #  Presets.append(list1)

def Drawpresets(offset):
    for thing in Presets:
        rect1=thing[0]
        name=thing[1]
        screen.blit(Presetdictionary[name][0],(rect1[0]-offset,rect1[1]))
#        elif name=="spark":
    #        screen.blit(Presetdictionary['spark'][0],(thing[6][0]-offest,thing[6][1]))

#######Other Variables ###################

def Drawpresetoptions():
    Presetrectlist=[] #looks like (rect,name)

    Presetnamelist=[] # list that holds the name of all the enemies
    
    for i in Presetdictionary:
        Presetnamelist.append(i)

    
    count=0

    for j in range(0,201,100): #loops through to make rects/draws enemies, x values, y values 
        if count==7:
            break
        for i in range(0,1000,150):
            if count==7:
                break
            item=Presetnamelist[count]
            length=Presetdictionary[item][1] #gets length
            height=Presetdictionary[item][2] # gets width
            rectangle=Rect(i,j,length,height)
            screen.blit(Presetdictionary[item][0],rectangle)
            Presetrectlist.append((rectangle,item))
            count+=1

    draw.rect(screen,blue,drawablearea,5)

    return Presetrectlist

        
def Drawenemeyoptions(): #see above  ^^^
    Enemeyreclist=[] #looks like (rect,name)

    Enemiesnamelist=[] # list that holds the name of all the enemies
    
    for i in Enemiesdictionary:
        Enemiesnamelist.append(i)

    
    count=0

    for j in range(0,201,100): #loops through to make rects/draws enemies
        if count==19:
            break
        for i in range(0,1000,150):
            if count==19:
                break
            enemey=Enemiesnamelist[count]
            length=Enemiesdictionary[enemey][1] #gets length
            height=Enemiesdictionary[enemey][2] # gets width
            rectangle=Rect(i,j,length,height)
            screen.blit(Enemiesdictionary[enemey][0],rectangle)
            Enemeyreclist.append((rectangle,enemey))
            count+=1

    draw.rect(screen,blue,drawablearea,5)
    return Enemeyreclist

        
    
def Drawplatformoptions():
    Platformrectlist=[]
    Platformnamelist=[]

    Containernamelist=[]
    Container_rectlist=[]

    for name in Containerdictionary:
        Containernamelist.append(name)

    for i in Scenerydictionary:
        Platformnamelist.append(i)

    count=0
    for j in range(0,201,100):
        if count==21:
            break        
        for i in range(0,1000,100):
           if count==21:
                break
           texture=Platformnamelist[count]
           length=Scenerydictionary[texture][1]
           height=Scenerydictionary[texture][2]
           rectangle=Rect(i,j,length,height)
           screen.blit(Scenerydictionary[texture][0],rectangle)
           Platformrectlist.append((rectangle,texture))
           count+=1

    count=0
    for j in range(200,301,100):
            if count==4:
                break
            for i in range(0,1000,100):
               if count==4:
                   break
               container=Containernamelist[count]
               length=Containerdictionary[name][1]
               height=Containerdictionary[name][2]
               rectangle=Rect(i,j,length,height)
               screen.blit(Containerdictionary[container][0],rectangle)
               Container_rectlist.append((rectangle,container))
               count+=1


    return Platformrectlist,Container_rectlist
    
 
def select_background(): #sees waht key they pressed and draw the appropriate background 
    global selected_background
    if key.get_pressed()[K_F1]==True:
        print 'ok'
        selected_background='sky'
    if key.get_pressed()[K_F2]==True:
        selected_background='cloud background'
    if key.get_pressed()[K_F3]==True:
        selected_background='forest'
    if key.get_pressed()[K_F4]==True:
        selected_background='underwater'
    if key.get_pressed()[K_F5]==True:
        selected_background='sky2'
    if key.get_pressed()[K_F6]==True:
        selected_background='sunset'
    if key.get_pressed()[K_F7]==True:
       selected_background='forest night'
    if key.get_pressed()[K_F8]==True:
       selected_background = 'desert'
    if key.get_pressed()[K_F9]==True:
        selected_background='darkness'

    

##########################################################Other Variables##############


Enemeyreclist=[]
selected_enemey=None


########################

Platformrectlist=[]
selected_texture=None
selected_container=None
Container_rectlist=[]
selected_colour=blue

#############################
Presetrectlist=[]
selected_preset=None

######################
#Main loop


                
Dynamic_Projectiles=twodim(10,6) #looks like [rect,accgravity,intial_v,horizontalmovement]
screenCopy=screen.copy()
selected_tool="platform tool" #tool that they are currently using 
Platforms=[] # list that contains all the platforms that you've made
Enemies=[] # list that contains all the enemies that you've created
Rotodisks=[] #stores rotodisk positions
Presets=[] #stores preset positions 
rotodiskvariable=0

mouse_position="up"
offset=0

projectilevariable=0
runflag=False
myclock=time.Clock()

SPAWNX=400
SPAWNY=100

music_variable=-1
####################################################
######################LOADING###############3

Drawtext( "Welcome to the Mario Level Editor would you like to...",40,(100,100),blue)
Drawtext( "1.)edit a level",40,(600,300),blue)
Drawtext( "2.)create a new level",40,(600,500),blue)
display.flip()
selected_background='forest'
#def inputtext((x,y),length2,width,colour,size,limit)
#def Drawtext(words,size,(x,y),colour)
choice=inputtext((600,700),40,40,pink,50,100)


if int(choice)==1:  #loads all the date you need from file,if you want to know more about how this is done go see the alogorithm
    screen.fill(black)
    Drawtext( "Enter name of file:",40,(100,100),blue)
    display.flip()
    name=inputtext((600,700),40,40,pink,50,100)
    name[0].upper()  #make the "W" captial 
    platform_file=open(name+"platforms.txt","r")
    enemey_file=open(name+"enemies.txt","r")
    roto_file=open(name+"rotodisks.txt","r")
    preset_file=open(name+"presets.txt","r")
    variable_file=open(name+"othervariables.txt","r")
    Presets=cPickle.load(preset_file) #loads presets from data file...
    Platforms=cPickle.load(platform_file)
    Enemies=cPickle.load(enemey_file)
    Rotodisks=cPickle.load(roto_file)
    variable_list=variable_file.readlines()
    pos=variable_list[0].index("a")
    SPAWNX=int(variable_list[0][0:pos])
    SPAWNY=int( variable_list[0][pos+4:])

    x=SPAWNX
    y=SPAWNY
    selected_background=variable_list[1][:-1] #to get rid of the \n
    selected_music=variable_list[2]
    music_variable=musiclist.index(selected_music) #load selected music
    bgm_music(musiclist[music_variable]) #load background 

#print Platforms
########################################################
running=True

while running:


  #  print Presets
    select_background()
    
    drawScene(screen,0,300,selected_background)    
    draw.rect(screen,blue,drawablearea,4) #just draws the rectangle in which you shoudl draw

    
    for evnt in event.get():
        
            
        if evnt.type==KEYDOWN:


            if evnt.key==51: #if they hit 3
                answer=raw_input("would you like to save positions to a data file and run program?")
                if answer=="yes":
                    if runflag==True: #basically "runs" a test of the program
                        runflag=False
                    elif runflag==False:
                        runflag=True



                    name=raw_input("what would you like the file to be called")
                    selected_music=musiclist[music_variable]

                    platform_file=open(name+"platforms.txt","w")
                    enemey_file=open(name+"enemies.txt","w")
                    roto_file=open(name+"rotodisks.txt","w")
                    preset_file=open(name+"presets.txt","w")
                    other_file=open(name+"othervariables.txt","w")
                


                    other_file.write((str(SPAWNX)+"and"+(str(SPAWNY))))
                    other_file.write('\n'+selected_background)
                    other_file.write('\n'+selected_music)
                    cPickle.dump(Enemies,enemey_file)
                    cPickle.dump(Platforms,platform_file)
                    cPickle.dump(Rotodisks,roto_file)
                    cPickle.dump(Presets,preset_file)
                    
    if key.get_pressed()[27]==True:
        running=False
    if key.get_pressed()[K_1]==True:
        selected_tool="platform tool"
    if key.get_pressed()[K_2]==True:
        selected_tool="enemey tool"
    if key.get_pressed()[K_4]==True:
        selected_tool="roto disk tool"

    if key.get_pressed()[K_6]==True:
        selected_tool="preset tool"

    if key.get_pressed()[K_7]==True:
        selected_tool="spawn tool"

    if key.get_pressed()[K_LEFT]==True:
        offset=offset-10
            
    if key.get_pressed()[K_RIGHT]==True:
        offset+=10

    if mouse.get_pressed()[0]==0 and clickflag==True: #indicates if hte mouse is not pressed, we only want one key evnt ins ome cases
        clickflag=False# so this is very useful  
        
    if selected_tool=="spawn tool" and mouse.get_pressed()[0]==1:
        mx,my=mouse.get_pos()
        mx+=offset
        SPAWNX=mx
        SPAWNY=my

    if key.get_pressed()[K_TAB]==True: #variable which controls what music is currently playing and will be playing in the level
        music_variable+=1
        if music_variable==len(musiclist):
            music_variable=0
        name=musiclist[music_variable]
        bgm_music(name)
        
    if runflag==True:
        plat_list=[]
        for i in range(len(Platforms)):
            plat_list.append((Platforms[i][0]))
        movedynamic_enemies(400,300,Enemies)
        move_dynamicprojectiles(400,300)
        Drawplatforms(screen,0,Platforms,400,300)
        drawrotodisk(400,300,Rotodisks)
        
        

    if runflag==False:      
        for i in range(len(Enemies)): #draws enemies
            rect=Enemies[i][1]
            screen.blit(Enemiesdictionary[Enemies[i][0]][0],(Enemies[i][1][0]-offset,Enemies[i][1][1]))

        Drawplatforms(screen,0,Platforms,400,300) #didn't even need the other stuff, jjust draw them here

        drawrotodisk(100,100,Rotodisks) #draw roto disks
        Drawpresets(offset) #draw offsets 

    if selected_tool=="roto disk tool":
       rotodiskcreator()

    if selected_tool=="enemey tool":
        Enemeyreclist=Drawenemeyoptions()
        selected_enemey=make_enemies(selected_enemey)
        
    if selected_tool=="platform tool":
        selected_texture,selected_container=drawplatforms(selected_texture,selected_container)
        Platformrectlist,Container_rectlist=Drawplatformoptions()
        
        
    if selected_tool=="preset tool":
        Presetrectlist=Drawpresetoptions()
        selected_preset=makePresets(offset,selected_preset)

    screen.blit(spawn_image,(SPAWNX-offset,SPAWNY))
    


    display.flip() #display.flip after everything 
    screen.fill(black)
    myclock.tick(60)
   
    

enemey_file.close() #close fliles
platform_file.close()
roto_file.close()
preset_file.close()
other_file.close()
quit()
