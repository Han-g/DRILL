from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
SHOOT_SPEED_KMPH = 120.0
SHOOT_SPEED_MPM = (SHOOT_SPEED_KMPH * 1000.0 / 60.0)
SHOOT_SPEED_MPS = (SHOOT_SPEED_MPM / 60.0)
SHOOT_SPEED_PPS = (SHOOT_SPEED_MPS * PIXEL_PER_METER)

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = SHOOT_SPEED_PPS):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, SHOOT_SPEED_PPS

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        print(self.velocity, SHOOT_SPEED_PPS)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
