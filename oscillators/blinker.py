from components.cell import Cell


def blinker():
    data = [[Cell(0, 0, False)]+ [Cell(0, 1, False)] + [Cell(0, 2, False)]] + \
        [[Cell(1, 0, True)] + [Cell(1, 1, True)] +[Cell(1, 2, True)]] + \
        [[Cell(2, 0, False)] +[Cell(2, 1, False)]+ [Cell(2, 2, False)]]
    return data
