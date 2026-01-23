from pesonalfunctions import *

class Slider:
    def __init__(s,x,y,w,h,perc,mx):
        s.x=x
        s.w=w
        s.h=h
        s.y=y
        s.y-=s.h//2
        s.x-=s.w//2
        s.percentege=perc
        s.maxperc=mx
        s.a=textures["slider"].get_width()/100*9
        s.b=textures["slider"].get_width()/100*82
        s.wt=1.75
        s.holding=False
    def general(s,mousep,mouses):
        pygame.draw.rect(window,"red",pygame.Rect(s.x,s.y,s.a+(s.b//s.maxperc)*s.percentege,s.h))
        window.blit(textures["slider"],(s.x,s.y))
        window.blit(textures["dot"],textures["dot"].get_rect(center=(s.x+s.a+(s.b//s.maxperc)*s.percentege,s.y+s.h//2)))
        
        pygame.draw.circle(window,"white",(s.x+s.w//4,s.y+s.h+(textures["plus"].get_height())*s.wt),tileh*0.65)
        window.blit(textures["minus"],textures["minus"].get_rect(center=(s.x+s.w//4,s.y+s.h+(textures["plus"].get_height())*s.wt)))
        
        pygame.draw.circle(window,"white",(s.x+(s.w//4)*3,s.y+s.h+(textures["plus"].get_height())*s.wt),tileh*0.65)
        window.blit(textures["plus"],textures["plus"].get_rect(center=(s.x+(s.w//4)*3,s.y+s.h+(textures["plus"].get_height())*s.wt)))
        if mouses[0]:
            if s.holding==False:
                if collison(s.x+(s.w//4)*1,s.y+s.h+(textures["plus"].get_height())*s.wt,tileh*0.65,mousep[0],mousep[1],1):
                    if s.percentege>=1:
                        s.percentege-=1
                        s.holding=True
                if collison(s.x+(s.w//4)*3,s.y+s.h+(textures["plus"].get_height())*s.wt,tileh*0.65,mousep[0],mousep[1],1):
                    if s.percentege<=s.maxperc-1:
                        s.percentege+=1
                        s.holding=True
        else:
            s.holding=False

        
Slidersplit=Slider(WIDTH//2,HEIGHT//3,textures["slider"].get_width(),textures["slider"].get_height(),1,2)
class Button:
    def __init__(s,x,y,w,h,type,text=None,pic=None,priority=None):
        s.x=x
        s.w=w
        s.h=h
        s.y=y
        s.type=type
        s.text=text
        s.pic=pic
        s.priority=priority
        if priority==None:
            s.priority=[s.picd,s.textd]
        else:
            s.priority=[s.textd,s.picd]
            
    def picd(s):
        if s.pic!=None:
            window.blit(textures[s.pic],(s.x,s.y))
    
    def textd(s):
        if s.text!=None:
            window.blit(textures[s.text],textures[s.text].get_rect(center=(s.x+s.w//2,s.y+s.h//2)))
            
    def general(s,mousep,mouses,arguments=None):
        returns=dictionary[s.type](s.x,s.y,s.w,s.h,s.priority,mousep,mouses,arguments)
        return returns
        
            
class Inventory:
    def __init__(s,size,contents,origin,gunslots=None,gunslotssize=None,extraslots=None,extraslotssize=None,extraslotstype=None,safeslots=None,safeslotssize=None):
        s.size=size
        s.contents=contents
        s.contents=make_empty([],size)
        s.contents[0]=["hat",1]
        s.contents[1]=["hat",1]
        s.origin=origin
        s.gunslots=gunslots
        s.gunslotssize=gunslotssize
        s.extraslots=extraslots
        s.extraslotssize=extraslotssize
        s.extraslotstype=extraslotstype
        s.safeslots=safeslots
        s.safeslotssize=safeslotssize
        s.awayfromleft=1000
        s.awayfromtop=300
        s.actions=None
        s.w=textures["inventoryslot"].get_width()
        s.h=textures["inventoryslot"].get_height()
        
    def p(s,mousestate,mouse,holdingmouse,originalmouse):
        global splitscreenitem
        argumets=splitscreenitem
        for i in range(max(math.ceil(s.size/4),1)):
            for j in range(min(s.size-i*4,4)):
                window.blit(textures["inventoryslot"],(j*s.w+s.awayfromleft,i*s.h+s.awayfromtop))
                if s.contents[i*4+j][0]!=None:
                    if i*4+j==s.actions:
                        pygame.draw.rect(window,(255,255,255),textures["inventoryslot"].get_rect(center=(j*s.w+s.awayfromleft+s.w//2,i*s.h+s.awayfromtop+s.h//2)))
                    window.blit(textures["inventoryslot"],(j*s.w+s.awayfromleft,i*s.h+s.awayfromtop))
                    window.blit(textures[f"{s.contents[i*4+j][0]}"],textures[f"{s.contents[i*4+j][0]}"].get_rect(center=(j*s.w+s.awayfromleft+s.w//2,i*s.h+s.awayfromtop+s.h//2)))
                    window.blit(textures[f"num{s.contents[i*4+j][1]}"],textures[f"num{s.contents[i*4+j][1]}"].get_rect(center=((1+j)*s.w+s.awayfromleft-s.w//2.5+(s.w//2.5//2),(1+i)*s.h+s.awayfromtop-s.h//2.5 +(s.h//2.5//2))))
                    
        if None!=s.actions:
            window.blit(textures["frame"],((s.actions%4)*s.w+s.awayfromleft+s.w,(s.actions//4)*s.h+s.awayfromtop+s.h-textures["frame"].get_height()))
            lsplitscreen=splitbutton.general(mouse,mousestate,splitscreenitem)
            splitscreenitem=lsplitscreen[0]
        return [splitscreenitem]
    def swap(s,xyoriginal,xy):
        xyoriginal[0]-=s.awayfromleft
        xyoriginal[1]-=s.awayfromtop
        xy[0]-=s.awayfromleft
        xy[1]-=s.awayfromtop
    
        tall=math.ceil(s.size/4)
        if s.size%4==0:
            if xy[0]<0 or xy[0]>s.w*4 or xy[1]<0 or xy[1]>tall*s.h:
                #drop to ground
                return
            if xyoriginal[0]<0 or xyoriginal[0]>s.w*4 or xyoriginal[1]<0 or xyoriginal[1]>tall*s.h:
                return
        else:
            if (xy[0]<0 or xy[0]>s.w*4 or xy[1]<0 or xy[1]>tall*s.h) and not (xy[0]>=0 and xy[0]<=s.w*(s.size%4) and xy[1]>=s.h*(s.size//4) and xy[1]<= tall*s.h):
                #drop to ground
                return
            if (xyoriginal[0]<0 or xyoriginal[0]>s.w*4 or xyoriginal[1]<0 or xyoriginal[1]>tall*s.h) and not (xyoriginal[0]>=0 and xyoriginal[0]<=s.w*(s.size%4) and xyoriginal[1]>=s.h*(s.size//4) and xyoriginal[1]<= tall*s.h):
                return
        
        originalindex=xyoriginal[1]//s.h*4+xyoriginal[0]//s.w
        nowindex=xy[1]//s.h*4+xy[0]//s.w
        if originalindex!=nowindex:
            if nowindex>=s.size:
                nowindex=s.size-1
            if originalindex>=s.size:
                originalindex=s.size-1
            if s.contents[originalindex][0]==s.contents[nowindex][0]:
                #Stack limit dict required
                    s.contents[nowindex][1]+=s.contents[originalindex][1]
                    s.contents[originalindex]=[None,0]
            
            else:
                # check if they can be swapped(eg. a non trinket into the trinket pocket)
                save=copy.deepcopy([s.contents[originalindex],s.contents[nowindex]])
                s.contents[originalindex]=save[1]
                s.contents[nowindex]=save[0]
splitbutton=None
def make_empty(lis:list,size):
    for i in range(size):
        ##          what much
        lis.append([None,0])
    return lis
class Player:
    def __init__(s,x,y,health,animation,angle,speed):
        s.x=x
        s.y=y
        s.health=health
        s.animation=animation
        s.angle=angle
        s.speed=speed
        s.shoottime=0
        s.maxhealth=s.health
        s.tabstate=False
        s.holdingtab=False
        s.holdingmouse=False
        s.originalmouse=[]
        s.holdingmouseR=False
        s.inventory=Inventory(12,[],"p",[],2,[],0,None,[],2)
    def genral(s,window,keys,croshier:object,mouse,mousepos):#prvi put ovo radim sa:object
        arguments=[]
        global offsetx,offsety
        if s.tabstate==False:
            s.fspeed=s.speed
            if s.shoottime>0:
                s.shoottime-=1
                s.fspeed//=2
            s.angle+=360
            s.angle%=360
            s.image=textures[f"player{s.angle}"]
            s.w=s.image.get_width()
            s.h=s.image.get_height()
            window.blit(s.image,s.image.get_rect(center=(s.x,s.y)))
            if s.health!=s.maxhealth:
                publicbar.draw(s.health,s.x,s.y-tileh/2-tileh/3,s.maxhealth)
            if (keys[pygame.K_w] or keys[pygame.K_s]) and (keys[pygame.K_a] or keys[pygame.K_d]):
                s.fspeed/=1.5
            prof=[offsetx,offsety]
            if keys[pygame.K_w]:
                offsety+=s.fspeed
            if keys[pygame.K_s]:
                offsety-=s.fspeed
            if keys[pygame.K_d]:
                offsetx-=s.fspeed
            if keys[pygame.K_a]:
                offsetx+=s.fspeed
            indexx=int((s.x+-offsetx)//tilew)
            indexy=int((s.y+-offsety)//tileh)
            for i in range(-1,2):
                for j in range(-1,2):
                    treny=indexy+i
                    trenx=indexx+j
                    if not (treny<0 or treny<0 or treny>=len(maps) or trenx>=len(maps[treny])):
                        if maps[treny][trenx]!=".":
                            if colision1(pygame.Rect(s.x-s.w//2,s.y-s.h//2,s.w,s.h),pygame.Rect(trenx*tilew+offsetx,treny*tileh+offsety,tilew,tileh)):
                                offsetx=prof[0]
                                offsety=prof[1]
            anglenotnormal,dx,dy=vector_to_angle(croshier.x-s.x,s.y-croshier.y)
            s.angle=anglenotnormal
            if mouse[0] and s.shoottime==0:
                s.shoottime=20
                l_bullets.append(bullet(s.x,s.y,dx,dy*-1,s.angle,"s",offsetx,offsety))
        else:
            if mouse[0]:
                if s.inventory.actions==None:
                    if s.holdingmouse==False:
                        s.holdingmouse=True
                        s.originalmouse=[mousepos[0],mousepos[1]]
                    s.inventory.actions=None
                else:
                    x=s.inventory.awayfromleft+(s.inventory.actions%4+1)*textures["inventoryslot"].get_width()
                    y=s.inventory.awayfromtop+(s.inventory.actions//4+1)*textures["inventoryslot"].get_height()-textures["frame"].get_height()
                    if button_colision(textures["frame"].get_width(),textures["frame"].get_height(),x,y,mousepos,mouse)==False or s.holdingmouse:
                        if s.holdingmouse==False:
                            s.holdingmouse=True
                            s.originalmouse=[mousepos[0],mousepos[1]]
                        s.inventory.actions=None
            elif mouse[2]:
                if s.holdingmouseR==False:
                    s.holdingmouseR=True
                    s.originalmouse=[mousepos[0],mousepos[1]]
            if (s.holdingmouse==True and mouse[0]==False) or (s.holdingmouseR and mouse[2]==False):
                if s.holdingmouse==True:
                    s.inventory.swap(s.originalmouse,[mousepos[0],mousepos[1]])
                    s.holdingmouse=False
                elif s.holdingmouseR==True:
                    global splitbutton
                    s.inventory.actions=min((mousepos[1]-s.inventory.awayfromtop)//textures["inventoryslot"].get_height()*4+(mousepos[0]-s.inventory.awayfromleft)//textures["inventoryslot"].get_width(),s.inventory.size-1)
                    splitbutton=Button((s.inventory.actions%4+1)*textures["inventoryslot"].get_width()+s.inventory.awayfromleft,(s.inventory.actions//4+1)*textures["inventoryslot"].get_height()+s.inventory.awayfromtop-textures["frame"].get_height(),textures["frame"].get_width(),textures["frame"].get_height()//5,"split","split")
                    s.holdingmouseR=False
            arguments=s.inventory.p(mouse,mousepos,s.holdingmouse,s.originalmouse)
        if keys[pygame.K_TAB]:
            if s.holdingtab==False:
                s.tabstate=not s.tabstate
                s.holdingtab=True
        else:
            s.holdingtab=False
        if s.health==0:
            exit()
        return offsetx,offsety,arguments
l_bullets=[]
class bar:
    def __init__(s):
        pass
    def draw(s,health,x,y,mxh):
        w=textures["bar"].get_width()
        frame=w/53.75
        h=textures["bar"].get_height()
        pygame.draw.rect(window,pygame.Color(124,13,14),pygame.Rect(frame+x-w/2,y-h+h/2,(w-frame*2)/mxh*health,h))#/8
        window.blit(textures["bar"],(x-w/2,y-textures["bar"].get_height()/2))
publicbar=bar()
class enemy:
    def __init__(s,x,y,tip):
        s.x=x
        s.y=y
        s.angle=0
        if tip=="bird":
            s.health=2
        s.speed=1
        s.shoottime=0
        s.maxhealth=s.health
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
        if s.health!=s.maxhealth:
            publicbar.draw(s.health,s.x+offsetx,s.y-s.image.get_height()/2-tileh/3+offsety,s.maxhealth)
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
        s.originaldxdy=[dx,dy]
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
    def draw(s,window,mousepos):
        s.im=textures[f"crosheir{p1.tabstate}"]
        s.x=mousepos[0]
        s.y=mousepos[1]
        window.blit(s.im,s.im.get_rect(center=(s.x,s.y)))
p1=Player(WIDTH/2,HEIGHT/2,5,None,0,2.5)
croshair=crosheir(0,0)
splitscreenitem=False
def detect_split(x,y,w,h,prio:list,mousepos,mousestate,splitscreenitem):
    global p1
    global mouseState
    global mousePos
    act=p1.inventory.actions
    if act!=None:
        if p1.inventory.contents[act]!=None:
            for i in range(2):
                prio[i]()
            if button_colision(w,h,x,y,mousepos,mousestate):
                splitscreenitem=True
    return [splitscreenitem]
dictionary={"split":detect_split}