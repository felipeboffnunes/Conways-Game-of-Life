from components.universe import Universe

def main():
    print("Welcome to Conway's Game of Life, built in Python by Felipe Boff Nunes at 25/05/2019")
    universe = Universe(10,10)
    universe.populate()
if __name__ == "__main__":
    main()