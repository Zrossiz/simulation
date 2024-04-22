from Grass import Grass
from Rock import Rock

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

    def set_grass(self):
        Grass(1, 2, self.map).set_grass()
        Grass(2, 1, self.map).set_grass()
        Grass(3, 4, self.map).set_grass()
        return self.map

    def set_rocks(self):
        Rock(8, 8, self.map).set_rock()
        Rock(10, 8, self.map).set_rock()
        Rock(12, 8, self.map).set_rock()
        Rock(14, 8, self.map).set_rock()
        return self.map


