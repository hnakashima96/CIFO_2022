from charles import Population, Individual
from Sudoku.data_sudoku import grid
from Sudoku.functions_2 import fitness, get_neighbour
import random


#Monkey Patching
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour

#create an initial pop P of N individuals and calculate the fitness
P = Population(
    size = 10,
    optim = 'min',
    grid = grid,
)

M = 5
Operator = 'crossover'
#loop
    #create a pop p with M individuals (aqui aplicar selection algorithm)
p = []
for i in range(M):
    while len(p) < i:
        choice = random.choice(P)
        p.append(choice)

    #select 2 individuals

    #apply crossover or reproduction

    #apply mutation

    #add the resut in pop

#Survivours + Result

#return improved pop