from random import uniform,choice
from operator import attrgetter

def roulette(population):
    
    total_fitness = sum([i.fitness for i in population])
    spin = uniform(0, total_fitness)
    position = 0
    for individual in population:
        position += individual.fitness
        if position > spin:
            return individual

def tournament(population, size=20):
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