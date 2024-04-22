from fauna.Creature import Creature


class Predator(Creature):
    def __init__(self, x, y, map_instance):
        super().__init__()
        self.x = x
        self.y = y
        self.map_instance = map_instance

    def set_predator(self):
        self.map_instance[self.x][self.y] = '🦊'
        return self.map_instance
