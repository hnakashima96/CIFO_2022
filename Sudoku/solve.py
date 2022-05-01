from Sudoku.data_sudoku import grid
from Sudoku.functions_2 import get_neighbour, fitness
from charles.charles import Population, Individual
from charles.GA import GA
import numpy as np
from charles.crossover import co_singlepoint

sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour

#fazer o loop para conseguir chegar a fitness igual a zero
pop = Population(
    size = 10,
    optim='min',
    grid = sudoku_grid
)
M = 5

#
# for i in range(10):
#     print(pop.individuals[i])
#     print(pop2.individuals[i])
pop2 = GA(pop,M)

#print(p1_index, p2_index, offspring1, offspring2)
#print(pop.individuals)

# print(p2 == offspring2)


#print(p.individuals)
#
# print(type(p))


#crossover check in
# for i in range(9):
#     print(p1.solution[i],offspring1[i])
# print('////')
# for i in range(9):
#     print(p2.solution[i],offspring2[i])
#
for i in range(10):
    print(i,pop1.individuals[i],pop2.individuals[i])