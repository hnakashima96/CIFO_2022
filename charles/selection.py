<<<<<<< Updated upstream
from random import uniform,choice
from operator import attrgetter
import numpy as np
from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_min
from charles.charles import Population, Individual

sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness_min
Individual.get_neighbours = get_neighbour

pop_size = 10

#initial population
pop = Population(
            size=pop_size,
            optim='min',
            grid=sudoku_grid
        )

print(pop)


### CREATE A ROULETTE WHEEL
def roulette(population):

    sum_all_fitness = sum([population.individuals[ind].fitness for ind in range(len(population))])
    
    individual_prob = [population.individuals[ind].fitness/sum_all_fitness for ind in range(len(population))]

    if population.optim == 'min':
        problem = 1 - np.array(individual_prob)

    elif population.optim == 'max':
        problem = np.array(individual_prob)

    problem /= problem.sum()

    choice = np.random.choice(population, p=problem)
=======
# import random
# from Sudoku.data_sudoku import grid
# from Sudoku.functions_2 import get_neighbour, fitness
# from charles import Population, Individual
import numpy as np

# sudoku_grid = grid
#
# # define monkey patch of the charles functions
# Individual.fitness = fitness
# Individual.get_neighbours = get_neighbour
#
# #fazer o loop para conseguir chegar a fitness igual a zero
#
# size = 6
# M = 4
# teste = 1
# #initial population
# pop = Population(
#             size=size,
#             optim='min',
#             grid=sudoku_grid
#     )
#
# p_index = [2, 4, 5]
#
# print([pop.individuals[i].fitness for i in range(len(pop))])

def roulette(p_index, P):
    fitness_list = []
    # definir o fitness de toda a população
    for j in range(len(p_index)):
        i = p_index[j]
        fitness_list.append(P.individuals[i].fitness)
    #print(fitness_list)
    # identificar a soma do fitness da população
    sum_fitness = sum(fitness_list)
    #print(sum_fitness)

    #probabilidade de um valor ser escolhido
    pchosen = [(fit/sum_fitness) for fit in fitness_list]
    #print(pchosen)

    #minimization problem
    min_problem = 1 - np.array(pchosen)
    #print('antes',min_problem)
    min_problem /= min_problem.sum()
    #print('depois',min_problem, sum(min_problem))

    #escolher um valor
    choice = np.random.choice(p_index, p=min_problem)
>>>>>>> Stashed changes

    return choice


<<<<<<< Updated upstream
### CREATE RANKING SELECTION
def rank(population):

    if population.optim == 'min':
        sort_all_fitness = [population.individuals[ind].fitness for ind in range(len(population))]
        sort_all_fitness.sort(reverse=True)
    elif population.optim == 'max':
        sort_all_fitness = [population.individuals[ind].fitness for ind in range(len(population))]
        sort_all_fitness.sort(reverse=False)

    individual_prob = np.array([ind/len(population) for ind in range(len(population))])

    individual_prob /= individual_prob.sum()

    choice = np.random.choice(population, p=individual_prob)

    return choice


def tournament(population, size=100):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = [choice(population.individuals) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")

#Ranking selection
=======

# print(roulette(p_index, pop))
# https://stackoverflow.com/questions/8760473/roulette-wheel-selection-for-function-minimization
>>>>>>> Stashed changes
