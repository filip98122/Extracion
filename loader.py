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
    return textures
