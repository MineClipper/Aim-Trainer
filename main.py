import pygame
import random
import time
import os

pygame.init()
disx = 1200
disy = 650
win = pygame.display.set_mode((disx,disy))
pygame.display.set_caption("Aim Trainer")
bg = pygame.image.load('bluecolor.png')
bg = pygame.transform.scale(bg, (disx,disy))
gm = pygame.image.load('gameover.jpg')
gm = pygame.transform.scale(gm, (600,325))
#Variabls
global circlesize
global x
global counter
counter = 0
global missed
missed = 0

def background():
    win.blit(bg, (0,0))
        
def collisions():
    global missed
    global counter
    global centerofcirclex
    global centerofcircley
    global radiusofcircle
    if event.type == pygame.MOUSEBUTTONDOWN:
        if abs(cordsx-centerofcirclex)<=radiusofcircle:
            if abs(cordsy-centerofcircley)<=radiusofcircle:
                background()
                circles()
                counter = counter + 1
            else:
                missed = missed + 1
        else:
            missed = missed + 1
            
            
                
def mouseclicker():
    if event.type == pygame.MOUSEBUTTONDOWN:
        global cordsx
        global cordsy
        cordsx, cordsy = event.pos

def circles():
    global centerofcirclex
    global centerofcircley
    global radiusofcircle
    centerofcirclex = (int(random.randrange(40,1160)))
    centerofcircley = (int(random.randrange(40,610)))
    radiusofcircle = circlesize
    pygame.draw.circle(win,(255,0,0),(centerofcirclex,centerofcircley),radiusofcircle,0)


print("How Big Do you want the circles to be?")
circlesize = int(input())
background()
run = True
x = 1
while run == True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        run = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            background()
            win.blit(gm,(325,175))
            print("Your score was ",counter)
            print("You missed ",missed)

            
    while x == 1:
        circles()
        x = 0
    mouseclicker()
    collisions()
    pygame.display.update()
    

#This Needs to Be the Last Line
pygame.quit()
