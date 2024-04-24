import pygame
from color_palette import *
import random
from time import sleep
import sys
import psycopg2

pygame.init()

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'roma2005ass'
)

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS snake_users (
            nickname VARCHAR(20) PRIMARY KEY,
            level INT
);
""")
conn.commit()


WIDTH = 600
HEIGHT = 600
SCORE = 0
LEVEL = 0
TEXT = ""
k = random.randrange(3)
y = 0

CELL = 30
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)
change = pygame.USEREVENT + 1
pygame.time.set_timer(change, 5000)

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        head = self.body[0]
        self.body.pop()
        
        new_x = head.x + self.dx
        new_y = head.y + self.dy

        new_head = Point(new_x, new_y)
        self.body.insert(0, new_head)

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x - self.dx, head.y - self.dy))
            pygame.time.set_timer(change, 0)
            pygame.time.set_timer(change, 5000) #reseting the timer
            global SCORE, LEVEL, k, lst, y
            if k == 0 : SCORE += 1
            if k == 1 : SCORE += 2
            if k == 2 : SCORE += 5
            if y != SCORE//10 and SCORE//10 != 0:
                LEVEL += 1
            y = SCORE//10
            k = random.randrange(3) #randomly choosing a food
            
            lst[k].pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
            
            for i in range(len(self.body)):
                if lst[k].pos.x == self.body[i].x and lst[k].pos.y == self.body[i].y :
                    while lst[k].pos.x == self.body[i].x and lst[k].pos.y == self.body[i].y:
                        lst[k].pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
            

class Food:
    def __init__(self, color):
        self.pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 2
clock = pygame.time.Clock()

food1 = Food(colorGREEN)
food2 = Food(colorPurple)
food5 = Food(colorGold)
lst = [food1, food2, food5]
snake = Snake()

def menu():
    doone = False
    f = 0
    txt = False
    men = ["Resume", "Save", "Exit"]
    while not doone:
        screen.fill((100, 34, 134))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    doone = True
                elif event.key == pygame.K_DOWN:
                    f += 1
                    if f > 2: f = 2
                elif event.key == pygame.K_UP:
                    f -= 1
                    if f < 0: f = 0
                if event.key == pygame.K_RETURN:
                    if f == 0: doone = True
                    if f == 1:
                        cur.execute(f"""UPDATE snake_users
                        SET level = '{LEVEL}'
                        WHERE nickname = '{TEXT}'
                        """)
                        conn.commit()
                        txt = True
                    if f == 2:
                        pygame.quit()
                        sys.exit()
        
        
        for i in range(3):
            if f == i:
                screen.blit(big_font.render('>' + men[i], True, colorWHITE), (100, 60 + 60*i))
            else:
                screen.blit(big_font.render(men[i], True, colorWHITE), (100, 60 + 60*i))
        if txt: screen.blit(big_font.render("Saved", True, colorWHITE), (450,550))
        
        pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                TEXT = TEXT[:-1]
            elif event.key == pygame.K_RETURN:
                done = True
            else:
                TEXT += event.unicode
                TEXT = TEXT[:20]
    
    screen.fill((100, 34, 134))
    pygame.draw.rect(screen, colorWHITE, pygame.Rect(100, 275, 400, 50))
    screen.blit(big_font.render("Enter your nickname", True, colorWHITE), (95,200))
    screen.blit(font.render(TEXT, True, colorBLACK), (120,285))
    
    pygame.display.flip()
    
cur.execute(f"SELECT * FROM snake_users WHERE nickname  = '{TEXT}'")
found = cur.fetchone()
if found:
    LEVEL = found[1]
else:
    cur.execute(f"""INSERT INTO snake_users (nickname, level) VALUES
                ('{TEXT}', 0);
            """)
    conn.commit()
    
    
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == change:
            y = k
            k = random.randrange(3)
            lst[k].pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
            for i in range(len(snake.body)):
                if lst[k].pos.x == snake.body[i].x and lst[k].pos.y == snake.body[i].y :
                    while lst[k].pos.x == snake.body[i].x and lst[k].pos.y == snake.body[i].y:
                        lst[k].pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_ESCAPE:
                menu()

    draw_grid_chess()

    snake.move()

    snake.check_collision(lst[k])

    snake.draw()
    lst[k].draw()
    screen.blit(font.render("Score:"+str(SCORE), True, colorBLACK), (500, 10))
    screen.blit(font.render("LVL:"+str(LEVEL), True, colorBLACK), (500, 40)) # counters for score and level
    for i in snake.body[1:]:
        if (snake.body[0].x == i.x and snake.body[0].y == i.y) or (snake.body[0].y == HEIGHT//30 or snake.body[0].x == WIDTH//30 or snake.body[0].y == -1 or snake.body[0].x == -1):
            screen.fill(colorRED)
            screen.blit(pygame.font.SysFont("Verdana", 60).render("Game over", True, colorBLACK), (130, 250))
            screen.blit(font.render("Your total score: " + str(SCORE), True, colorBLACK), (150, 350))
            screen.blit(font.render("Your total level: " + str(LEVEL), True, colorBLACK), (150, 380))
            pygame.display.flip()
            cur.execute(f"""UPDATE snake_users
                        SET level = '{LEVEL}'
                        WHERE nickname = '{TEXT}'
                        """)
            conn.commit()
            sleep(2)
            pygame.quit()
            sys.exit()
    #checking for collision on a wall or snake itself
            
    FPS = 2 + LEVEL #increasing speed every level
    pygame.display.flip()
    clock.tick(FPS)