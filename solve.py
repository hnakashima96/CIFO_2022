from Sudoku.data_sudoku import grid
from Sudoku.functions_2 import get_neighbour, fitness
from charles.charles import Population, Individual
from charles.GA import GA
from operator import attrgetter
import numpy as np

sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour

pop_size = 100

#initial population
pop = Population(
            size=pop_size,
            optim='min',
            grid=sudoku_grid
        )

#valida se nenhum dos individuos inicializados já é a solução final
solution = 0
flag_sucesso = False
if min(pop, key=attrgetter("fitness")).fitness == 0:
    flag_sucesso = True
    solution = min(pop, key=attrgetter("fitness"))

#fazer o loop para conseguir chegar a fitness igual a zero
count = 0
while flag_sucesso == False:
    
    #inicializa a nova população de offspring
    off_pop = Population(0,'min',grid)
    
    #loop até a off_pop tiver o tamanho da parent pop
    while len(off_pop) < pop_size:
        off_pop.individuals.extend(GA(pop))
    
    #a população de offspring vira a nova parent population
    pop = off_pop

    #pega o indivíduo com o menor valor de fitness
    best_fit = min(pop, key=attrgetter("fitness"))

    print('count:', count,', Fitness Mínimo',best_fit.fitness)

    if best_fit.fitness==0:
        print(np.abs(best_fit.solution))
        break

    count += 1
    if  count > 1000:
        print("more than ",{count}," interations, pass limited time")
        break