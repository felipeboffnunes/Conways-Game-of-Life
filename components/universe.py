from .cell import Cell

class Universe:
    def __init__(self, x_size:int, y_size:int):
        self.x_size = x_size
        self.y_size = y_size
        self.seed = [[]*x_size]*y_size

    def fate(self, cell, current_universe):
        coordinates = cell.x, cell.y
        print(coordinates)
        def rule_1():
            return False
        
        def rule_2():
            return True

        def rule_3():
            return False

        def rule_4():
            return True

        if cell.state:
            cell.state = rule_1() or rule_2() or rule_3()
        else:
            cell.state = rule_4()
        new_state = False
        return new_state
        
    def iterate(self):
        current_universe = self.seed
        update = lambda cell, current_universe: self.fate(cell, current_universe)
        self.seed = [[update(current_universe[row][cell], current_universe) \
                    for cell in range(len(current_universe[row]))] \
                    for row in range(len(current_universe))]
        print(self.seed)

    def start(self):
        generate = lambda x, y: Cell(x, y, False)
        self.seed = [[generate(cell, row) \
                    for cell in range(self.x_size)] \
                    for row in range(self.y_size)]
        print(self.seed)
        

