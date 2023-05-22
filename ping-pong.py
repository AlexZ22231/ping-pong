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
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (21,139))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y)
        self.speed = player_speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -139:
            self.rect.y += self.speed
    def update_l(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < win_height -139:
                self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y):
        super().__init__(player_image, player_x, player_y)
        self.image = transform.scale(image.load(player_image), (35,35))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if  self.rect.y < 4 or self.rect.y > win_height-50:
                self.speed_y *= -1
        if self.rect.x > win_width-20 or ball.rect.x < 0:
            self.speed_x *= -1
    def change_direction(self):
        self.speed_x *= -1







FPS = 60
clock = time.Clock()

run = True

player_right = Player('rocket right.png', 650,300, 5)
player_left = Player('rocket left.png', 30,300, 5)
ball = Ball('ball.png', 350,250,3,3)
while run:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False 
    player_right.update_r()
    player_left.update_l()
    ball.update()
    if sprite.collide_rect(player_left,ball) or sprite.collide_rect(player_right,ball):
        ball.change_direction()
    ball.reset()
    player_right.reset()
    player_left.reset()
    clock.tick(FPS)
    display.update()
