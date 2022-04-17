'import numpy as np
import random
import sys

startingSudoku = """
                    530070000
                    600195000
                    098000060
                    800060003
                    400803001
                    700020006
                    060000280
                    000419005
                    000080079
                """'

grid = np.array([[int(i) for i in line] for line in startingSudoku.split()])

solution1 = [5, 3, 4, 6, 7, 8, 9, 1, 2]

error2 = [5, 3, 5, 6, 7, 8, 9, 1, 2]

def get_neighbour():
    solution = []
    for i in range(0,9):
        element = random.randint(0,9)
        solution.append(element)
    return solution

#define the solutions of a spot
def evaluation(row, column, solution):
    global grid #work outside function while working in the function

    fitness_row = 0
    #Is the number in the row?
    for element in solution:
        for i in range(0,9): #column of the row
            print(grid[row][i],row,i, element)
            if grid[row][i] == element: #the number that we are guessing exists in this row?
                fitness_row += element

    ff_row = fitness_row - sum(grid[row])

    fitness_column = 0
    #Is the number in the column?
    for element in solution:
        for j in range(0,9): #column of the row
            print(grid[j][column],row,j, element)
            if grid[row][j] == element: #the number that we are guessing exists in this row?
                fitness_column += element

    ff_column = fitness_column - sum(grid[column])

    print(solution)

    #Is the number in the square?
    # fitness_square = 0
    # for element in solution():
    #     x0 = (column // 3) * 3
    #     y0 = (row // 3) * 3
    #
    #     for i in range(0,3):
    #         for j in range(0,3):
    #             if grid[y0+i][x0+j] == element:
    #                 fitness_square += element
    # ff_square = fitness_square #- sum(grid[y0+i][x0+j])

    final_fitness = ff_row + ff_column
    print(final_fitness)

#evaluation(1,1,error2)


def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if evaluation(row,column, number):
                        solve()
                        grid[row][column] = 0
                return


    # print(np.matrix(grid))
    # input('More possible solutions')
pass

#print("Python Recursive Limitation = ", sys.getrecursionlimit())