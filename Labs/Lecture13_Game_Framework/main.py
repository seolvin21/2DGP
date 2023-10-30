import pico2d
from pico2d import delay, close_canvas, open_canvas
import logo_mode

open_canvas()
logo_mode.init()
# game loop
while logo_mode.running:
    logo_mode.handle_events()
    logo_mode.update()
    logo_mode.draw()
    delay(0.01)

logo_mode.finish()
# finalization code
close_canvas()