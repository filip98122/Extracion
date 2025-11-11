from classes import *
keylogesc=0
while True:
    if keylogesc>=1:
        keylogesc-=1
    window.fill((100,100,100))
    rendermap(maps,namematch)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if keylogesc==0:
        if keys[pygame.K_ESCAPE]:
            keylogesc=300
            break
    pygame.display.update()
    clock.tick(60)