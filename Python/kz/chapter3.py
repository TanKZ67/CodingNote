import pygame
import os
os.chdir(os.path.dirname(__file__))
#if not this, when you pygame.image.load, system will start from "C:\Users\Assignment\CodingNote"" not start at "C:Users....\Chapter2\rectangle.py"
#so we need use import os.chdir(os.path.dirname(__file__)
#__file__ means "C:Users....\Chapter2\rectangle.py"
#chdir = change directory


pygame.init()
width=850
height=450
window=pygame.display.set_mode((width,height))#window width and height
pygame.display.set_caption("First Game")#caption
clock=pygame.time.Clock()

walkLeft=[pygame.image.load('img/L1.png'),pygame.image.load('img/L2.png'),pygame.image.load('img/L3.png'),pygame.image.load('img/L4.png'),pygame.image.load('img/L5.png'),pygame.image.load('img/L6.png'),pygame.image.load('img/L7.png'),pygame.image.load('img/L8.png'),pygame.image.load('img/L9.png')]
walkRight=[pygame.image.load('img/R1.png'),pygame.image.load('img/R2.png'),pygame.image.load('img/R3.png'),pygame.image.load('img/R4.png'),pygame.image.load('img/R5.png'),pygame.image.load('img/R6.png'),pygame.image.load('img/R7.png'),pygame.image.load('img/R8.png'),pygame.image.load('img/R9.png')]
char=pygame.image.load('img/standing.png')
bg=pygame.image.load('img/bg.jpg')
#load png and jpg

class character():
    def __init__(self,char_width,char_height,x,y,velocity):
        self.char_height=char_height
        self.char_width=char_width
        self.x=x
        self.y=y
        self.velocity=velocity
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0

    def draw(self,window):
        if self.walkCount+1>=27:#this is because frame, need to take care about next code which is walkCount+=1 because walkCount is start from 0, until 26 already 27 frame.This walkCount+1>=27 is same as walkCount==26 but former is more ezy to the programmer to underestand what the code are representing
            self.walkCount=0
        
        if self.left:
            self.walkCount+=1
            window.blit(walkLeft[self.walkCount//3],(self.x,self.y))#use //3 is because frame(a picture use in 3 frame)
        elif self.right:
            self.walkCount+=1
            window.blit(walkRight[self.walkCount//3],(self.x,self.y))
        else:
            window.blit(char,(self.x,self.y))


def refreshWindow():

    window.blit(bg,(0,0))#Block Level Image Transfer(put image on window)
    player.draw(window)
    pygame.display.update() #update what is going on(x,y,background......)
    

player=character(100,100,((width//2)-(300//2)),(height//2-(300//2)),10)    
run=True
while run:#main loop
   
    clock.tick(27)
    pygame.time.delay(20) #lzy explain ask me by personal
    
    for event in pygame.event.get(): #track user keyboard and mouse record in event(use event)
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed() #track user keyboard and mouse record in event(use key(different ask me personal))
    if keys[pygame.K_LEFT] and player.x>=player.velocity: #left
        player.x-=player.velocity
        player.left=True
        player.right=False

    if keys[pygame.K_RIGHT] and player.x<width-player.char_width: #right
        player.x+=player.velocity
        player.left=False
        player.right=True

    if not player.isJump:    #check is jump or not, if is jump we can't move up， down and jump
        if keys[pygame.K_UP] and player.y >= player.velocity: #up
            player.y-=player.velocity
            player.left=False
            player.right=False

        if keys[pygame.K_DOWN] and player.y < height-player.char_height: #down
            player.y+=player.velocity
            player.left=False
            player.right=False
        
        if keys[pygame.K_SPACE]: #jump
            player.isJump=True
    else: 
        if player.jumpCount>=-10: #all is formula of gravity
            neg =1
            if player.jumpCount<0:
                neg = -1
            player.y-=(player.jumpCount**2)*0.5*neg
            player.jumpCount-=1
        else:
            player.isJump=False
            player.jumpCount=10
     
    refreshWindow()



print("byebye")
pygame.quit()