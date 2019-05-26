from .cell import Cell

class Universe:
    def __init__(self, x_size:int, y_size:int):
        self.x_size = x_size
        self.y_size = y_size
        self.seed = [[Cell(state=False)]*x_size]*y_size

    def fate(self, cell, current_state):
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
        
        return False
        
    def iterate(self):
        current_state = self.seed
        generate = lambda cell, current_state: self.fate(cell, current_state)
        self.seed = [[generate(current_state[row][cell], current_state) for cell in range(len(current_state[row]))] for row in range(len(current_state))]
        print(self.seed)
        

