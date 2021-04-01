import pygame

size = width, height = (300,400)
screen = pygame.display.set_mode(size)

screen.fill((150,100,0))
pygame.draw.rect(screen,(150,0,150),(20,30,100,100), 5)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
pygame.quit()