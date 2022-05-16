from Sudoku.data_sudoku import grid
from Sudoku.functions import get_neighbour, fitness_max,fitness_min
from charles.charles import Population, Individual
import numpy as np
import random
from scipy.spatial.distance import hamming

#problem parameters
sudoku_grid = grid
optimization = 'min'
pop_size = 10

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


def fitness_sharing(P):

    patient_zero = random.choice(P.individuals)
    print('checkpoint1')
    # find a individual to calculate the distance
    second_patient = random.choice(P.individuals)
    print('checkpoint2')
    sharing_fitness = 0

    #if they are equal generate again
    while patient_zero == second_patient:
        second_patient = random.choice(P.individuals)
        print('equal individuals')

    # calculate the distance of all individuals in pop
    for i in range(len(patient_zero.solution)):

        sharing_fitness += hamming(patient_zero.solution[i], second_patient.solution[i])*len(patient_zero.solution[i])

        #substituir pelo menor fitness ou maior
        if P.optim == 'min':
            if patient_zero.fitness > second_patient.fitness:
                patient_zero == second_patient

        if P.optim == 'max':
            if patient_zero.fitness < second_patient.fitness:
                patient_zero == second_patient


    #normalize the distance

    #reward for large distances and penalty for small distance

    #share coefficient calculus

    #define fitness

fitness_sharing(pop)

print(pop.individuals)