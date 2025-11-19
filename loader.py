import pygame
import os
import random
import math
import time
import json
import sys
pygame.init()
pygame.font.init()
WIDTH,HEIGHT=1920,1080
tilew=96
tileh=54
def load():
    textures={}
    textures["+"]=pygame.transform.scale(pygame.image.load("textures/brick.png"),(tilew,tileh))
    textures["player0"]=pygame.transform.scale(pygame.image.load("textures/player.png"),(tileh,tilew))
    for i in range(1,360):
        textures[f"player{((-i)+360)}"]=pygame.transform.rotate(textures["player0"],i)
    textures["crosheir"]=pygame.transform.scale(pygame.image.load("textures/crosheir.png"),(tileh/2,tileh/2))
    textures["bullet0"]=pygame.transform.scale(pygame.image.load("textures/bullet.png"),(tilew/9.6,tileh/1.5))
    return textures