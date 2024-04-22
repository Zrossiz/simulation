class Map:

    def __init__(self):
        self.map = []
        self.x = 20
        self.y = 20

    def init_map(self):
        for i in range(self.x):
            for j in range(self.y):
                print('🍀', end='')
            print()


