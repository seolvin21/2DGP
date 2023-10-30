import pico2d
from pico2d import delay, close_canvas, open_canvas
import play_mode

open_canvas()
play_mode.init()
# game loop
while play_mode.running:
    play_mode.handle_events()
    play_mode.update()
    play_mode.draw()
    delay(0.01)

play_mode.finish()
# finalization code
close_canvas()