from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
from charles.crossover import co_singlepoint,cycle_co, pmx
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament, roulette, rank
from charles.GA import GA
from operator import attrgetter
import numpy as np
import pandas as pd
import timeit

#get the sudoku puzzle 
sudoku_grid = grid

#Population size definition
pop_size = 5000

#define a sudoku'd first solution initialization function
Individual.get_neighbours = get_neighbour

#optimization type of the fitness function
optimization = 'max'

#define the fitness function based in the optimization type
if optimization == 'min':
    Individual.fitness = fitness_min
else:
    Individual.fitness = fitness_max

#Genetic Operators parameters decision
co_percent = 0.97
mut_percent = 0.01
mut_option1 = swap_mutation
mut_option2 = mutation

#list with combinations of Genetic Operators
sel_list = [tournament, roulette, rank]
cross_list = [pmx,cycle_co,co_singlepoint]
elitism_list=[0,0.3]
permutations = []
for x in sel_list:
    for y in cross_list:
        for e in elitism_list:
            permutations.append([x,y,e])

#create a empty dataframe to store the results
result_table = pd.DataFrame()

#iterator over every combination of Genetic Operators
for index, combination in enumerate(permutations):
    
    #for each combination of Genetic Operators run 30 iterations
    test_number = 0
    while test_number < 30:
        
        #initialize population
        pop = Population(
                    size=pop_size,
                    optim=optimization,
                    grid=sudoku_grid
                )

        count = 0
        start = 0
        stop = 0

        #loop for 40 generations or until find the optimum fit
        while count <= 40:
            
            #get the individual with best fitness
            if pop.optim == 'min':
                best_fit = min(pop, key=attrgetter("fitness"))
            elif pop.optim == 'max':
                best_fit = max(pop, key=attrgetter("fitness"))

            print('permutation',index+1,'test_number',test_number, ', count:', count,', Fitness: ',best_fit.fitness,',Diversity: ',pop.variance())
            
            #store the best fitness in the results table
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

            #stops loop if the optimum solution is found
            if pop.optim =='min' and best_fit.fitness==0:
                print(np.abs(best_fit.solution))
                break
            elif pop.optim =='max' and best_fit.fitness==243:
                print(np.abs(best_fit.solution))
                break

            start = timeit.default_timer()
            
            #initialize the offspring population
            off_pop = Population(0,optimization,grid)
            
            #if elitims is greater than 0
            if combination[2] > 0:
                #define the number of individuals that are the elit
                eli_number = int(pop_size*combination[2])

                #sort the population based in the fitness
                eli_pop_sort = sorted(pop.individuals, key=lambda x:x.fitness, reverse=pop.optim == 'max')

                #add in the new offspring population the number of indiciduals that are elit accorinding to the previews sort
                off_pop.individuals.extend(eli_pop_sort[:eli_number])

            #loop over evolution process until the population of the offspring is the same size of the parent population
            while len(off_pop) < pop_size:
                off_pop.individuals.extend(GA(pop, co_percent, mut_percent, combination[0], combination[1], mut_option1, mut_option2))

            #the offspring population becames the new parent population
            pop = off_pop

            stop = timeit.default_timer()

            count += 1
        
        test_number += 1

#save results to a excel table
result_table.to_excel("results5000.xlsx")  

