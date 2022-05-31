# CIFO_2022

This project is the deliverable of Computational Intelligence for Optimization subject from University NOVA de Lisboa IMS 

The main goal is to use Genetic Algorithms to solve a sudoku puzzle.

The project is coded in python.

Libraries need to run the code and results:

- Python installed with those libraries:
  * numpy
  * scipy
  * operator
  * math
  * intertools
  * operator
  * pandas
  * timeit
  * random
  * statistics

The project is dividev into 4 parts in this repository:

Folder Sudoku is composed by two main files .py:
- data_sudoku.py: the user add a Sudoku grid, where the empty spaces are returned as zeros
- functions.py: this file merge all the functions to identify the problem itself.
  * get_neighbour: to initialize the indiviuals of a population
  * split: to split the sudoku grid into a list of submatrixes 
  * fitness_min: fitness function to a minimization problem
  * fitness_max: fitness function to a maximization problem
  
Folder Charles is composed by five main files .py:
- Charles.py: there are the classes to create a Population and Individidual of this population
- Crossover.py: crossover functions developed (single point, parallel mapped and cycle)
- mutation.py: mutation functions developed (mutation and swap_mutation)
- selection.py: selection functions developed (roullete, rank and tournament)
- GA.py: function which merge all the information above to make possible to solve the problem.
 
 Outside the folder has the third and forth part of the project:
 
 solve.py: is the code which combine the problem and the Genetic Algorithm in order to solve.
 
 