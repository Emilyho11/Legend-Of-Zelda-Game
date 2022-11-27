import os
import random
import pygame
import time
from pygame.locals import*

pygame.mixer.init()
white = 255, 255, 255
#play music
pygame.mixer.music.load("zelda music.ogg")
pygame.mixer.music.set_volume(0.5)
#play music over and over again
pygame.mixer.music.play(-1)

    
# Create player
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(20, 20, 20, 20)

    def move(self, length, width):
        
# Check for collisions.
        if length != 0:
            self.moving(length, 0) 
        if width != 0:
            self.moving(0, width)
    
    def moving(self, length, width):
        
        # Move the rect
        self.rect.x += length
        self.rect.y += width

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if length > 0: # Moving right and hit the left side of the wall
                    self.rect.right = wall.rect.left
                if length < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if width > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if width < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)

# Initialise pygame
os.environ["Zelda Game"] = "1"
pygame.init()

# Set up the display
displaywidth = 600
displayheight = 600
pygame.display.set_caption("Level 3")
gamewindow = pygame.display.set_mode((displaywidth, displayheight))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W  W                                W",
"W  W                                W",
"W  WWWWW  W     WWWWWW  WWWW  W     W",
"W         W     W         W   WWWWWWW",
"W         W     W         W   W     W",
"W  WWWWWWWW     W         W   W     W",
"W  W         WWWW         W   W     W",
"W  W         W            W   WWWW  W",
"W  W     WWWWW            W         W",
"W        W       WWWWWWWWWW         W",
"W        W       W                  W",
"W        W       W            WWWW  W",
"W  W     W       W            W     W",
"W  W     W       W            W     W",
"W  W     W       W            W     W",
"W  W     W       W            W     W",
"W  W     W       W   WWWWWWWWWWWW   W",
"W  W     W       W   W          W   W",
"WWWWWWWWWW    WWWW   W          W   W",
"W                W   WWWWWWW    W   W",
"W                W   W     W    W   W",
"W        W       W   W     W    W   W",
"W        W       W   W     W    W   W",
"W        W       W   W     W    W   W",
"W        WWWWWWWWW         W    W   W",
"W                          W    WWWWW",
"W                     WWWWWW        W",
"W   WWWWWWWWW         W             W",
"W   W                 W             W",
"W   W             WWWWWWWWWWWWW     W",
"W   W             W      W          W",
"W                 W      W          W",
"W      WWWWWWWWWWWW      W          W",
"W                                   W",
"W                                   E",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# W = wall, E = exit
x =0
y = 0
for row in level:
    for letter in row:
        if letter == "W":
            Wall((x, y))
        if letter == "E":
            exitsquare = pygame.Rect(x, y, 20, 20)
        x += 16
    y += 16
    x = 0
    
'''
    #change screen
def fade():
    fade = pygame.surface((600,600))
    fade.fill((0,0,0))
    for alpha in range (0,300):
        fade.set_alpha(alpha)
        redrawWindow()
        gamewindow.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawWindow():
    win.fill((255,255,255))
    pygame.draw.rect(gamewindow,(255,0,0),(200,300,200,200), 0)
    pygame.draw.rect(gamewindow,(0,255,0),(500,500,100,200), 0)

    if self.rect > gamewidow:
        gamewindow.fade
        gamewindow.redrawWindow
'''
running = True
while running:
    
    clock.tick(500)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        #speed of the player
        player.move(-10, 0)
    if key[pygame.K_RIGHT]:
        player.move(10, 0)
    if key[pygame.K_UP]:
        player.move(0, -10)
    if key[pygame.K_DOWN]:
        player.move(0, 10)
    
    # Draw the scene
    background = pygame.transform.scale(pygame.image.load("dirt.png"), (600,600))
    gamewindow.blit(background, (0,0))
    treasure = pygame.transform.scale(pygame.image.load("treasure.png"), (25,25))
    gamewindow.blit(treasure, (400,350))
    treasure = pygame.transform.scale(pygame.image.load("treasure.png"), (25,25))
    gamewindow.blit(treasure, (540,380))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (400,400))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (360,295))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (110,280))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (70,120))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (510,105))
    coin = pygame.transform.scale(pygame.image.load("coin.png"), (20,20))
    gamewindow.blit(coin, (245,370))
    treasure = pygame.transform.scale(pygame.image.load("treasure.png"), (30,30))
    gamewindow.blit(treasure, (100,480))                    

        
    for wall in walls:
        pygame.draw.rect(gamewindow, (192,192,192), wall.rect)
        pygame.draw.rect(gamewindow, (255, 0, 0), exitsquare)
        pygame.draw.rect(gamewindow, (135,206,250), player.rect)

        
    pygame.display.flip()
'''
#message on the screen
WHITE = (255,255,255)
font = pygame.font.Sys.Font(None, 25) #25 is the size
    
def messagescreen(message,colour):
    screentext = font.render(message, True, colour)
    gamewindow.blit(screentext, [displaywidth/2,displayheight/2])
    
messagescreen("Level 1", WHITE)
pygame.display.update()
time.sleep(2)
'''

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()