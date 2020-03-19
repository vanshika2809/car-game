


import pygame
import time
import sys
import random
pygame.init()

gray=(119,118,110)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,255)
bright_red=(255,0,0)
bright_green=(0,255,0)
window_width=800
window_height=600
A=[]

G=pygame.display.set_mode((window_width,window_height))
cimg=pygame.image.load('yellow strip.jpg')
C1=pygame.transform.scale(cimg,(100,100))
clock=pygame.time.Clock()
def load(name,xp,yp):
    v = pygame.image.load(name)
    G.blit(v, (xp, yp))
    pygame.display.update()
def message(m,colour,size,x,y):
     font=pygame.font.SysFont(None,size)
     screen_text=font.render(m,True,colour)
     G.blit(screen_text,(x,y))
     pygame.display.update()

def button(x,y,w,h,m,m_color,actc,noc,size,tx,ty,func):
    mouse = pygame.mouse.get_pos()
    click=  pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:

        pygame.draw.rect(G, actc, [x, y, w, h])
        message(m, m_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func()

    else:
        pygame.draw.rect(G, noc, [x, y, w, h])
        message(m, m_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()
def quit1():
    pygame.quit()
    quit()

def game_intro():
  load('background1.jpg', 0, 0)
  gameintro=False
  while gameintro==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameintro = True
            game_over=True

    window_width = 800
    window_hight = 600


    message('MAIN MENU',green,100,(window_width/2 - 220),100)
    button(100, 400, 70, 30, 'GO!', white, bright_red, red,25,106,406,gameloop)
    button(600, 400, 70, 30, 'QUIT', white, bright_green, green,25,606,406,quit1)

    pygame.display.update()



  pygame.display.update()

def back():
    blue_strip=pygame.image.load('download12.jpg')
    img=pygame.transform.scale(blue_strip,(100,600))
    G.blit(img,(0,0))
    G.blit(img,(700,0))
def crash(x):
    if 90>x  or x+90>700:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('game_over', True, white)
        G.blit(screen_text, (250, 280))
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def car_crash(x,y,y_en,x_en):

    if x<x_en+57<x+150 and (y<y_en+100<y+100 or y<y_en<y+100):
        message('CRASHED!', red, 100, 250, 280)
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()




def score(count):
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('score :' + str(count), True, white)
    G.blit(screen_text, (0, 0))
    pygame.display.update()

def other_car(y_en):
    enmy1=pygame.image.load('car3.jpg')
    enmy=pygame.transform.scale(enmy1,(70,100))
    global  x_en
    if y_en==0:
      x_en=random.randrange(100,600)
      A.clear()
      A.append(x_en)
    else:
      x_en=A[0]
    G.blit(enmy,(x_en,y_en))
    pygame.display.update()


def gameloop():

     x = 300
     y = 400
     x_change = 0
     y_change = 0
     global game_over
     game_over=False

     count = 0
     y_en=0
     while game_over==False:
         for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     game_over=True
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_LEFT:
                         x_change=-10
                     elif event.key==pygame.K_RIGHT:
                         x_change=+10
                 if event.type==pygame.KEYUP:
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                         x_change=0

         x+=x_change


         G.fill(gray)

         back()
         G.blit(G, (x, y))
         if y_en>600:
           y_en=0
           count += 1
         other_car(y_en)
         y_en+=10
         crash(x)
         car_crash(x,y,y_en,x_en)
         score(count)



         clock.tick(30)
         pygame.display.update()


game_intro()
pygame.quit()
quit()
        
