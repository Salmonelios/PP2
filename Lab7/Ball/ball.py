import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700))
done = True
x = 25
y = 25

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    if x>975:
        x = 975
    if x<25:
        x = 25
    if y<25:
        y = 25
    if y>675:
        y = 675
        
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x,y), 25)
    pygame.display.flip()
    
    pygame.time.Clock().tick(30)
    
    