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
namematch=[[".",None],["+",textures["+"]]]#[neki]

def rendermap(maps,name):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            img=None
            for n in range(len(namematch)):
                if name[n][0]==maps[i][j][0]:
                    img=name[n][1]
                    break
            if img!=None and ():
                window.blit(img,(j*tilew,i*tileh))
