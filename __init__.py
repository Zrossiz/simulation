from Map import Map


my_map = Map()
my_map.init_map()
result = my_map.set_grass(1, 2)

for i in range(20):
    for j in range(20):
        print(result[i][j], end="")
    print()
