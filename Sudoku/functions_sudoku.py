import numpy as np
from data_sudoku import startingSudoku, sudoku

#the grid visualization
def PrintSudoku(sudoku):
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i,j])+" "
        print(line)


def FixSudokuValues(fixed_sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if fixed_sudoku[i, j] != 0:
                fixed_sudoku[i, j] = 1

    return (fixed_sudoku)
