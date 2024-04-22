from Grass import Grass


class Map:
    def __init__(self):
        self.map = []
        self.x = 20
        self.y = 20

    def init_map(self):
        for i in range(self.x):
            generated_string = []
            for j in range(self.y):
                generated_string.append('#')
            self.map.append(generated_string)
        return self.map

    def set_grass(self, x, y):
        grass_instance = Grass(x, y, self.map)
        return grass_instance.set_grass()

