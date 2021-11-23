from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
hand_x, hand_y = 0, 0


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def running_move():
    global x, y

    while True:
        if x == hand_x and y == hand_y:
            break

        elif x != hand_x:
            if x > hand_x:
                x -= 1
            elif x < hand_x:
                x += 1

        elif y != hand_y:
            if y > hand_y:
                y -= 1
            elif y < hand_y:
                y += 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_x, hand_y = random.randint(0, 1280), random.randint(0, 1024)
    hand.draw(hand_x, hand_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    running_move()
    handle_events()
