from functions import *
offsetx=0
offsety=0
maps=[]
class Particle:
    def __init__(s,color,x,y,dx,dy,halflife,slep,ofx,ofy,who):
        s.who=who
        s.color=color
        s.x=x
        s.y=y
        s.dx=dx
        s.dy=dy
        s.halflife=halflife
        s.ddy=0.01
        s.slep=slep
        s.ofx=ofx
        s.ofy=ofy
    def general(s,ofx,ofy):
        if s.slep==0:
            if s.who=="player":
                pygame.draw.circle(window,s.color,(s.x,s.y),tileh/24)
            else:
                pygame.draw.circle(window,s.color,(s.x+(ofx-s.ofx),s.y+(ofy-s.ofy)),tileh/24)
            s.x+=s.dx
            s.y+=s.dy
            s.halflife-=1
            if s.dx<0:
                s.dx-=max(-0.1,s.dx)
            if s.dx>0:
                s.dx-=min(0.1,s.dx)
            s.dy+=s.ddy
            s.ddy+=0.03
        else:
            s.slep-=1
def particle(color,x,y,dx,dy,halflife,sleep,offsetx,offsety,who=None):
    lparticles.append(Particle(color,x,y,dx,dy,halflife,sleep,offsetx,offsety,who))
with open("map.txt","r",) as f:
    ltemp=f.readlines()
    for i in range(len(ltemp)):
        maps.append([])
        for j in range(len(ltemp[i])):
            maps[i].append(ltemp[i][j])
namematch=[[".",None],["+",textures["+"],[137,167,137,167,141,171]],["t",textures["tree1"],[0,21,49,79,28,58]]]#[neki]

lparticles=[]
def rendermap(maps,name,offsetx,offsety,lbull):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            img=None
            ncuvar=0
            for n in range(len(namematch)):
                if name[n][0]==maps[i][j][0]:
                    img=name[n][1]
                    ncuvar=n
                    break
            if img!=None and colision1(pygame.Rect(j*tilew+offsetx,i*tileh+offsety,tilew,tileh),pygame.Rect(0,0,WIDTH,HEIGHT)):
                ii=0
                for ki in range(len(lbull)):
                    if colision1(pygame.Rect(j*tilew+offsetx,i*tileh+offsety,tilew,tileh),pygame.Rect(lbull[ii].x+(offsetx-lbull[ii].ofx)-lbull[ii].w//2,lbull[ii].y+(offsety-lbull[ii].ofy)-lbull[ii].h//2,lbull[ii].w,lbull[ii].h)):
                        for iii in range(10):
                            negative=1
                            if random.randint(0,1)==0:
                                negative=-1
                            particle((random.randint(name[ncuvar][2][0],name[ncuvar][2][1]),random.randint(name[ncuvar][2][2],name[ncuvar][2][3]),random.randint(name[ncuvar][2][4],name[ncuvar][2][5])),lbull[ii].x,lbull[ii].y,(random.uniform(2,4))*negative,-tileh/40,95,random.randint(0,iii),offsetx,offsety)
                        del lbull[ii]
                        ii-=1
                    ii+=1
                
                window.blit(img,(j*tilew+offsetx,i*tileh+offsety))
