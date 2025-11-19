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

    def genral(s,window,keys,croshier:object):#prvi put ovo radim sa:object
        s.fspeed=s.speed
        if s.shoottime>0:
            s.shoottime-=1
            s.fspeed//=2
        s.dx=0
        s.dy=0
        s.angle+=360
        s.angle%=360
        s.image=textures[f"player{s.angle}"]
        window.blit(s.image,s.image.get_rect(center=(s.x,s.y)))
        if keys[pygame.K_w]:
            s.dy-=s.fspeed
        if keys[pygame.K_s]:
            s.dy+=s.fspeed
        if keys[pygame.K_d]:
            s.dx+=s.fspeed
        if keys[pygame.K_a]:
            s.dx-=s.fspeed
        s.x+=s.dx
        s.y+=s.dy
        anglenotnormal,dx,dy=vector_to_angle(croshier.x-s.x,s.y-croshier.y)
        s.angle=anglenotnormal
        if keys[pygame.K_SPACE] and s.shoottime==0:
            s.shoottime=20
            l_bullets.append(bullet(s.x,s.y,dx,dy*-1,s.angle))
l_bullets=[
    
    
    
    
]
class bullet:
    def __init__(s,x,y,dx,dy,angle):
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
        
    def general(s,window):
        window.blit(s.image,(s.x,s.y))
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
p1=Player(300,300,100,None,0,1.5)
croshair=crosheir(0,0)