from flora.Grass import Grass
from flora.Rock import Rock
from flora.Dirt import Dirt
from flora.Tree import Tree
from fauna.Herbivore import Herbivore
from fauna.Predator import Predator
import random


class Map:
    def __init__(self):
        self.map = []
        self.x = 20
        self.y = 20

    def init_map(self):
        for i in range(self.x):
            generated_string = []
            for j in range(self.y):
                generated_string.append('🟫')
            self.map.append(generated_string)
        return self.map

    def set_grass(self, entities_counter):
        for i in range(entities_counter):
            coordinates = self.get_random_x_y()
            Grass(coordinates[0], coordinates[1], self.map).set_grass()
        return self.map

    def set_rocks(self, entities_counter):
        for i in range(entities_counter):
            coordinates = self.get_random_x_y()
            Rock(coordinates[0], coordinates[1], self.map).set_rock()
        return self.map

    def set_dirt(self, x, y):
        Dirt(x, y, self.map).set_dirt()
        return self.map

    def set_trees(self, entities_counter):
        for i in range(entities_counter):
            coordinates = self.get_random_x_y()
            Tree(coordinates[0], coordinates[1], self.map).set_tree()
        return self.map

    def set_herbivores(self, entities_counter):
        for i in range(entities_counter):
            coordinates = self.get_random_x_y()
            Herbivore(coordinates[0], coordinates[1], self.map).set_herbivore()
        return self.map

    def set_predators(self, entities_counter):
        for i in range(entities_counter):
            coordinates = self.get_random_x_y()
            Predator(coordinates[0], coordinates[1], self.map).set_predator()
        return self.map

    def get_random_x_y(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        return [x, y]
