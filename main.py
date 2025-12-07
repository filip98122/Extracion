from classes import *
pygame.mouse.set_visible(False)
keylogesc=0
 
while True:
    if keylogesc>=1:
        keylogesc-=1
    window.fill((10,150,10))
    rendermap(maps,namematch,offsetx,offsety,l_bullets)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    cou=0
    window.blit(textures["bar"],(100,100))
    for i in range(len(l_bullets)):
        l_bullets[cou].general(window)
        if l_bullets[cou].halflife<=0:
            del l_bullets[cou]
            continue
        if colision1(pygame.rect.Rect(l_bullets[cou].x+(offsetx-l_bullets[cou].ofx)-l_bullets[cou].w//2,l_bullets[cou].y+(offsety-l_bullets[cou].ofy)-l_bullets[cou].h//2,l_bullets[cou].w,l_bullets[cou].h),pygame.rect.Rect(p1.x-p1.image.get_width()//2,p1.y-p1.image.get_height()//2,p1.image.get_width(),p1.image.get_height())) and l_bullets[cou].origin=="e":
            p1.health-=1
            del l_bullets[cou]
            continue
        if l_bullets[cou].origin=="s":
            coun1=0
            for j in range(len(l_enemies)):
                if colision1(pygame.rect.Rect(l_bullets[cou].x+(offsetx-l_bullets[cou].ofx)-l_bullets[cou].w//2,l_bullets[cou].y+(offsety-l_bullets[cou].ofy)-l_bullets[cou].h//2,l_bullets[cou].w,l_bullets[cou].h),pygame.rect.Rect(l_enemies[coun1].x+offsetx,l_enemies[coun1].y+offsety,l_enemies[coun1].image.get_width(),l_enemies[coun1].image.get_height())):
                    l_enemies[coun1].health-=1
                    if l_enemies[coun1].health==0:
                        del l_enemies[coun1]
                        coun1-=1
                    del l_bullets[cou]
                    break
                coun1+=1
            continue

        cou+=1
    
    
    cou=0
    for i in range(len(l_enemies)):
        l_enemies[cou].general(window,keys,p1)
        cou+=1
    
    
    offsetx,offsety=p1.genral(window,keys,croshair,mouseState)
    croshair.draw(window,mousePos)
    if keylogesc==0:
        if keys[pygame.K_ESCAPE]:
            keylogesc=300
            break
    pygame.display.update()
    clock.tick(60)