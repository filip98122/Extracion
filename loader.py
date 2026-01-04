import pygame
import os
import random
import math
import time
import json
import sys
import copy
pygame.init()
pygame.font.init()
WIDTH,HEIGHT=1920,1080
kolko=40
tilew=120
tileh=120
def load():
    textures={}
    textures["+"]=pygame.transform.scale(pygame.image.load("textures/brick.png"),(tilew,tileh))
    textures["player0"]=pygame.transform.scale(pygame.image.load("textures/player.png"),(tileh/1.5,(tilew/1.5)*1.25))
    for i in range(1,360):
        textures[f"player{((-i)+360)}"]=pygame.transform.rotate(textures["player0"],i)
    textures["crosheirFalse"]=pygame.transform.scale(pygame.image.load("textures/crosheir.png"),(tileh/3,tileh/3))
    textures["bullet0"]=pygame.transform.scale(pygame.image.load("textures/bullet.png"),(tilew/9.6,tileh/1.5))
    textures["bird0"]=pygame.transform.scale(pygame.image.load("textures/bird.png"),(tileh/1.5,tilew/1.5))
    textures["tree1"]=pygame.transform.scale(pygame.image.load("textures/tree.png"),(tilew,tileh))
    textures["bar"]=pygame.transform.scale(pygame.image.load("textures/bar.png"),(tilew/1.2,tileh/12))
    textures["inventoryslot"]=pygame.transform.scale(pygame.image.load("textures/inventory slot.png"),(tilew-tilew/4,tileh-tileh/4))
    textures["crosheirTrue"]=pygame.transform.scale(pygame.image.load("textures/mouse.png"),(tileh/2.5,tileh/3))
    textures["hat"]=pygame.transform.scale(pygame.image.load("textures/hat.png"),(tilew-tilew/2.5,tileh-tileh/2.5))
    return textures