from .cell import Cell
from .visualizer import visualize_universe


class Universe:
    def __init__(self, x_size: int, y_size: int, seed):
        self.x_size = x_size
        self.y_size = y_size
        self.seed = seed
        self.iterations = 0

    def fate(self, cell, current_universe):
        # Adding manual Padding
        padded_universe = [[Cell(-1, -1, False)]*(self.x_size + 2)] + \
            [[Cell(-1, -1, False)] + current_universe[row] + [Cell(-1, -1, False)] for row in range(self.y_size)] + \
            [[Cell(-1, -1, False)]*(self.x_size+2)]

        new_x = cell.x + 1
        new_y = cell.y + 1
        
        # Checking neighbours
        neighbours = padded_universe[new_y + 1][new_x + 1], \
            padded_universe[new_y][new_x + 1], \
            padded_universe[new_y - 1][new_x + 1], \
            padded_universe[new_y + 1][new_x], \
            padded_universe[new_y-1][new_x], \
            padded_universe[new_y + 1][new_x - 1], \
            padded_universe[new_y][new_x - 1], \
            padded_universe[new_y - 1][new_x - 1]

        neighbours_alive = sum(int(cell.state) for cell in neighbours)


        def rule_1():
            if neighbours_alive < 2:
                return False

        def rule_2():
            if neighbours_alive == 2 or neighbours_alive == 3:
                return True

        def rule_3():
            if neighbours_alive > 3:
                return False

        def rule_4():
            if neighbours_alive == 3:
                return True
            return False

        new_state = False
        if cell.state:
            new_state = rule_1() or rule_2() or rule_3()
        else:
            new_state = rule_4()

        if new_state == None:
            new_state = False
        
        return new_state

    def iterate(self):
        current_universe = self.seed
        visualize_universe(current_universe, self.iterations)
        def update(cell, current_universe): return self.fate(
            cell, current_universe)
        aux = [[Cell(cell, row, update(current_universe[row][cell], current_universe))
                for cell in range(self.x_size)]
               for row in range(self.y_size)]
        self.iterations += 1
        visualize_universe(aux, self.iterations)
        self.seed = aux

    def start(self):
        def generate(x, y): return Cell(x, y, False)
        self.seed = [[generate(cell, row)
                      for cell in range(self.x_size)]
                     for row in range(self.y_size)]
        visualize_universe(self.seed, self.iterations)
