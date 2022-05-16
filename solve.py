from audioop import avg
from statistics import mean
from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
from charles.crossover import co_singlepoint,cross_extrems,cycle_co, pmx
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament, tournament2
from charles.GA import GA
from operator import attrgetter
import numpy as np
import timeit

sudoku_grid = grid
optimization = 'max'

pop_size = 5000

#GA parameters decision

co_percent = 0.97
mut_percent = 0.01
selec_option = tournament
co_option = pmx
mut_option1 = mutation
mut_option2 = swap_mutation

#Quer elitismo? Identificar a porcentagem
elitism = 0

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

    if pop.optim == 'min':
        if elitism == 0:
            #inicializa a nova população de offspring
            off_pop = Population(0,optimization,grid)

            #loop até a off_pop tiver o tamanho da parent pop
            while len(off_pop) < pop_size:

                off_pop.individuals.extend(GA(pop, co_percent, mut_percent,selec_option, co_option, mut_option1, mut_option2))

            #a população de offspring vira a nova parent population
            pop = off_pop

            #pega o indivíduo com o menor valor de fitness
            best_fit = min(pop, key=attrgetter("fitness"))

        elif elitism > 0:
            # Armazenar a porcentagens de novos indivíduos
            eli_percent = int(pop_size*elitism)
            offspring_percent = int(pop_size*(1-elitism))

            #Criar população de elite
            eli_pop_sort = sorted(pop.individuals, key=lambda x:x.fitness)
            eli_pop = []

            for elite in eli_pop_sort:
                while len(eli_pop) < eli_percent:
                    eli_pop.append(elite)

            # inicializa a nova população de offspring
            off_pop = Population(0, optimization, grid)

            print('check-in 2',len(off_pop))
            # loop até a off_pop tiver o tamanho da parent pop
            while len(off_pop) < offspring_percent:
                off_pop.individuals.extend(
                    GA(pop, co_percent, mut_percent, selec_option, co_option, mut_option1, mut_option2))

            print('check-in 3',len(off_pop))
            # a população de offspring vira a nova parent population
            for elite in eli_pop:
                off_pop.individuals.append(elite)

            pop = off_pop

            print('check-in', len(pop))

            # pega o indivíduo com o menor valor de fitness
            best_fit = min(pop, key=attrgetter("fitness"))

    elif pop.optim == 'max':
        if elitism == 0:
            # inicializa a nova população de offspring
            off_pop = Population(0, optimization, grid)

            # loop até a off_pop tiver o tamanho da parent pop
            while len(off_pop) < pop_size:
                off_pop.individuals.extend(
                    GA(pop, co_percent, mut_percent, selec_option, co_option, mut_option1, mut_option2))

            # a população de offspring vira a nova parent population
            pop = off_pop

            # pega o indivíduo com o menor valor de fitness
            best_fit = max(pop, key=attrgetter("fitness"))

        elif elitism > 0:
            # Armazenar a porcentagens de novos indivíduos
            eli_percent = int(pop_size * elitism)
            offspring_percent = int(pop_size * (1 - elitism))

            # Criar população de elite
            eli_pop_sort = sorted(pop.individuals, key=lambda x: x.fitness)
            eli_pop = []

            for elite in eli_pop_sort:
                while len(eli_pop) < eli_percent:
                    eli_pop.append(elite)

            # inicializa a nova população de offspring
            off_pop = Population(0, optimization, grid)

            print('check-in 2', len(off_pop))
            # loop até a off_pop tiver o tamanho da parent pop
            while len(off_pop) < offspring_percent:
                off_pop.individuals.extend(
                    GA(pop, co_percent, mut_percent, selec_option, co_option, mut_option1, mut_option2))

            print('check-in 3', len(off_pop))
            # a população de offspring vira a nova parent population
            for elite in eli_pop:
                off_pop.individuals.append(elite)

            pop = off_pop

            print('check-in', len(pop))

            # pega o indivíduo com o menor valor de fitness
            best_fit = max(pop, key=attrgetter("fitness"))


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