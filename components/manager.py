from .universe import Universe

class Manager:
    def __init__(self, size, iterate_for):
        self.size = size
        self.iterate_for = iterate_for

    def manage(self):
        u = Universe(self.size, self.size)
        #u.start()
        for _ in range(self.iterate_for): u.iterate()