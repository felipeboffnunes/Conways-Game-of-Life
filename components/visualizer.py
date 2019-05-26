def visualize_universe(universe_state, iteration):
    print("\n=========ITER {}=========".format(iteration))
    for row in universe_state:
        print([cell.state for cell in row])
    print("========================")