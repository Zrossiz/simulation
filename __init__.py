from Map import Map
import random

my_map = Map()
my_map.init_map()


def draw_map_with_entities():
    for x_map in range(20):
        for y_map in range(20):
            my_map.set_dirt(x_map, y_map)

    for r in range(12):
        coordinates = get_random_x_y()
        my_map.set_rocks(coordinates[0], coordinates[1])

    for g in range(12):
        coordinates = get_random_x_y()
        my_map.set_grass(coordinates[0], coordinates[1])

    for t in range(6):
        coordinates = get_random_x_y()
        my_map.set_tree(coordinates[0], coordinates[1])

    for h in range(8):
        coordinates = get_random_x_y()
        my_map.set_herbivore(coordinates[0], coordinates[1])

    for p in range(3):
        coordinates = get_random_x_y()
        my_map.set_predator(coordinates[0], coordinates[1])


def get_random_x_y():
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    return [x, y]


draw_map_with_entities()

for i in range(20):
    for j in range(20):
        print(my_map.map[i][j], end="")
    print()
