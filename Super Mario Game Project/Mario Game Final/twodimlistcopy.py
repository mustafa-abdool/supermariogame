from pygame import *


def twodim(row,col):
    list1=[]
    for i in range(row):
        temp=[]
        for j in range(col):
            temp.append(None)
        list1.append(temp)
    return list1



def twodimcopy(twodlist):
    length1=len(twodlist)
    length2=len(twodlist[0])
    new=twodim(length1,length2)
    for i in range(len(twodlist)):
        for j in range(len(twodlist[i])):
            value=twodlist[i][j]
            if j==1:
                value=Rect(twodlist[i][j][0],twodlist[i][j][1],twodlist[i][j][2],twodlist[i][j][3])
            new[i][j]=value
    return new


DEFAULTS=[["koopa",Rect(450,300,32,48),2,(32,48),-15,1.5,0,"alive",False,False,50,1,77,2,"parabolic",False,0,200,False,0]]


Enemies=[["bowser",Rect(450,300,102,102),2,(102,102),-15,1.5,0,"alive",False,False,50,1,13,2,"parabolic",False,0,200,False,0]]

