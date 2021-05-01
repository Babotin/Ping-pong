from pygame import *

w = 1000
h = 700

window = display.set_mode((w, h))

clock = time.Clock()

game = True
while game:
    window.fill((0, 150, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(50)
