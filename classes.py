from pesonalfunctions import *
class Player:
    def __init__(s,x,y,health,animation):
        s.x=x
        s.y=y
        s.health=health
        s.animation=animation
    def draw(s,window):
        if s.animation=="":
            s.image=textures#nesto
        window.blit(s.image)