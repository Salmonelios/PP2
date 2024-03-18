import pygame, datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
mic = pygame.image.load("chaa.png")
back = pygame.image.load("micc.png")
sm = pygame.image.load("small.png")
bg = pygame.image.load("big.png")
dg = 1
done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = False
                
    dg = datetime.datetime.now().second * 6
    dgg = datetime.datetime.now().minute * 6
    screen.fill((255, 255, 255))
    bg_rt = pygame.transform.rotate(bg, -dg)
    sm_rt = pygame.transform.rotate(sm, -dgg)
    bg_rect = bg_rt.get_rect(center = (400, 400))
    sm_rect = sm_rt.get_rect(center = (400, 400))
    screen.blit(pygame.transform.scale(back, (401, 574)), (200, 100))
    screen.blit(pygame.transform.scale(mic, (800, 800)), (0, 0))
    screen.blit(bg_rt, bg_rect)
    screen.blit(sm_rt, sm_rect)
    pygame.display.flip()
