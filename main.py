from classes import *
pygame.mouse.set_visible(False)
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
    
    croshair.draw(window,mousePos)
    cou=0
    for i in range(len(l_bullets)):
        l_bullets[cou].general(window)
        if l_bullets[cou].halflife==0:
            del l_bullets[cou]
            cou-=1
        cou+=1
    p1.genral(window,keys,croshair)
    if keylogesc==0:
        if keys[pygame.K_ESCAPE]:
            keylogesc=300
            break
    pygame.display.update()
    clock.tick(60)