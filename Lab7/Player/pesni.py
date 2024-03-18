import pygame

pygame.init()

screen = pygame.display.set_mode((300, 150))
done = True
on = pygame.image.load("on.png")
off = pygame.image.load("off.png")
nxt = pygame.image.load("next.png")
prev = pygame.image.load("prev.png")
on = pygame.transform.scale(on, (50, 50))
off = pygame.transform.scale(off, (50, 50))
prev = pygame.transform.scale(prev, (50, 50))
nxt = pygame.transform.scale(nxt, (50, 50))
prs = True
font = pygame.font.SysFont("Times New Roman", 34)

names = [font.render("Fontaine", True, (0, 0, 0)), font.render("Dawn Winery", True, (0, 0, 0)), font.render("Port Ormos", True, (0, 0, 0)), font.render("Rex Incognito", True, (0, 0, 0)), font.render("Sinner's Finale", True, (0, 0, 0)), font.render("Wildfire", True, (0, 0, 0))]
songs = [pygame.mixer.Sound("Fontaine.mp3"), pygame.mixer.Sound("Dawn Winery.mp3"), pygame.mixer.Sound("Port Ormos.mp3"), pygame.mixer.Sound("Rex Incognito.mp3"), pygame.mixer.Sound("Sinner's Finale.mp3"), pygame.mixer.Sound("Wildfire.mp3")]
i = 0
a = -1


while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                prs = not prs
            if event.key == pygame.K_RIGHT:
                if i != 5:
                    i += 1
            if event.key == pygame.K_LEFT:
                if i !=0:
                    i -= 1
            
            
    screen.fill((255, 255, 255))
    if a != i:
        pygame.mixer.stop()
        songs[i].play()
        songs[i].set_volume(0.3)
    pl = on.get_rect(center = (150, 75))
    pl1 = nxt.get_rect(center = (250, 75))
    pl2 = prev.get_rect(center = (50, 75))
    txt = names[i].get_rect(center = (150, 125))
    if prs:
        screen.blit(on, pl)
        pygame.mixer.unpause()
    else:
        screen.blit(off, pl)
        pygame.mixer.pause()
    screen.blit(nxt, pl1)
    screen.blit(prev, pl2)
    screen.blit(names[i], txt)
    a = i
    pygame.display.flip()