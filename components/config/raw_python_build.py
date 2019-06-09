from components.logic.universe import Universe
from components.tools.interface import GameInterface

class Manager:
    def __init__(self):
        self.interface = GameInterface()

    def manage(self):
        self.interface.run()
        
       