from flora.Grass import Grass
from flora.Rock import Rock
from flora.Dirt import Dirt

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
        Grass(x, y, self.map).set_grass()
        Grass(x, y, self.map).set_grass()
        Grass(x, y, self.map).set_grass()
        return self.map

    def set_rocks(self, x, y):
        Rock(x, y, self.map).set_rock()
        Rock(x, y, self.map).set_rock()
        Rock(x, y, self.map).set_rock()
        Rock(x, y, self.map).set_rock()
        return self.map

    def set_dirt(self, x, y):
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        Dirt(x, y, self.map).set_dirt()
        return self.map




