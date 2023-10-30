import pico2d
from pico2d import delay, close_canvas, open_canvas
import logo_mode as start_mode
# import title_mode as start_mode
import game_framework

open_canvas()
game_framework.run(start_mode)
close_canvas()