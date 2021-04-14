import pygame
import random

pygame.init()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_OF_BALLS = 0

screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")

background = pygame.Surface((400,600))
image = pygame.image.load('road1.png')
background.blit(image,(0,0))

class enemy:
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemyyyy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))




done = False

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
    screen.blit(background,(0,0))
    pygame.display.flip()

pygame.quit()                