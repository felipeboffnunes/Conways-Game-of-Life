from components.universe import Universe

def main():
    print("Welcome to Conway's Game of Life, built in Python by Felipe Boff Nunes at 25/05/2019")
    universe = Universe(2,2)
    universe.start()
if __name__ == "__main__":
    main()