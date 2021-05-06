from pygame import *
from random import randint


back  = (200, 255, 255)
win_width = 600
win_width = 500
window = display.set_mode((win_width, win_width))
window.fill(back)

game = True 
finish = False
clock = time.Clock()
FPS = 60

while game: 
    for e in event.get ():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)


    display.update()
    clock.tick(FPS)