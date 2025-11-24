from pesonalfunctions import *
class Player:
    def __init__(s,x,y,health,animation,angle,speed):
        s.x=x
        s.y=y
        s.health=health
        s.animation=animation
        s.angle=angle
        s.speed=speed
        s.shoottime=0
    def genral(s,window,keys,croshier:object,mouse):#prvi put ovo radim sa:object
        global offsetx,offsety
        s.fspeed=s.speed
        if s.shoottime>0:
            s.shoottime-=1
            s.fspeed//=2
        s.angle+=360
        s.angle%=360
        s.image=textures[f"player{s.angle}"]
        window.blit(s.image,s.image.get_rect(center=(s.x,s.y)))
        if (keys[pygame.K_w] or keys[pygame.K_s]) and (keys[pygame.K_a] or keys[pygame.K_d]):
            s.fspeed/=1.5
        if keys[pygame.K_w]:
            offsety+=s.fspeed
        if keys[pygame.K_s]:
            offsety-=s.fspeed
        if keys[pygame.K_d]:
            offsetx-=s.fspeed
        if keys[pygame.K_a]:
            offsetx+=s.fspeed
        anglenotnormal,dx,dy=vector_to_angle(croshier.x-s.x,s.y-croshier.y)
        s.angle=anglenotnormal
        if mouse[0] and s.shoottime==0:
            s.shoottime=20
            l_bullets.append(bullet(s.x,s.y,dx,dy*-1,s.angle,"s",offsetx,offsety))
        if s.health==0:
            exit()
        return offsetx,offsety
l_bullets=[]
class enemy:
    def __init__(s,x,y,tip):
        s.x=x
        s.y=y
        s.angle=0
        if tip=="bird":
            s.health=2
        s.speed=1
        s.shoottime=0
    def general(s,window,keys,croshier:object):#prvi put ovo radim sa:object
        s.fspeed=s.speed
        if s.shoottime>0:
            s.shoottime-=1
            s.fspeed//=2
        s.dx=0
        s.dy=0
        s.angle+=360
        s.angle%=360
        if f"bird{s.angle}" not in textures:
            textures[f"bird{s.angle}"]=pygame.transform.rotate(textures["bird0"],-s.angle+360)
        s.image=textures[f"bird{s.angle}"]
        window.blit(s.image,s.image.get_rect(center=(s.x+offsetx,s.y+offsety)))
        s.x+=s.dx
        s.y+=s.dy
        anglenotnormal,dx,dy=vector_to_angle(croshier.x-offsetx-s.x,s.y-croshier.y+offsety)
        s.angle=anglenotnormal
        if random.randint(1,150)==1 and s.shoottime==0:
            s.shoottime=60
            l_bullets.append(bullet(s.x+offsetx,s.y+offsety,dx,dy*-1,s.angle,"e",offsetx,offsety))
    
l_enemies=[enemy(700,700,"bird")]
class bullet:
    def __init__(s,x,y,dx,dy,angle,origin,ofx,ofy):
        s.x=x
        s.y=y
        s.dx=dx
        s.dy=dy
        s.halflife=27
        s.speedmult=35
        s.angle=angle
        if f"bullet{s.angle}" in textures:
            pass
        else:
            textures[f"bullet{s.angle}"]=pygame.transform.rotate(textures["bullet0"],-s.angle+360)
        s.image=textures[f"bullet{s.angle}"]
        s.dx*=s.speedmult
        s.dy*=s.speedmult
        s.origin=origin
        s.w=s.image.get_width()
        s.h=s.image.get_height()
        s.ofx=ofx
        s.ofy=ofy
    def general(s,window):
        window.blit(s.image,(s.x-s.w//2+(offsetx-s.ofx),s.y-s.h//2+(offsety-s.ofy)))
        s.x+=s.dx
        s.y+=s.dy
        s.halflife-=1
        
        
class crosheir:
    def __init__(s,x,y):
        s.x=x
        s.y=y
        s.image=textures["crosheir"]
        s.wh=s.image.get_width()

    def draw(s,window,mousepos):
        s.x=mousepos[0]
        s.y=mousepos[1]
        window.blit(s.image,(s.x-s.wh/2,s.y-s.wh/2))
p1=Player(WIDTH/2,HEIGHT/2,5,None,0,2.5)
croshair=crosheir(0,0)