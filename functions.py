from loader import *
textures=load()

"""
def ens(file_data):
    with open("info.json", "w") as fa:
        json.dump(file_data, fa)
def end():
    with open("info.json", "r") as fa:
        file_data=fa.read()
    file_data=json.loads(file_data)
    return file_data
"""
"""



def ens(file_data):
    with open("info.json", "w") as fa:
        json.dump(file_data, fa)
def end():
    with open("info.json", "r") as fa:
        file_data=fa.read()
    file_data=json.loads(file_data)
    return file_data



def read():
    info=end()
    return info
info=read()
def save(info):
    ens(info)
"""
#save({'local': {'turn': 'b', 'check': False, 'cheesboardmap': None, 'value': 0.00}, 'ai': {},"lpieces":{}})
#exit()
def collison(x1,y1,r1,x2,y2,r2): 
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def checker(keys):
    pressed = 0
    for key in range(512):
        if keys[key]:
            pressed = key
            break
    if pressed!=0:
        return pressed
def checker(keys):
    pressed = 0
    for key in range(512):
        if keys[key]:
            pressed = key
            break
    if pressed!=0:
        return pressed
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH,HEIGHT))
def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
