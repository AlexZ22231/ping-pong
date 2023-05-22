from pygame import *

win_width = 700 
win_height = 500 

window = display.set_mode(
(win_width, win_height)
)
display.set_caption("Ping-pong")
background = transform.scale(
image.load("background.png"), 
(win_width, win_height)
)

FPS = 60

clock = time.Clock()

run = True


while run:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False 
    clock.tick(FPS)
    display.update()
