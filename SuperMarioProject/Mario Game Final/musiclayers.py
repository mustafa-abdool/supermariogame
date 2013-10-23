#music example.py


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

mixer.init()


Musicdictionary={}

Musicdictionary["Jump Sound"]="Jump.wav"
Musicdictionary["Game Over"]="Game Over.OGG"
Musicdictionary["Basic Theme"]="World 1.OGG"
Musicdictionary["SMB3 Theme"]="sm3wd3.mid"

#Musiclist=["Jump.wav","Game Over.OGG","World 1.OGG","sm3wd3.mid"]




#####################################################

def changemusic(soundname,channel):
    current_music=mixer.Sound(Musicdictionary[soundname])
    channel.play(current_music)

overworld_music=mixer.Channel(1)
sounds=mixer.Channel(2)


changemusic("Basic Theme",overworld_music)

running=True
while running:
    for evnt in event.get():
         if mouse.get_pressed()[0]==1:
             
        
            changemusic("Jump Sound",sounds)


