import pickle

import server
from boy import Boy
from background import FixedBackground as Background

objects = [[] for _ in range(4)]
collision_pairs = {}


def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    global objects, collision_pairs

    objects = [[] for _ in range(4)]
    collision_pairs = {}


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collisions():
    collided_pairs = []
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    collided_pairs.append((group, a, b))
    for group, a, b in collided_pairs:
        a.handle_collision(group, b)
        b.handle_collision(group, a)


def all_objects():
    # fill here
    pass


def save():
    # fill here
    world = [objects, collision_pairs]
    with open('game.sav', 'wb') as f:
        pickle.dump(world, f)

def load():
    # fill here
    global objects, collision_pairs
    with open('game.sav', 'rb') as f:
        world = pickle.load(f)
    objects, collision_pairs = world[0], world[1]

    for layer in objects:
        for o in layer:
            if isinstance(o, Boy):
                server.boy = o
            elif isinstance(o, Background):
                server.background = o