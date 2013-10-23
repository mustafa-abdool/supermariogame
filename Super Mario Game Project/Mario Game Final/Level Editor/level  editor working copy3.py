# Level Editor

#just get textures and stuff


#CHECK IF THINGS CAN BE SEEN BEFORE YOU DRAW THEM...JUST LIKE IN THE REAL GAME.....aishh so much to do 

# A way to edit, make, and create levels all by yourself
# Save to data file, then read from it
# Use pickle (mmm I love pickles)


#use left/right keys to change offest
#always add offset
#SCREW screen.copy(), we have to draw everything agiann aishhh (as mommy would say!)
#RED MEANS PLATFORM CAN MOVEEE


#ALLOW THEM TO PUT IN A BACKGROUND

#Enemies

#when making enemies just ask for the enemey that they wan't dont bother w/ variables and stuffff

#something else for moving platforms


from pygame import*
from random import*
from colours import *
from marioworkingcopy50 import *




init()
size=width,height=1000,600
screen=display.set_mode(size)

#############################
Scenerydictionary={}
Scenerydictionary["block 1"]=image.load("Block World 1.PNG")
Scenerydictionary["grass"]=image.load("Grass Middle.PNG")
Scenerydictionary["cloud"]=image.load("Cloud.PNG")
Scenerydictionary["question block"]=image.load("Question Block 1.PNG")
Scenerydictionary["empty block"]=image.load("Empty Block.PNG")
Scenerydictionary['trampoline']=image.load("trampoline.PNG")
Scenerydictionary['moving platform']=image.load("Platform Large.PNG")
#############################
Enemeydict={} #dictionary that contains enemey values

Enemeydict['bowser']=["bowser",Rect(450,300,102,102),2,(102,102),-15,1.5,0,"alive",False,False,50,1,13,2,"parabolic",False,0,200,False,0]
Enemeydict['koopa']=["koopa",Rect(450,300,32,48),2,(32,48),-15,1.5,0,"alive",False,False,301,1,301,1,"parabolic",True,0,200,True,0]
Enemeydict['jumping koopa']=["koopa",Rect(450,300,32,48),2,(32,48),-15,1.5,0,"alive",False,False,50,1,301,1,"parabolic",True,0,200,True,0]
Enemeydict['koopa fast']=["koopa",Rect(450,300,32,48),5,(32,48),-15,1.5,0,"alive",False,False,301,1,301,1,"parabolic",True,0,200,True,0]
#Enemeydict['

#############################
Enemiesdictionary={} #dictionary that stores enemies names/pictures

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

###########################################################

def enemey_prompt(x,y):
    Enemey_list=["bowser","koopa","goomba"] #put in moving/jumping/etc 
    print """Here are your choices of enemies 
        1.) Bowser
        2.) Koopa
        3.) Goomba"""
    enemey_choice=input("enter your choice")
    enemey=(Enemeydict[Enemey_list[enemey_choice-1]])[:] # have to make a copy of hte list, or else the rect object will be overwritten
    value=Rect(x,y,enemey[3][0],enemey[3][1]) #then you change w/e the coordinates of the top left corner were to x,y
    enemey[1]=value # set to value...don't know if this makes a difference??
    return enemey
    

def platformprompt(list1): #pass in the list and then return it, basically prompts and asks them for the platform attributes
    platform_types=["block 1","grass","cloud","question block","empty block","trampoline","moving platform"] #contains all the choices
    containers=["mushroom","flower","hammer","coin","None"]
    movement_choices=[True,False]
    
    print """These are your texture choices
            1.)block 1
            2.)grass
            3.)cloud
            4.)question block
            5.)empty block
            6.)trampoline
            7.)moving platform"""
    platform_type_choice=input("enter your choice")
    platform_type=platform_types[platform_type_choice-1]
    list1.append(platform_type) #HAVE TO MAKE COIN WORK IN THE ACUTAL ALGORIHTM
    print """What do you want to the block to contain
            1.)mushroom
            2.)flower
            3.)hammer
            4.)coin 
            5.) None"""
    container_type_choice=input("enter your choice")
    container_type=containers[container_type_choice-1]
    list1.append(container_type)

    print """Do you want your platform to be moving?
            1.) Yes
            2.) No"""
    movement_type_choice=input("enter your choice")
    movement_type=movement_choices[movement_type_choice-1]
    list1.append(movement_type)

    #TRAMPOLINE'S CAN'T MOVE...OR CAN THEY?!?...fix this/or at least think about it 

    if movement_type==True:
            up_down=input("how fast do you want it to move up/down") #can't move both directions!!
            list1.append(up_down)
            left_right=input("how fast do you want it move left/right")
            list1.append(left_right)
            acc_movement=0
            list1.append(acc_movement)
            limit=input("how far do you want it to be able to move before it stops")
            list1.append(limit)
    else:
        list1.append(0)
        list1.append(0)
        list1.append(0)
        list1.append(0)
    return list1
    

def getMouse():
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()[0]
    return mx,my,mb

def make_enemies():
    if mouse.get_pressed()[0]==1:
        x,y=mouse.get_pos()
        x=x+offset
        enemey=enemey_prompt(x,y) #prompts what enemey you want...allows you to select them and what not
        Enemies.append(enemey)

def divisible32(n): #we wnat to round it off to 32, so it doesn't like 
	remainder=n%32
	if remainder>=16:
		remainder=32-remainder
		n+=remainder
	else:
		n=n-remainder
	return n

        
 
def drawplatforms(selected_colour,offset): #BE ABLE TO INCREASE/RETURN OFFSET HEREEE
    mouse_status="up"
    if mouse.get_pressed()[0]==1:
        x,y=mouse.get_pos()
        x=x+offset
        previous_screen=screen.copy() #gets what it looks like before I start drawing stuff
        mouse_status="down"
        while mouse_status=="down":
            screen.blit(previous_screen,(0,0))
            event.get()

            mx,my=mouse.get_pos()
            mx=mx+offset
            delta_x=mx-x
            if delta_x<0:
                delta_x=delta_x*(-1) #we don't want it to be negative, so if it is we make it positive
            delta_y=my-y
            if delta_y<0: #find the change in the y values
                delta_y=delta_y*(-1)
            if mx<x and my<y: #draw a rectangle to the TOP LEFT
                last_rect=Rect(x-delta_x,y-delta_y,delta_x,delta_y) #REMEMBERS WHAT THE RECTANGLE IS , maybe just subtract offsets here
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2) #have to subtract offsets
            if mx>x and my<y: #draws a rectangle to the BOTTOM RIGHT
                last_rect=Rect(x,y-delta_y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
            if mx>x and my>y: #BOTTOM LEFT
                last_rect=Rect(x,y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
            if mx<x and my>y: #TOP RIGHT
                last_rect=Rect(x-delta_x,y,delta_x,delta_y)
                draw.rect(screen,selected_colour,Rect(last_rect[0]-offset,last_rect[1],last_rect[2],last_rect[3]),2)
            display.flip()
            if mouse.get_pressed()[0]==0 and mouse_status=="down":
                mouse_status="up"
                last_rect[2]=divisible32(last_rect[2]) #to make it even, for him to walk on
                last_rect[3]=divisible32(last_rect[3]) #see above =P
                
                if last_rect[2]!=0 and last_rect[3]!=0: #if its zero that means that they drew it too small and I don't care 
                    list1=[] # list that holds the platform and other information that you have to input, 
                    list1.append(last_rect) #just prompts for other information
    
                    newlist=platformprompt(list1)
                    
                    
                    Platforms.append(newlist) #ADDS THE RECTANGLE THAT YOU JUST DREW TO THE LIST, YO

# [Rect,"texture","contains",movefflag,updown/movemen,leftright/movement,accmovement,limit]               
                
#for drawing platforms...
#but we have to check offests for this too!! don't forget

            
        
            #    for p in range(newplat[1],newplat[1]+newplat[3]-1,32):#goes through all y values...
              #      for j in range(newplat[0],newplat[0]+newplat[2]-1,32): # then go through and blit the appropirate texture
                #         screen.blit(Scenerydictionary[bothplatforms[i][1]],(j,p)) #minus makes it go higher, plus makes it go lower    
    


#Main loop

screenCopy=screen.copy()
selected_tool="platform tool"
Platforms=[] # list that contains all the platforms that you've made
Enemies=[] # list that contains all the enemies that you've created
mouse_position="up"
selected_colour=blue
offset=0

running=True
while running:
    
    event.get()
    print "running"
    if key.get_pressed()[K_1]==True:
        selected_tool="platform tool"
    if key.get_pressed()[K_2]==True:
        selected_tool="enemey tool"
    
    if key.get_pressed()[K_LEFT]==True:
        offset=offset-10
        
    if key.get_pressed()[K_RIGHT]==True:
        offset+=10
        
    for i in range(len(Platforms)): #draws platforms 
        newplat=Platforms[i][0]
        #if Platforms[i][3]==True:
         #   draw.rect(screen,red,Rect(rect[0]-offset,rect[1],rect[2],rect[3]),2) #have to subtract offsets
        #else:
         #  draw.rect(screen,blue,Rect(rect[0]-offset,rect[1],rect[2],rect[3]),2) #have to subtract offsets
        for p in range(newplat[1],newplat[1]+newplat[3]-1,32):#goes through all y values...
            for j in range(newplat[0],newplat[0]+newplat[2]-1,32): # then go through and blit the appropirate texture
                screen.blit(Scenerydictionary[Platforms[i][1]],(j-offset,p)) #minus makes it go higher, plus makes it go lower 
           
    for i in range(len(Enemies)): #draws enemies
        rect=Enemies[i][1]
        screen.blit(Enemiesdictionary[Enemies[i][0]],(Enemies[i][1][0]-offset,Enemies[i][1][1]))
   #     draw.rect(screen,pink,Rect(rect[0]-offset,rect[1],rect[2],rect[3]),2) #have to subract offsets 

    if selected_tool=="enemey tool":
        make_enemies()
    if selected_tool=="platform tool":
        drawplatforms(selected_colour,offset)
        
    display.flip() #display.flip after everything 
    screen.fill(black)
    
    
