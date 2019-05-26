from components.manager import Manager

SIZE = 5
N_ITERATIONS = 10

def main():
    print("Welcome to Conway's Game of Life, built in Python by Felipe Boff Nunes at 25/05/2019")
    Manager(size=SIZE, iterate_for=N_ITERATIONS)
if __name__ == "__main__":
    main()