from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


while(1):
    x = 0
    y = 90
    
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.001)

    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.001)

    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.001)

    while(y > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.001)

# 사각형 운동 완성

    clear_canvas_now()
    t = 0


    while(t < 720):
        clear_canvas_now()
        x = 400 + math.sin(t / 360 * math.pi) * 210
        y = 300 - math.cos(t / 360 * math.pi) * 210
        grass.draw_now(400,30)
        character.draw_now(x,y)
        t = t + 2
        delay(0.001)


close_canvas()
