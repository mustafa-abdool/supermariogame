# Level Editor

# A way to edit, make, and create levels all by yourself
# Save to data file, then read from it
# Use pickle (mmm I love pickles)


#use left/right keys to change offest
#always add offset
#SCREW screen.copy(), we have to draw everything agiann aishhh
#RED MEANS PLATFORM CAN MOVEEE


from pygame import*
from random import*
from colours import *




init()
size=width,height=600,600
screen=display.set_mode(size)

#############################

#def platformprompt(list1): #pass in the list and then return it 
    

def getMouse():
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()[0]
    return mx,my,mb
 
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
                list1=[] # list that holds the platform and other information that you have to input, 
                list1.append(last_rect) #just prompts for other information

             #   platformstuff=platformprompt(list1)
                
                texture=raw_input("what texture for platform") #MAKE SURE OF INPUT/RAW INPUT
                list1.append(texture)
                container=raw_input("what do you want to platform to contain")
                list1.append(container)
                moving=raw_input("do you want the platform to move Enter True/False please")
                list1.append(moving)
               # if moving==True: #only ask if its true...blah blah 
                up_down=input("how fast do you want it to move up/down") #can't move both directions!!
                list1.append(up_down)
                left_right=input("how fast do you want it move left/right")
                list1.append(left_right)
                acc_movement=0
                list1.append(acc_movement)
                limit=input("how far do you want it to be able to move before it stops")
                list1.append(limit)
                
                
                Platforms.append(list1) #ADDS THE RECTANGLE THAT YOU JUST DREW TO THE LIST, YO

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
mouse_position="up"
selected_colour=blue
offset=0

running=True
while running:
    
    event.get()
    print Platforms
    
    if key.get_pressed()[K_LEFT]==True:
        offset=offset-10
        
    if key.get_pressed()[K_RIGHT]==True:
        offset+=10
        
    for i in range(len(Platforms)):
        rect=Platforms[i][0]
        if Platforms[i][3]==True:
            draw.rect(screen,blue,Rect(rect[0]-offset,rect[1],rect[2],rect[3]),2) #have to subtract offsets
        else:
           draw.rect(screen,red,Rect(rect[0]-offset,rect[1],rect[2],rect[3]),2) #have to subtract offsets 
        
    if selected_tool=="platform tool":
        drawplatforms(selected_colour,offset)
        
    display.flip() #display.flip after everything 
    screen.fill(black)
    
    
