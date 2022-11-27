import pygame,sys
from pygame.locals import*

#At home, the player is the Zelda character, but when he enters a maze,
#He turns into a square
pygame.mixer.init()

#play music
pygame.mixer.music.load("zelda music.ogg")
pygame.mixer.music.set_volume(0.5)
#play music over and over again
pygame.mixer.music.play(-1)


#display
gamewindow = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Home")

x = 20
y = 20
width = 20
height = 20
YELLOW = (254,249,52)
BLUE = (0,191,255)
velocity = 10
GREEN = (8,242,47)
BROWN = (139,69,19)
width2 = 40
height2 = 40
BLACK = (0,0,0)
WHITE = (255,255,255)

d = 10
e = 10
direction = "right"
for enemi in range(0,5):
    enemi1 = pygame.transform.scale(pygame.image.load("enemi1.png"), (40,40))
    gamewindow.blit(enemi1, (100,100))
#enemi1 = pygame.transform.scale(pygame.image.load("enemi1.png"), (40,40))
#gamewindow.blit(enemi1, (100,100))
#enemi1 = pygame.transform.scale(pygame.image.load("enemi1.png"), (40,40))
#gamewindow.blit(enemi1, (100,100))

while True:
    #pygame.time.speed(5)
    if direction == "right":
        d += 100
        gamewindow.blit(enemi1,(d,80))
        if d == 100:
            direction = "left"
    elif direction == "left":
        d -=100
        gamewindow.blit(enemi1, (d,80))
        if d == 100:
            direction = "right"

    if direction == "right":
        d += 100
        gamewindow.blit(enemi1,(d,150))
        if d == 100:
            direction = "left"
    elif direction == "left":
        d -=100
        gamewindow.blit(enemi1, (d,500))
        if d == 100:
            direction = "right"
    if direction == "right":
        d += 100
        gamewindow.blit(enemi1,(d,100))
        if d == 100:
            direction = "left"
    elif direction == "left":
        d -=100
        gamewindow.blit(enemi1, (d,800))
        if d == 100:
            direction = "right"
    if direction == "right":
        d += 100
        gamewindow.blit(enemi1,(d,130))
        if d == 100:
            direction = "left"
    elif direction == "left":
        d -=100
        gamewindow.blit(enemi1, (d,1500))
        if d == 100:
            direction = "right"
    if direction == "right":
        d += 100
        gamewindow.blit(enemi1,(d,70))
        if d == 100:
            direction = "left"
    elif direction == "left":
        d -=100
        gamewindow.blit(enemi1, (d,2000))
        if d == 100:
            direction = "right"
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #pygame.display.update()

        #Move the shape
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity
        if x<=0: 
            x = 0
        elif x>150 and x<300 and y < 130: #Wall for forest
            x=150
                
    if keys[pygame.K_RIGHT]:
        x += velocity
        if x>=600:
            x=600
        elif x>150 and x<300 and y < 120: #Wall for forest
            x=150
                
    if keys[pygame.K_UP]:
        y -= velocity
        if y<=0:
            y=0
                
    if keys[pygame.K_DOWN]:
        y += velocity
        if y>=600:
            y=600

    background = pygame.transform.scale(pygame.image.load("lawn.jpg"), (600,600))
    gamewindow.blit(background, (0,0))

    for d in range (0,4):
        fence = pygame.transform.scale(pygame.image.load("fence.png"), (70,70))
        gamewindow.blit(fence, (300+d*70,250+d*0))

    house2= pygame.transform.scale(pygame.image.load("house2.png"), (150,150))
    gamewindow.blit(house2, (100,200))
    rockpath= pygame.transform.scale(pygame.image.load("rocks path.png"), (150,150))
    gamewindow.blit(rockpath, (200,250))
    rockpath= pygame.transform.scale(pygame.image.load("rocks path.png"), (150,150))
    gamewindow.blit(rockpath, (310,300))
    house= pygame.transform.scale(pygame.image.load("house.png"), (180,180))
    gamewindow.blit(house, (380,240))

    
    for t in range(0, 7):        
        tree = pygame.transform.scale(pygame.image.load("pine tree.png"), (70,70))
        gamewindow.blit(tree, (200+t*55,0+t*0))

    for i in range(0,10):
        tree = pygame.transform.scale(pygame.image.load("pine tree.png"), (70,70))
        gamewindow.blit(tree, (150+i*55,40+i*0))
        
    for a in range(0,7):
        tree = pygame.transform.scale(pygame.image.load("pine tree.png"), (70,70))
        gamewindow.blit(tree, (200+a*55,80+a*0))
        fence = pygame.transform.scale(pygame.image.load("fence.png"), (70,70))
        gamewindow.blit(fence, (100+a*70,400+a*0))

    for b in range(0,6):
        tree = pygame.transform.scale(pygame.image.load("pine tree.png"), (70,70))
        gamewindow.blit(tree, (280+b*55,120+b*0))

    for c in range(0,4):
        tree = pygame.transform.scale(pygame.image.load("pine tree.png"), (70,70))
        gamewindow.blit(tree, (360+c*55,160+c*0))
        

    zelda = pygame.transform.scale(pygame.image.load("zelda png.png"), (40,40))
    gamewindow.blit(zelda, (x,y))

    
    pygame.display.update()

    
            
