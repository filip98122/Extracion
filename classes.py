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
        window.blit(s.image,(s.x-s.image.get_width()/2,s.y-s.image.get_height()))
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
        
class bullet:
    def __init__(s,x,y,dx,dy):
        s.x=x
        s.y=y
        s.dx=dx
        s.dy=dy
        s.halflife=60
        s.speedmult=2.5
    def general(s,window):
        window
        
        
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