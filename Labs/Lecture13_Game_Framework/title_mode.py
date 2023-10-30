from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time, SDL_KEYDOWN,  SDLK_ESCAPE, SDLK_SPACE
import game_framework
import play_mode


def init():
    global image
    global running
    global logo_start_time

    running = True
    image = load_image('title.png')
    logo_start_time = get_time()
    pass

def finish():
    pass

def update():
    global running
    if get_time() - logo_start_time >= 2.0:
        game_framework.quit()
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)
    pass