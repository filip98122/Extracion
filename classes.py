from pesonalfunctions import *
def Vector_Normalization(x,y):
    # Calculate dx and dy with direction
    vector_length=math.sqrt(x*x+y*y)#Pitagorina teorema
    x=x/vector_length
    y=y/vector_length
    return x,y

def vector_to_angle(x,y):
    x,y=Vector_Normalization(x,y)
    radians=math.asin(y)
    return int(math.degrees(radians))

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
        window.blit(s.image)
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
        bdx,bdy=Vector_Normalization(s.x,s.y,croshier.x,croshier.y)
        