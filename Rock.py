class Rock:
    def __init__(self, x, y, map_instance):
        self.x = x
        self.y = y
        self.map_instance = map_instance

    def set_rock(self):
        self.map_instance[self.x][self.y] = '🪨'
        return self.map_instance
