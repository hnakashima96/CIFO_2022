from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
from charles.crossover import cross_extrems,co_singlepoint, cycle_co, pmx
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament, roulette, rank
from charles.GA import GA
from operator import attrgetter
from bancodados import create_table_analysis, insere_teste,create_table_perform, insere_perform
import numpy as np
import timeit

sudoku_grid = grid
optimization = 'max'

#Population size definition
pop_size = 2500

#GA parameters decision
co_percent = 0.97
mut_percent = 0.01
selec_option = tournament
co_option = co_singlepoint
mut_option1 = swap_mutation
mut_option2 = mutation
elitism = 0

##PRECISA CRIAR TABELA PERFORM?
tabela_perform = 'sim'

#NÚMERO DA COMBINAÇÃO
combinacao = 1

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


#criar tabela para resultado de performance
if tabela_perform == 'sim':
    create_table_perform()

#criar tabela para cada combinação
create_table_analysis(combinacao,selec_option,co_option)

test_number = 0
while test_number < 50:
    #fazer o loop para conseguir chegar a fitness igual a zero
    count = 0
    flag_sucesso = False
    start = timeit.default_timer()
    #laço para encontrar o fitness
    while flag_sucesso == False:
        if count > 40:
            break
        
        #inicializa a nova população de offspring
        off_pop = Population(0,optimization,grid)
        
        if elitism > 0:
            # Armazenar a porcentagens de novos indivíduos
            eli_number = int(pop_size*elitism)

            #orderna população do elitismo de acordo com o optimization
            eli_pop_sort = sorted(pop.individuals, key=lambda x:x.fitness, reverse=pop.optim == 'max')

            #adiciona a população do elitismo de acordo com a ordem
            off_pop.individuals.extend(eli_pop_sort[:eli_number])

        #completa o resto da população com GA
        while len(off_pop) < pop_size:
            off_pop.individuals.extend(GA(pop, co_percent, mut_percent, selec_option, co_option, mut_option1, mut_option2))

        #a população de offspring vira a nova parent population
        pop = off_pop

        # pega o indivíduo com o melhor fitness
        if pop.optim == 'min':
            best_fit = min(pop, key=attrgetter("fitness"))
        elif pop.optim == 'max':
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

        insere_teste(test_number,combinacao,selec_option, co_option, count, best_fit.fitness,pop.variance())

        print('count:', count,', Fitness: ',best_fit.fitness,',Diversity: ',pop.variance())

    stop = timeit.default_timer()

    insere_perform(combinacao,selec_option, co_option, test_number, stop - start, pop_size, co_percent, mut_percent, elitism)

    test_number += 1

    print('Time: ', stop - start, 's')


