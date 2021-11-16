import game_framework
from pico2d import *
import random
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Move:
    def enter(bird):
        bird.frame = 0

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time

    def draw(bird):
        if bird.velocity == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(100, 300)
        self.image = load_image('bird100x100x14.png')
        self.velocity = 0
        self.frame = 0

    def update(self):
        Move.do(self)

    def draw(self):
        Move.draw(self)

    def handle_event(self, event):
        pass
