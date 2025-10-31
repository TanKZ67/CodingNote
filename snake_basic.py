import pygame

pygame.init()
width=700
height=500
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")


char_width=50
char_heigth=50
x=((width//2)-(char_width//2))
y=(height//2-(char_heigth//2))
velocity=5

isJump=True
jumpCount=10
run=True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>=velocity:
        x-=velocity
    if keys[pygame.K_RIGHT] and x<width-char_width:
        x+=velocity
    if not isJump:    
        if keys[pygame.K_UP] and y >= velocity:
            y-=velocity
        if keys[pygame.K_DOWN] and y < height-char_heigth:
            y+=velocity
        if keys[pygame.K_SPACE]:
            isJump=True
    else: 
        if jumpCount>=-10:
            neg =1
            if jumpCount<0:
                neg = -1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
     

    window.fill((0,0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,char_heigth,char_width))
    pygame.display.update()


print("byebye")
pygame.quit()