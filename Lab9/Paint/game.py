import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
add_screen = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5
i = 0
lst = [colorRED, colorBLUE, colorWHITE]
font = pygame.font.SysFont("Verdana", 20)

currX = 0
currY = 0

prevX = 0
prevY = 0
fig = 0

done = False
Eveeent = pygame.USEREVENT

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

while not done:
    for event in pygame.event.get():
        if (fig != 0 and fig != 3) and LMBpressed:
            screen.blit(add_screen, (0,0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == Eveeent:
            pygame.draw.rect(screen, colorBLACK, pygame.Rect(10, 570, 130, 50))
            pygame.time.set_timer(Eveeent, 0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            if fig == 0 or fig == 3:
                currX = event.pos[0]
                currY = event.pos[1]
                prevX = event.pos[0]
                prevY = event.pos[1]
            if fig != 0 and fig != 3:
                prevX = event.pos[0]
                prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if fig == 1:
                    pygame.draw.rect(screen, lst[i], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if fig == 2:
                    pygame.draw.circle(screen, lst[i], (prevX, prevY), max(abs(currX-prevX), abs(currY-prevY)), THICKNESS)
                if fig == 4:
                    pygame.draw.rect(screen, lst[i], pygame.Rect(min(prevX, currX), min(prevY, currY), abs(prevX-currX), abs(prevX-currX)))
                if fig == 5:
                    pygame.draw.polygon(screen, lst[i], ((prevX, prevY), (abs(prevX-currX), prevY), (prevX, abs(prevY-currY))))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if fig == 1:
                pygame.draw.rect(screen, lst[i], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            if fig == 2:
                pygame.draw.circle(screen, lst[i], (prevX, prevY), max(abs(currX-prevX), abs(currY-prevY)), THICKNESS)
            if fig == 4:
                pygame.draw.rect(screen, lst[i], pygame.Rect(min(prevX, currX), min(prevY, currY), abs(prevX-currX), abs(prevX-currX)))

            add_screen.blit(screen, (0,0))
        if fig == 0:
            pygame.draw.line(screen, lst[i], (prevX, prevY), (currX, currY), THICKNESS)
        if fig == 3:
            pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS -= 1
            if event.key == pygame.K_LEFT:
                i -= 1
                if i < 0: i = 0
                if i == 0:
                    screen.blit(font.render("Color: red",True, (0, 255, 255)), (10, 570))
                    pygame.time.set_timer(Eveeent, 1000)
                if i == 1:
                    screen.blit(font.render("Color: blue",True, (0, 255, 255)), (10, 570))
                    pygame.time.set_timer(Eveeent, 1000)
            if event.key == pygame.K_RIGHT:
                i += 1
                if i > 2: i = 2
                if i == 1:
                    screen.blit(font.render("Color: blue",True, (0, 255, 255)), (10, 570))
                    pygame.time.set_timer(Eveeent, 1000)
                if i == 2:
                    screen.blit(font.render("Color: white",True, (0, 255, 255)), (10, 570))
                    pygame.time.set_timer(Eveeent, 1000)
                
    keys = pygame.key.get_pressed()
    
    
    if fig == 0 or fig == 3:
        prevX = currX
        prevY = currY
        
        
    if keys[pygame.K_r]: fig = 1
    if keys[pygame.K_l]: fig = 0
    if keys[pygame.K_c]: fig = 2
    if keys[pygame.K_e]: fig = 3
    if keys[pygame.K_s]: fig = 4
    if keys[pygame.K_t]: fig = 5

    pygame.display.flip()
    clock.tick(60)