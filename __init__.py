from Map import Map
import random

my_map = Map()
my_map.init_map()


def draw_map_with_entities():
    for x_map in range(20):
        for y_map in range(20):
            my_map.set_dirt(x_map, y_map)

    for r in range(6):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        my_map.set_rocks(x, y)

    for g in range(12):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        my_map.set_grass(x, y)


draw_map_with_entities()


for i in range(20):
    for j in range(20):
        print(my_map.map[i][j], end="")
    print()
