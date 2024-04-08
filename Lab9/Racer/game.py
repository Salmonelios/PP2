#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coins = 0
i = random.randrange(3)

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
coin1 = pygame.transform.scale(pygame.image.load("Coin.png"), (40, 40))
coin2 = pygame.transform.scale(pygame.image.load("Coin2.png"), (40, 40))
coin5 = pygame.transform.scale(pygame.image.load("Coin5.png"), (40, 40))
#adding 3 different type of coins

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        #added movement in y axis
        
class COINS(pygame.sprite.Sprite):
    def __init__(self, imagee):
        super().__init__()
        self.image = imagee
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_WIDTH - 40))
        
    def move(self):
        pass
#creating class for coins
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = COINS(coin1)
C2 = COINS(coin2)
C5 = COINS(coin5)

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
lst = []
lst.append(C1)
lst.append(C2)
lst.append(C5)

pygame.mixer.Sound("background.wav").play()
#added background music

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    Coins = font_small.render("Coins:" + str(coins), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(Coins, (300, 10))
    #The counter for coins shown on screen
    
    DISPLAYSURF.blit(lst[i].image, lst[i].rect) #displaying a coin

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.stop()
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          Total_car = font_small.render(f"Total cars: {SCORE}", True, BLACK)
          Total_coins = font_small.render(f"Total coins: {coins}", True, BLACK)
          DISPLAYSURF.blit(Total_car, (30, 350))
          DISPLAYSURF.blit(Total_coins, (30, 390)) # added score titles at the end of game
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()    
    
    if pygame.sprite.collide_rect(P1, lst[i]):
        if i == 0: coins += 1
        if i == 1: coins += 2
        if i == 2: coins += 5
        # adding points in case which coint collected
        i = random.randrange(3)
        SPEED = 5 + 0.5 * (coins//10) #adding speed every 10 points
        lst[i].rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        # If collecting coint increasing score and replacing coin
        
            
        
    pygame.display.update()
    FramePerSec.tick(FPS)