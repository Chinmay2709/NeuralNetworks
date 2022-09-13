#Discription:
#    This is my little gaming environment I made for my Neural Network to play and learn a ball game,
#    where it has to figure out a way to collect the cirlcle that pops on the map at a random position.
#    I think it's little broken now.
#    Refer Log.py for the Neural Code.
#Author:
#    Chinmay Mishra
#Date:
#    Some time unknown: I started recording my coding progress late.



import random
import numpy as np
import sys
import pygame as pyg
import log as NN

pyg.init()
pyg.font.init()



point=0
x=300
y=580
white=(255,255,255)
speed=0.1
jump_speed=0.1
screen=pyg.display.set_mode((600,600))
cyclone=pyg.image.load("C:/Users/Chinmay/Documents/Learn_python/pyhton/cyclone.png")
ball=pyg.image.load("C:/Users/Chinmay/Documents/Learn_python/pyhton/soccerball.png")
ball=pyg.transform.scale(ball,(20,20))
my_font=pyg.font.SysFont('Comic Sans MS', 15)
sury=my_font.render('',False,(0,0,0))
surx=my_font.render('',False,(0,0,0))
targetx=my_font.render('',False,(0,0,0))
targety=my_font.render('',False,(0,0,0))
pointdisp=my_font.render('',False,(0,0,0))
class display():
    def __init__(self,input_up,input_bottom,input_left,input_rigth):
        self.T_inputes=my_font.render('FRONT: '+str(input_up),False,(0,0,0))
        self.B_inputes=my_font.render('BOTTOM: '+str(input_bottom),False,(0,0,0))
        self.L_inputes=my_font.render('LEFT: '+str(input_left),False,(0,0,0))
        self.R_inputes=my_font.render('RIGHT: '+str(input_rigth),False,(0,0,0))
        self.Inputs=np.array([input_up,input_bottom,input_left,input_rigth],dtype=float)
while 1:
    mind=NN.NeuralNetwork()
    cyclonex=random.randint(1,579)
    cycloney=random.randint(1,579)
    check_rect=pyg.Rect((cyclonex,cycloney,30,30))
    cyclone=pyg.transform.scale(cyclone,(check_rect.width,check_rect.height))
    while 1:
        #mind=NN.NeuralNetwork()
        senses=display((y+1),(y-1),(x-1),(x+1))
        ball_rect=pyg.Rect(x,y,20,20)
        gravity=0.019
        for event in pyg.event.get():
            if event.type==pyg.QUIT:
                sys.exit()
        move=mind.forward(X=(np.array([x+1,x-1,y+1,y-1])),Target=np.array([cyclonex,cyclonex,cycloney,cycloney]))
        print('Movement\n', move)
        if move[0]<=1 and move[1]>0.5 and x<580:
            x+=1
        elif move[1]<=1 and move[0]>0.5 and x>0:
            x-=1
        elif move[2]<=1 and move[3]>0.5 and y>0:
            y-=1
        elif move[3]<=1 and move[2]>0.5 and y<580:
            y+=1
        elif y<580:
            y+=gravity
        if check_rect.collidepoint(x,y):
            point+=1
            break
        sury=my_font.render('Y POS: '+str(y),False,(0,0,0))
        surx=my_font.render('X POS: '+str(x),False,(0,0,0))
        targetx=my_font.render('Target POS X:'+str(cyclonex),False,(0,0,0))
        targety=my_font.render('Target POS Y:'+str(cycloney),False,(0,0,0))
        pointdisp=my_font.render('Points: '+str(point),False,(0,0,0))
        screen.fill(white)
        screen.blit(ball,(x,y))
        screen.blit(cyclone,(cyclonex,cycloney))
        screen.blit(sury,(1,1))
        screen.blit(surx,(1,20))
        screen.blit(targetx,(1,40))
        screen.blit(targety,(1,60))
        screen.blit(pointdisp,(1,80))
        screen.blit(senses.T_inputes,(1,100))
        screen.blit(senses.B_inputes,(1,120))
        screen.blit(senses.L_inputes,(1,140))
        screen.blit(senses.R_inputes,(1,160))
        pyg.display.update()    













