import pygame

pygame.init()

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (150,0,150)
ORANGE = (150,100,0)

size = (700,500)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rect_change_x = 2
rect_change_y = 2

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rect_x += rect_change_x
    rect_y += rect_change_y
     
    if rect_x > 650 or rect_x < 0:
        rect_change_x *= -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y *= -1
    screen.fill((0,0,0))    
    pygame.draw.rect(screen,(255,255,255), (rect_x,rect_y,50,50)) 
    pygame.draw.rect(screen,RED, (rect_x+10,rect_y+10,30,30)) 


    clock.tick(60)
    pygame.display.flip()
pygame.quit()