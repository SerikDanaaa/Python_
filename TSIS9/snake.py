import pygame, random,sys
from pygame.math import Vector2

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

cell_size = 20
cell_number = 25
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
apple = pygame.image.load('apple.png').convert_alpha()
game_font = pygame.font.SysFont('Bodoni-MT-Black',30)


RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (100,0,200)
BLUE1 = (200,0,250)
GREEN = (175,215,70)

class FOOD:
    def __init__(self):
        self.randomize()
    
    def Draw_Food(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        food_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size)
        screen.blit(apple, food_rect)
        #pygame.draw.rect(screen,(RED), food_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self,x,y,z):
        self.body = [x,y,z]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.sound = pygame.mixer.Sound('sound.mp3')
    
    def Draw_Snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * cell_size),int(block.y * cell_size), cell_size,cell_size)
            pygame.draw.rect(screen,(BLUE), snake_rect)
    
    def Draw_Snake1(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * cell_size),int(block.y * cell_size), cell_size,cell_size)
            pygame.draw.rect(screen,(BLUE1), snake_rect)        
    
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
    
    def play_sound(self):
        self.sound.play()

class MAIN:
    def __init__(self):
        self.snake = SNAKE(Vector2(5,10),Vector2(4,10),Vector2(3,10))
        self.snake1 = SNAKE(Vector2(5,15),Vector2(4,15),Vector2(3,15))
        self.food = FOOD()
        self.pos = []

    def update(self):
        self.snake.Move_Snake()
        self.snake1.Move_Snake()  
        self.check_collision()
        self.fail()

    def draw_elements(self):
        self.draw_grass()
        self.food.Draw_Food()
        self.snake.Draw_Snake()
        self.snake1.Draw_Snake1()
        self.score()
        self.score1()
        if len(self.snake.body) - 3 > 1 or len(self.snake1.body) - 3 > 1 :
            self.draw_walls()
        if len(self.snake.body) - 3 > 3 or len(self.snake1.body) - 3 > 3 :
            self.draw_walls2()    

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.snake.play_sound()
        if self.food.pos == self.snake1.body[0]:
            self.food.randomize()
            self.snake1.add_block()
            self.snake1.play_sound()
                
    def fail(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:    
            self.game_over()
        if not 0 <= self.snake1.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake1.body[0].y < cell_number:    
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()        
        
        for block in self.snake1.body[1:]:
            if block == self.snake1.body[0]:
                self.game_over()  

        for block in self.pos:
            if block == self.snake.body[0]:
                self.game_over()        
        
        for block in self.pos:
            if block == self.snake1.body[0]:
                self.game_over()         
        
    def game_over(self):
        pygame.quit()
        sys.exit()  
    
    def draw_grass(self): 
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect) 
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def score(self):
        score_text ='Player 1:' + str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_pos_x = int(cell_size * cell_number - 60)
        score_pos_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_pos_x,score_pos_y))
        screen.blit(score_surface,score_rect)
        

    def score1(self):
        score_text = 'Player 2:' + str(len(self.snake1.body) - 3)
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_pos_x1 = int(cell_size * cell_number - 60)
        score_pos_y1 = int(cell_size * cell_number - 10)
        score_rect = score_surface.get_rect(center = (score_pos_x1,score_pos_y1))
        screen.blit(score_surface,score_rect)    

    def draw_walls(self):
        #1 level
        for row in range(5):
            self.pos.append(Vector2(row,10))
            wall_rect = pygame.Rect(row * cell_size,cell_size * 10,cell_size,cell_size)
            pygame.draw.rect(screen,(BLACK),wall_rect)
        for col in range(8):
            self.pos.append(Vector2(10,col))
            wall_rect = pygame.Rect(10* cell_size,cell_size * col,cell_size,cell_size) 
            pygame.draw.rect(screen,(BLACK),wall_rect)    
        for row in range(10,20):
            self.pos.append(Vector2(row,20))
            wall_rect = pygame.Rect(row * cell_size,cell_size * 20,cell_size,cell_size)
            pygame.draw.rect(screen,(BLACK),wall_rect)    

    def draw_walls2(self):
        #2 level
        for row in range(10):
            self.pos.append(Vector2(row,8))
            wall_rect = pygame.Rect(row * cell_size,cell_size * 8,cell_size,cell_size)
            pygame.draw.rect(screen,(BLACK),wall_rect)
        for col in range(8):
            self.pos.append(Vector2(15,col))
            wall_rect = pygame.Rect(15* cell_size,cell_size * col,cell_size,cell_size) 
            pygame.draw.rect(screen,(BLACK),wall_rect)    
        for row in range(15,):
            self.pos.append(Vector2(row,25))
            wall_rect = pygame.Rect(row * cell_size,cell_size * 21,cell_size,cell_size)
            pygame.draw.rect(screen,(BLACK),wall_rect)  
        for col in range(21):
            self.pos.append(Vector2(21,col))
            wall_rect = pygame.Rect(21 * cell_size,cell_size * col,cell_size,cell_size) 
            pygame.draw.rect(screen,(BLACK),wall_rect)  
        for row in range(10,18):
            self.pos.append(Vector2(row,10))
            wall_rect = pygame.Rect(row * cell_size,cell_size * 12,cell_size,cell_size)
            pygame.draw.rect(screen,(BLACK),wall_rect)                       

main = MAIN()

done = False

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

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
                if event.key == pygame.K_w:
                    if main.snake1.direction.y != 1:
                        main.snake1.direction = Vector2(0,-1) 
                if event.key == pygame.K_s:
                    if main.snake1.direction.y != -1:
                        main.snake1.direction = Vector2(0,1) 
                if event.key == pygame.K_d:
                    if main.snake1.direction.x != -1:
                        main.snake1.direction = Vector2(1,0) 
                if event.key == pygame.K_a:
                    if main.snake1.direction.x != 1:
                        main.snake1.direction = Vector2(-1,0)                    
    main.draw_elements()
    main.draw_elements()
    pygame.display.flip()
    screen.fill(GREEN)

pygame.quit()    