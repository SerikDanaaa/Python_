import pygame
pygame.init()

size = (500,500)
screen = pygame.display.set_mode(size)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (150,0,150)
ORANGE = (150,100,0)


screen.fill((255,255,255))
PI = 3.14

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #line
    pygame.draw.line(screen,GREEN,[0,0],[100,100],5)   

    for i in range(0,100,10):
        pygame.draw.line(screen, RED, [0,10+i],[100,110+i],2)
    
    #rectangle
    pygame.draw.rect(screen,(0,0,0),[20,20,100,50],2)

    #ellipse
    pygame.draw.ellipse(screen,BLUE,[20,100,100,50],2)
    
    #arca
    pygame.draw.arc(screen,PINK,[20,20,100,50],PI/2,PI,2)
    pygame.draw.arc(screen,GREEN,[20,20,100,50],0, PI/2,2)
    pygame.draw.arc(screen,RED,[20,20,100,50],PI, 3*PI/2,2)
    pygame.draw.arc(screen,BLUE,[20,20,100,50],3*PI/2,2*PI,2)
    
    #TEXT ROTATE
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Programming Technologies", True, (0,0,0))
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, (0, 100))
    font1 = pygame.font.SysFont('Calibri', 25, True, False)
    text1 = font.render("Programming Technologies", False,(0,0,0))
    text1 = pygame.transform.rotate(text1, 90)
    screen.blit(text, (50, 100))
 

    pygame.display.flip()
pygame.quit()