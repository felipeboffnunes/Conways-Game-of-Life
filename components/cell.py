class Cell:
    def __init__(self,state:bool):
        self.state = state

    def die(self):
        self.state = False

    def live(self):
        self.state = True