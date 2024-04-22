from Map import Map
import random

instance_map = Map()
instance_map.init_map()


def draw_map_with_entities():
    instance_map.set_grass(30)
    instance_map.set_rocks(20)
    instance_map.set_trees(20)
    instance_map.set_herbivores(6)
    instance_map.set_predators(4)


draw_map_with_entities()

for i in range(20):
    for j in range(20):
        print(instance_map.map[i][j], end="")
    print()
