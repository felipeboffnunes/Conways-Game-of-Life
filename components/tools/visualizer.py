import matplotlib.pyplot as plt
import numpy as np
STATES = []

def visualize_universe(universe_state, iteration):
    universe = []
    
    print("\n=========ITER {}=========".format(iteration))
    for row in universe_state:
        aux_row = []
        for cell in row:

            if cell.state:
                aux_row.append(1)
            else:
                aux_row.append(0)
        universe.append(aux_row)
    
    universe = np.matrix(universe)
    print(universe)
    print("========================")
    STATES.append(universe)
  
def plot_states():
    global STATES
    for state in STATES:
        plt.imshow(state, cmap='gray')
        plt.show()
    STATES = []