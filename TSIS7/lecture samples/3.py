import pygame

pygame.init()

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (150,0,150)
ORANGE = (150,100,0)

size = (500,500)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
text_rotate = 1

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
    #TEXT ROTATE
    screen.fill((255,255,255))
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Programming Technologies", True,(0,0,0))
    text = pygame.transform.rotate(text, text_rotate)
    screen.blit(text, (100,100))
    text_rotate += 1
    clock.tick(60)
 
    pygame.display.flip()
pygame.quit()