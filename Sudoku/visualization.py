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


PrintSudoku(sudoku)


