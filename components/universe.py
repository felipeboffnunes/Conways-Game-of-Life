from .cell import Cell


class Universe:
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size
        self.seed = [[]*x_size]*y_size

    def fate(self, cell, current_universe):
        neighbours = current_universe[cell.x + 1][cell.y + 1], \
            current_universe[cell.x + 1][cell.y + 1], \
            current_universe[cell.x][cell.y + 1], \
            current_universe[cell.x - 1][cell.y + 1], \
            current_universe[cell.x + 1][cell.y], \
            current_universe[cell.x + 1][cell.y - 1], \
            current_universe[cell.x - 1][cell.y], \
            current_universe[cell.x - 1][cell.y - 1]

        neighbours_alive = [cell.state for cells in neighbours]
        print(neighbours_alive)

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

        if cell.state:
            cell.state = rule_1() or rule_2() or rule_3()
        else:
            cell.state = rule_4()
        new_state = False
        return new_state

    def iterate(self):
        current_universe = self.seed
        def update(cell, current_universe): return self.fate(
            cell, current_universe)
        self.seed = [[update(current_universe[row][cell], current_universe)
                      for cell in range(self.x_size)]
                     for row in range(self.y_size)]
        print(self.seed)

    def start(self):
        def generate(x, y): return Cell(x, y, False)
        self.seed = [[generate(cell, row)
                      for cell in range(self.x_size)]
                     for row in range(self.y_size)]
        print(self.seed)
