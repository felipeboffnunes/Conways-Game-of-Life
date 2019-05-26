from .cell import Cell

class Universe:
    def __init__(self, x_size:int, y_size:int):
        self.x_size = x_size
        self.y_size = y_size
        self.seed = [[0]*x_size]*y_size
        
    def populate(self):
        cell = Cell(9,9,0)
        print(cell)

    def iterate(self):
        state = self.seed
