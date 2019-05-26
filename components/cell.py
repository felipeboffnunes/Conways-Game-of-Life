class Cell:
    def __init__(self, x:int, y:int, state:bool):
        self.x = x
        self.y = y
        self.state = state

    def die(self):
        self.state = False

    def live(self):
        self.state = True