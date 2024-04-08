import pygame
from color_palette import *
import random
from time import sleep
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
SCORE = 0
LEVEL = 0

CELL = 30
font = pygame.font.SysFont("Verdana", 20)

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
            global SCORE, LEVEL
            SCORE += 1
            if SCORE %5 == 0:
                LEVEL += 1 #counters for score and level

            food.pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
            if food.pos in self.body:
                while food.pos in self.body:
                    food.pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))
            

class Food:
    def __init__(self):
        self.pos = Point(random.randrange(HEIGHT//30), random.randrange(WIDTH//30))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 2
clock = pygame.time.Clock()

food = Food()
snake = Snake()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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

    draw_grid_chess()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    screen.blit(font.render("Score:"+str(SCORE), True, colorBLACK), (500, 10))
    screen.blit(font.render("LVL:"+str(LEVEL), True, colorBLACK), (500, 40)) # counters for score and level
    for i in snake.body[1:]:
        if (snake.body[0].x == i.x and snake.body[0].y == i.y) or (snake.body[0].y == HEIGHT//30 or snake.body[0].x == WIDTH//30 or snake.body[0].y == -1 or snake.body[0].x == -1):
            screen.fill(colorRED)
            screen.blit(pygame.font.SysFont("Verdana", 60).render("Game over", True, colorBLACK), (130, 250))
            screen.blit(font.render("Your total score: " + str(SCORE), True, colorBLACK), (150, 350))
            screen.blit(font.render("Your total level: " + str(LEVEL), True, colorBLACK), (150, 380))
            pygame.display.flip()
            sleep(2)
            pygame.quit()
            sys.exit()
    #checking for collision on a wall or snake itself
            
    FPS = 2 + LEVEL #increasing speed every level
    pygame.display.flip()
    clock.tick(FPS)