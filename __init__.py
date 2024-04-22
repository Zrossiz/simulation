from Map import Map


my_map = Map()
my_map.init_map()
my_map.set_grass()
my_map.set_dirt()
result = my_map.set_rocks()


for i in range(20):
    for j in range(20):
        print(result[i][j], end="")
    print()
