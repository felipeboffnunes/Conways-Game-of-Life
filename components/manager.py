from .universe import Universe
from .interface import GameInterface

class Manager:
    def __init__(self):
        self.interface = GameInterface()

    def manage(self):
        self.interface.run()
        
       