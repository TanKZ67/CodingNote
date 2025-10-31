import pygame
import os
os.chdir(os.path.dirname(__file__))
#if not this, when you pygame.image.load, system will start from "C:\Users\Assignment\CodingNote"" not start at "C:Users....\Chapter2\rectangle.py"
#so we need use import os.chdir(os.path.dirname(__file__)
#__file__ means "C:Users....\Chapter2\rectangle.py"
#chdir = change directory


pygame.init()
width=700
height=500
window=pygame.display.set_mode((width,height))#window width and height
pygame.display.set_caption("First Game")#caption
clock=pygame.time.Clock()

walkLeft=[pygame.image.load('../img/L1.png'),pygame.image.load('../img/L2.png'),pygame.image.load('../img/L3.png'),pygame.image.load('../img/L4.png'),pygame.image.load('../img/L5.png'),pygame.image.load('../img/L6.png'),pygame.image.load('../img/L7.png'),pygame.image.load('../img/L8.png'),pygame.image.load('../img/L9.png')]
walkRight=[pygame.image.load('../img/R1.png'),pygame.image.load('../img/R2.png'),pygame.image.load('../img/R3.png'),pygame.image.load('../img/R4.png'),pygame.image.load('../img/R5.png'),pygame.image.load('../img/R6.png'),pygame.image.load('../img/R7.png'),pygame.image.load('../img/R8.png'),pygame.image.load('../img/R9.png')]
char=pygame.image.load('../img/standing.png')
bg=pygame.image.load('../img/bg.jpg')
#load png and jpg

left=False
right=False
walkCount=0

char_width=50
char_height=50
x=((width//2)-(char_width//2))
y=(height//2-(char_height//2))
velocity=5#speed

isJump=False
jumpCount=10
run=True

def refreshWindow():
    window.blit(bg,(0,0))#Block Level Image Transfer(put image on window)
    global walkCount
    if walkCount+1>=27:#this is because frame, need to take care about next code which is walkCount+=1 because walkCount is start from 0, until 26 already 27 frame.This walkCount+1>=27 is same as walkCount==26 but former is more ezy to the programmer to underestand what the code are representing
        walkCount=0
    
    if left:
        walkCount+=1
        window.blit(walkLeft[walkCount//3],(x,y))#use //3 is because frame(a picture use in 3 frame)
    elif right:
        walkCount+=1
        window.blit(walkRight[walkCount//3],(x,y))
    else:
        window.blit(char,(x,y))

    pygame.display.update() #update what is going on(x,y,background......)

while run:#main loop
    clock.tick(27)
    pygame.time.delay(20) #lzy explain ask me by personal
    for event in pygame.event.get(): #track user keyboard and mouse record in event(use event)
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed() #track user keyboard and mouse record in event(use key(different ask me personal))
    if keys[pygame.K_LEFT] and x>=velocity: #left
        x-=velocity
        left=True
        right=False

    if keys[pygame.K_RIGHT] and x<width-char_width: #right
        x+=velocity
        left=False
        right=True

    if not isJump:    #check is jump or not, if is jump we can't move up， down and jump
        if keys[pygame.K_UP] and y >= velocity: #up
            y-=velocity
            left=0
            right=0

        if keys[pygame.K_DOWN] and y < height-char_height: #down
            y+=velocity
            left=0
            right=0
        
        if keys[pygame.K_SPACE]: #jump
            isJump=True
    else: 
        if jumpCount>=-10: #all is formula of gravity
            neg =1
            if jumpCount<0:
                neg = -1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
     
    refreshWindow()



print("byebye")
pygame.quit()