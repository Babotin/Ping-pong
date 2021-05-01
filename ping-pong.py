from pygame import *

w = 1000
h = 700

window = display.set_mode((w, h))

class GameSprite(sprite.Sprite):
    def __init__(self, file, W, H, x, y, speed_x, speed_y):
        #sprite.Sprite.__init__(self)
        super().__init__()
        self.file = image.load(file)
        self.file = transform.scale(self.file, (W, H))
        self.rect = self.file.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def draw(self):
        window.blit(self.file, self.rect)

class Ball(GameSprite):
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x > w - 40 or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y > h - 40 or self.rect.y < 0:
            self.speed_y *= -1

ball = Ball("ball.png", 40, 40, w / 2, h / 2, 6, 6)

clock = time.Clock()

game = True
while game:
    window.fill((0, 150, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.move()
    ball.draw()
    display.update()
    clock.tick(50)
