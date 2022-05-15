from audioop import avg
from statistics import mean
from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
from charles.crossover import co_singlepoint,cross_extrems,co_singlepoint_linear_inversion,cycle_co, pmx
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament
from charles.GA import GA
from operator import attrgetter
import numpy as np
import timeit

sudoku_grid = grid
optimization = 'min'

pop_size = 1000

#GA parameters decision

co_percent = 0.95
mut_percent = 0.01
selec_option = tournament
co_option = pmx
mut_option1 = swap_mutation
mut_option2 = swap_mutation
elitism = True


# define monkey patch of the charles functions
if optimization == 'min':
    Individual.fitness = fitness_min
else:
    Individual.fitness = fitness_max

Individual.get_neighbours = get_neighbour

#initial population
pop = Population(
            size=pop_size,
            optim=optimization,
            grid=sudoku_grid
        )

#valida se nenhum dos individuos inicializados já é a solução final
solution = 0
flag_sucesso = False
if pop.optim =='min' and min(pop, key=attrgetter("fitness")).fitness == 0:
    flag_sucesso = True
    solution = min(pop, key=attrgetter("fitness"))
elif pop.optim =='max' and min(pop, key=attrgetter("fitness")).fitness==243:
    flag_sucesso = True
    solution = min(pop, key=attrgetter("fitness"))

#fazer o loop para conseguir chegar a fitness igual a zero
count = 0
start = timeit.default_timer()
while flag_sucesso == False:
    
    #inicializa a nova população de offspring
    off_pop = Population(0,optimization,grid)
    
    #loop até a off_pop tiver o tamanho da parent pop
    while len(off_pop) < pop_size:

        off_pop.individuals.extend(GA(pop, co_percent, mut_percent,selec_option, co_option, mut_option1, mut_option2, elitism))
    
    #a população de offspring vira a nova parent population
    pop = off_pop

    #pega o indivíduo com o menor valor de fitness
    best_fit = min(pop, key=attrgetter("fitness"))

    if pop.optim =='min' and best_fit.fitness==0:
        print(np.abs(best_fit.solution))
        print('count:', count)
        flag_sucesso = True
    elif pop.optim =='max' and best_fit.fitness==243:
        print(np.abs(best_fit.solution))
        print('count:', count)
        flag_sucesso = True

    count += 1

    print('count:', count,', Fitness: ',best_fit.fitness,',Diversity: ',pop.variance())


stop = timeit.default_timer()

print('Time: ', stop - start,'s')  

# cycle cross over pg 86
# partily matched cross over
# diversity measure
# fitness sharing pg75