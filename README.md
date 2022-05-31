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
 
## How to call the solve.py

The usage of the solve.py is like the following:

solve.py -c \<crossover name> -s \<selection name> -e \<elitism %> -o \<optimization type> -p \<population number>

where you can add as many crossover/selection names and elitism options taking into consideration:

- If you add more than one option for crossover, selection or elitism the program will run all the permutation of these choices.
- Available options for crossover: 'pmx','cycle_co','co_singlepoint'
- Available options for selection: 'tournament', 'roulette', 'rank'
- Elitism should be a float number between 0 and 1
- Available options for optimization type: 'min', 'max'
- Population should be a integer number
