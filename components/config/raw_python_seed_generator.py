from components.logic.cell import Cell

def create_seed(id, simulation_status):
    seed = []
    for row_id, row_status in zip(id, simulation_status):
        cell_row = []
        for i in range(len(row_id)):
            c = Cell(i, int(row_id[i]) , row_status[i])
            cell_row.append(c)
        seed.append(cell_row)

    return seed
