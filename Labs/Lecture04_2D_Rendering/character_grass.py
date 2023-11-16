from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

for x in range(0,800+1,2):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)

    delay(0.01)

close_canvas()
