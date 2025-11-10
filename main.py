from classes import *
keylogesc=0
while True:
    if keylogesc>=1:
        keylogesc-=1
    window.fill((0,0,0))
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()