from random import uniform,choices,sample
from operator import attrgetter


from Sudoku.functions import sharring_coef

### CREATE A ROULETTE WHEEL
def roulette(population):
    '''
        The roulette wheel for the minization problem considers the sum of inverse fitness of
        all each individual and each interaction is added the inverse fitness to the position
        variable. With this configuration, higher values of fitness are smaller than lower ones,
        thus the proportion of it in the wheel and in the probabilities.
    
    '''
    
    position = 0

    if population.optim == 'min': 
        sum_all_fitness = sum([1 / ind.fitness for ind in population])
        spin = uniform(0, sum_all_fitness)
        for ind in population:
            position += (1 / ind.fitness)
            if position > spin:
                return ind

    elif population.optim == 'max':   
        sum_all_fitness = sum([ind.fitness for ind in population])
        spin = uniform(0, sum_all_fitness)
        for ind in population:
            position += ind.fitness
            if position > spin:
                return ind

### CREATE RANKING SELECTION
def rank(population):
    '''
        The rank selection considered the probability of select an individual based in his position in the 
        rank of fitness. The rank is just a sorting of the individuals by fitness: higher the position of 
        the individual in the list, higher the probability.
        The probability is obtain by the formula:
            individual index / AP(n)
        Where AP(n) is the sum of all the index we obtain by the gaussing arithmetic progression formula:
            n * (n+1) / 2    , n = number of elements or the higher index
    
    '''
    #rank the population by sorting individuals bases on their fitness
    rank = sorted(population, key=attrgetter("fitness"), reverse=population.optim == 'min')

    #get sum of index's
    max_index = len(rank)
    index_sum = ( max_index * (max_index + 1) ) / 2

    #creat a list with the probability for each individual be selected
    individual_prob = [ i / index_sum for i in range(1,max_index+1) ] 

    return choices(rank, weights=individual_prob, k=1)


def tournament(population, size=5, sharing_cal = False ):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    if sharing_cal:
        # Select individuals based on tournament size
        tournament_indexs = sample(range(len(population)),size) 

        for i in tournament_indexs:
            population[i].sharing_fitness = population[i].fitness / sharring_coef(i,population)

        tournament = [population[i] for i in tournament_indexs] 

    else:
        # Select individuals based on tournament size
        tournament = sample(population.individuals,size) 

    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")


