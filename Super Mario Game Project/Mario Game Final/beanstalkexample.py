
############Beanstalk example



def beanstalk(px,py,picture,x,y,mx,my,deltax): #try getting a copy of a previous screen....that way mario will still be there
    global screen2
    global Beanstalkflag
    picture=beanstalkimage
  # beanstalklist=[]
  #  previous_screen=screen.copy()
    if Beanstalkflag==False:
        count=0
        for i in range(py,py-300,-32):
            count+=1
            Myrect=Rect(px,i,32,32*count) # rect that controls what can be modified
            screen.set_clip(screen2)
           # drawMario(screen,x,y,standing,False,mx,my,deltax)
            drawFullscene(screen,x,y,mx,my,0)             #draw full scene then blit it
           # screen.blit(previous_screen,(0,0))
            screen.set_clip(Myrect) #increases each time
            screen.blit(picture,(px,i)) #blit the picture
            time.wait(100) #delay
            display.flip() #update
           # screen.fill(black)
            print "testing"
        screen.set_clip(screen2)
       # beanstalklist.append((px,py))
    
