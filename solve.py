from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
from charles.crossover import cross_extrems,co_singlepoint, cycle_co, pmx
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament, roulette, rank
from charles.GA import GA
from operator import attrgetter
import numpy as np
import pandas as pd
import timeit

sudoku_grid = grid
optimization = 'max'

#Population size definition
pop_size = 2500


#GA parameters decision
co_percent = 0.97
mut_percent = 0.01
mut_option1 = swap_mutation
mut_option2 = mutation

elitism = 0.3


sel_list = [tournament, roulette, rank]
cross_list = [pmx,cycle_co,co_singlepoint]
elitism_list=[0,0.3]
permutations = []
for x in sel_list:
    for y in cross_list:
        for e in elitism_list:
            permutations.append([x,y,e])

# define monkey patch of the charles functions
if optimization == 'min':
    Individual.fitness = fitness_min
else:
    Individual.fitness = fitness_max

Individual.get_neighbours = get_neighbour

result_table = pd.DataFrame()

for index, combination in enumerate(permutations):
    
    test_number = 0
    while test_number < 30:
        
        #initial population
        pop = Population(
                    size=pop_size,
                    optim=optimization,
                    grid=sudoku_grid
                )

        #fazer o loop para conseguir chegar a fitness igual a zero
        count = 0
        start = 0
        stop = 0

        #laço para encontrar o fitness
        while count <= 40:
            
            # pega o indivíduo com o melhor fitness
            if pop.optim == 'min':
                best_fit = min(pop, key=attrgetter("fitness"))
            elif pop.optim == 'max':
                best_fit = max(pop, key=attrgetter("fitness"))

            print('permutation',index+1,'test_number',test_number, ', count:', count,', Fitness: ',best_fit.fitness,',Diversity: ',pop.variance())
            
            new_row = pd.DataFrame({'combination': [index+1],
                                    'test_number': [test_number+1],
                                    'co_option':[combination[1].__name__],
                                    'selec_option':[combination[0].__name__],
                                    'elitism': [combination[2]],
                                    'best fit':[best_fit.fitness],
                                    'count': [count+1],
                                    'variance':[pop.variance()],
                                    'time': [stop - start]})

            result_table = pd.concat([result_table,new_row], ignore_index=True)

            if pop.optim =='min' and best_fit.fitness==0:
                print(np.abs(best_fit.solution))
                break
            elif pop.optim =='max' and best_fit.fitness==243:
                print(np.abs(best_fit.solution))
                break

            start = timeit.default_timer()
            
            #inicializa a nova população de offspring
            off_pop = Population(0,optimization,grid)
            
            if combination[2] > 0:
                # Armazenar a porcentagens de novos indivíduos
                eli_number = int(pop_size*combination[2])

                #orderna população do elitismo de acordo com o optimization
                eli_pop_sort = sorted(pop.individuals, key=lambda x:x.fitness, reverse=pop.optim == 'max')

                #adiciona a população do elitismo de acordo com a ordem
                off_pop.individuals.extend(eli_pop_sort[:eli_number])

            #completa o resto da população com GA
            while len(off_pop) < pop_size:
                off_pop.individuals.extend(GA(pop, co_percent, mut_percent, combination[0], combination[1], mut_option1, mut_option2))

            #a população de offspring vira a nova parent population
            pop = off_pop

            stop = timeit.default_timer()

            count += 1
        
        test_number += 1


result_table.to_excel("results.xlsx")  


