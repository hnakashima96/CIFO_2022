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
- -c: Available options for crossover: pmx,cycle_co,co_singlepoint
- -s: Available options for selection: tournament, roulette, rank
- -e: Elitism should be a float number between 0 and 1
- -o: Available options for optimization type: min, max
- -p: Population should be a integer number

- If you add more than one option for crossover, selection or elitism the program will run all the permutation of these choices.

example:

python solve.py -c pmx -c co_singlepoint -s rank -e 0.5 -e 0 -o min -p 100

for this example the program would run all the combinations for the 2 types of crossover (pmx and co_singlepoint), 1 selection method (rank), 2 elitism options (0.5 and 0), minimization type of optimization and population of 100.

## Output:

The program will run 40 generations 30 times for each combinations of the parameters passed in the solve.py

After running all the combinations a excel file will be saved in the same directory of the solve.py with the results of each generation on each iteration. The informations in the result excel:

combination: numer of the combination,
test_number: number of the interation,
co_option : name of the crossover option in this combination,
selec_option: name of the selection option in this combination,
elitism: value of the elitism in this combination,
best fit: best fit of the population for that generation,
count: generation number,
variance: variance whitin the population ,
time: time to run a full generation
