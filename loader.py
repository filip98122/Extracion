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
mouseState = pygame.mouse.get_pressed()
mousePos = pygame.mouse.get_pos()
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
    textures["frame"]=pygame.transform.scale(pygame.image.load("textures/frame.png"),((tilew-tilew/4)*2.5,(tileh-tileh/4)*3.5))
    textures["frameblack"]=pygame.transform.scale(pygame.image.load("textures/frameb.png"),((tilew)*5,(tileh)*1.5))
    textures["font-/2.5"]= pygame.font.SysFont('B', int((tilew-tilew/2.5)/2.5))
    textures["fontsplit"]= pygame.font.SysFont('B', int(tileh-(tileh//8*5.5)))
    textures["plus"]=pygame.transform.scale(pygame.image.load("textures/plus.png"),((tilew),(tileh)))
    textures["framebigwhite"]=pygame.transform.scale(pygame.image.load("textures/frame.png"),(tilew*5,tileh*1))
    textures["minus"]=pygame.transform.scale(pygame.image.load("textures/minus.png"),((tilew),(tileh//7)))
    textures["framebig"]=pygame.transform.scale(pygame.image.load("textures/frameb.png"),(tilew*5,tileh*1))
    textures["slider"]=pygame.transform.scale(pygame.image.load("textures/emptyslider.png"),(tilew*11,tileh*1))
    textures["dot"]=pygame.transform.scale(pygame.image.load("textures/dot.png"),((tilew),(tileh)))
    textures["OK"]=textures["fontsplit"].render(f"OK",False,(255,255,255))
    textures["split"]=textures["fontsplit"].render(f"Split stack",False,(0,0,0))
    for i in range(50):
        textures[f"num{i}"]=textures["font-/2.5"].render(f"{i}",False,(255,255,255))
    return textures