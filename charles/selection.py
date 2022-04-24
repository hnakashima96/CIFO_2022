from random import uniform

def roulette(population):
    total_fitness = sum([i.fitness for i in population])
    spin = uniform(0, total_fitness)
    position = 0
    for individual in population:
        position += individual.fitness
        if position > spin:
            return individual
