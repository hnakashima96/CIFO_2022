import numpy as np
import random

def get_neighbour(self):
    '''
        This function takes a Sudoku generated from the sudoku_grid function and fill up each row at the time with the possible combinations 
        of numbers that won't creat duplicates in the row.

        The numbers will be filled up in the Sudoku as negative in order to differenciate them from the already given numbers in the sudoku.
    
    '''
    init_grid = np.copy(self)
   
    #for each line in sudoku
    for i in range(9):
       #create a list with the missing numbers in the range 1-9 for that row
       fixed = [-x for x in range(1,10) if x not in set(init_grid[i,:])]
       #suffle the oreder of the numbers
       random.shuffle(fixed)
       #fill the row in the order of the suffled list
       np.place(init_grid[i,:], init_grid[i,:]==0, fixed)

    return init_grid

def split(array, nrows, ncols):
    '''
        This function divide the 9x9 Sudoku grid in 3x3 sub grids that are used to evaluate
        the solution
    '''
    h = array.shape[1]
    return (array.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols))


def fitness_min(prob_sol):
    '''
        This function count the number of duplicates in columns and sub-grids of the Sudoku. Due the way 
        Sudokus are being initialized in the get_neighbour function rows already have 0 number of duplicate
    '''
    prob_sol = np.abs(prob_sol)

    total_fit = 0

    #loop to count the number of duplicates in each column
    for i in range(9):
        counts_row = np.unique(prob_sol[:,i], return_counts=True)[1] 
        counts_column = np.unique(prob_sol[i,:], return_counts=True)[1]
        total_fit += sum(counts_row-1) + sum(counts_column-1)

    #generate a list with the sub-grids of the sudoku
    sub_matrix = split(prob_sol,3,3)

    #loop to count the number of duplicates in each sub-grid
    for i in sub_matrix:
        counts = np.unique(i, return_counts=True)[1]
        total_fit += sum(counts-1)

    return total_fit

def fitness_max(prob_sol):
    '''
        This function count the number of unique values in columns and sub-grids of the Sudoku. Due the way 
        Sudokus are being initialized in the get_neighbour function rows already have 9 unique values
    '''
    prob_sol = np.abs(prob_sol)

    total_fit = 0

    #loop to count the number of unique values in each column
    for i in range(9):
        total_fit += len(set(prob_sol[:,i])) + len(set(prob_sol[i,:]))


    #generate a list with the sub-grids of the sudoku
    sub_matrix = split(prob_sol,3,3)

    #loop to count the number of unique in each sub-grid
    for i in sub_matrix:
        unique = np.unique(i)
        total_fit += len(unique)

    return total_fit



