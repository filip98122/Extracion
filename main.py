from classes import *
pygame.mouse.set_visible(False)
keylogesc=0
#Bug1:plater blood particles would still be calculated using the offsetx/y(the thing the makes everything seem to go to the leftt if you press right)
#Fix1: Added a special case with if the player was shot (Note: this can have further uses later)
#Bug2: The enemy bar was not directly above him when i moved(stayed fixed in a pos)
#Fix2: After a lot of debugging found that i was not inputing x+offsetx, but just x :|
#Bug3: Particles would become fixed (like in bug2)
#Fix3: Apparently in the personalfunctions file the "global" variable of offsetx/y would be 0( bcs i at the start of the file,not in a function, i said offsetx/y=0)
#Bug4: Particles wouldn't spawn where the point of coliosion is. 
#Fix4: Particles now spawn at the center of the bullet + half the width and height  ( it's complicated, using the original dx and dy)
#
#
#
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
    if keylogesc==0:
        if keys[pygame.K_ESCAPE]:
            keylogesc=300
            break
    if p1.tabstate==False:
        for i in range(len(l_bullets)):
            l_bullets[cou].general(window)
            if l_bullets[cou].halflife<=0:
                del l_bullets[cou]
                continue
            if colision1(pygame.rect.Rect(l_bullets[cou].x+(offsetx-l_bullets[cou].ofx)-l_bullets[cou].w//2,l_bullets[cou].y+(offsety-l_bullets[cou].ofy)-l_bullets[cou].h//2,l_bullets[cou].w,l_bullets[cou].h),pygame.rect.Rect(p1.x-p1.image.get_width()//2,p1.y-p1.image.get_height()//2,p1.image.get_width(),p1.image.get_height())) and l_bullets[cou].origin=="e":
                p1.health-=1
                for iii in range(10):
                    negative=1
                    if random.randint(0,1)==0:
                        negative=-1
                    particle((random.randint(160,190),random.randint(28,58),random.randint(15,45)),l_bullets[cou].x+(kolko*l_bullets[cou].originaldxdy[0]),l_bullets[cou].y+(kolko*l_bullets[cou].originaldxdy[1]),(random.uniform(2,4))*negative,-tileh/40,25,random.randint(0,iii),offsetx,offsety,"player")
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
                        for iii in range(10):
                            negative=1
                            if random.randint(0,1)==0:
                                negative=-1
                            particle((random.randint(160,190),random.randint(28,58),random.randint(15,45)),l_bullets[cou].x+(kolko*l_bullets[cou].originaldxdy[0]),l_bullets[cou].y+(kolko*l_bullets[cou].originaldxdy[1]),(random.uniform(2,4))*negative,-tileh/40,25,random.randint(0,iii),offsetx,offsety)
                        del l_bullets[cou]
                        break
                    coun1+=1
                continue

            cou+=1
        
        
        cou=0
        for i in range(len(l_enemies)):
            l_enemies[cou].general(window,keys,p1)
            cou+=1
    
        offsetx,offsety=p1.genral(window,keys,croshair,mouseState,mousePos)
        croshair.draw(window,mousePos)
        count=0
        for i in range(len(lparticles)):
            lparticles[count].general(offsetx,offsety)
            if lparticles[count].halflife==0:
                del lparticles[count]
                continue
            count+=1
    if p1.tabstate:
        window.fill("black")
        offsetx,offsety=p1.genral(window,keys,croshair,mouseState,mousePos)
        croshair.draw(window,mousePos)
    pygame.display.update()
    clock.tick(60)