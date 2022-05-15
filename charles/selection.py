from random import uniform,choice,sample
from operator import attrgetter
import numpy as np

from Sudoku.functions import sharring_coef

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

    return choice


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


def tournament(population, size=5):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = sample(population.individuals,size) 
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")



def tournament2(population, size=5):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """
 
    # Select individuals based on tournament size
    tournament_indexs = sample(range(len(population)),size) 

    for i in tournament_indexs:
        population[i].sharing_fitness = population[i].fitness / sharring_coef(i,population)

    tournament = [population[i] for i in tournament_indexs] 
    
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("sharing_fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("sharing_fitness"))
    else:
        raise Exception("No optimization specified (min or max).")
