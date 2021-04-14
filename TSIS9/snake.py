import pygame, random,sys
from pygame.math import Vector2

pygame.init()

cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (255,255,100)

class FOOD:
    def __init__(self):
        self.randomize()
    
    def Draw_Food(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        food_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size)
        pygame.draw.rect(screen,(RED), food_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number)
        self.y = random.randint(0,cell_number)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def Draw_Snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * cell_size),int(block.y * cell_size), cell_size,cell_size)
            pygame.draw.rect(screen,(BLUE), snake_rect)
    
    def Move_Snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.Move_Snake()  
        self.check_collision()
        self.fail()

    def draw_elements  (self):
        self.food.Draw_Food()
        self.snake.Draw_Snake()
    
    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()

    def fail(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:    
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()  
        
    def game_over(self):
        pygame.quit()
        sys.exit()  


main = MAIN()

done = False

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,200)

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == SCREEN_UPDATE:
                main.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main.snake.direction.y != 1:
                        main.snake.direction = Vector2(0,-1) 
                if event.key == pygame.K_DOWN:
                    if main.snake.direction.y != -1:
                        main.snake.direction = Vector2(0,1) 
                if event.key == pygame.K_RIGHT:
                    if main.snake.direction.x != -1:
                        main.snake.direction = Vector2(1,0) 
                if event.key == pygame.K_LEFT:
                    if main.snake.direction.x != 1:
                        main.snake.direction = Vector2(-1,0)            
    main.draw_elements()
    main.draw_elements()
    pygame.display.flip()
    screen.fill(BLACK)

pygame.quit()    