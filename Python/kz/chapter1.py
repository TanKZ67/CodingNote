import pygame

pygame.init()
width=700
height=500
window=pygame.display.set_mode((width,height))#window width and height
pygame.display.set_caption("First Game")#caption


char_width=50
char_heigth=50
x=((width//2)-(char_width//2))
y=(height//2-(char_heigth//2))
velocity=5

isJump=False
jumpCount=10
run=True

while run:#main loop
    pygame.time.delay(20) #lzy explain ask me by personal
    for event in pygame.event.get(): #track user keyboard and mouse record in event(use event)
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed() #track user keyboard and mouse record in event(use key(different ask me personal))
    if keys[pygame.K_LEFT] and x>=velocity: #left
        x-=velocity
    if keys[pygame.K_RIGHT] and x<width-char_width: #right
        x+=velocity
    if not isJump:    #check is jump or not, if is jump we can't move up and down and jump
        if keys[pygame.K_UP] and y >= velocity: #up
            y-=velocity
        if keys[pygame.K_DOWN] and y < height-char_heigth: #down
            y+=velocity
        if keys[pygame.K_SPACE]:
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
     

    window.fill((0,0,0)) #fill the entire window with (color)
    pygame.draw.rect(window,(255,0,0),(x,y,char_width,char_heigth)) #draw character name as rect in window surface
    pygame.display.update() #update what is going on(x,y,background......)


print("byebye")
pygame.quit()