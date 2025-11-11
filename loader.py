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
    textures["player0"]=pygame.transform.scale(pygame.image.load("textures/player.png"),(tilew,tileh))
    for i in range(1,360):
        textures[f"player{i}"]=pygame.transform.rotate(textures["player0"],i)
    return textures
