class Npc:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

yuri = Npc('yuri', 100, 200)
print(type(yuri.__dict__))
print(yuri.__dict__)