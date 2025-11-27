from functions import *
offsetx=0
offsety=0
maps=[]
with open("map.txt","r",) as f:
    ltemp=f.readlines()
    for i in range(len(ltemp)):
        maps.append([])
        for j in range(len(ltemp[i])):
            maps[i].append(ltemp[i][j])
namematch=[[".",None],["+",textures["+"]],["t",textures["tree1"]]]#[neki]

def rendermap(maps,name,offsetx,offsety,lbull):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            img=None
            for n in range(len(namematch)):
                if name[n][0]==maps[i][j][0]:
                    img=name[n][1]
                    break
            if img!=None and colision1(pygame.Rect(j*tilew+offsetx,i*tileh+offsety,tilew,tileh),pygame.Rect(0,0,WIDTH,HEIGHT)):
                ii=0
                for ki in range(len(lbull)):
                    if colision1(pygame.Rect(j*tilew+offsetx,i*tileh+offsety,tilew,tileh),pygame.Rect(lbull[ii].x+(offsetx-lbull[ii].ofx)-lbull[ii].w//2,lbull[ii].y+(offsety-lbull[ii].ofy)-lbull[ii].h//2,lbull[ii].w,lbull[ii].h)):
                        del lbull[ii]
                        ii-=1
                    ii+=1
                
                window.blit(img,(j*tilew+offsetx,i*tileh+offsety))
