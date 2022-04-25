from charles import Population, Individual
from Sudoku.data_sudoku import grid
from Sudoku.functions_2 import fitness, get_neighbour
import random
from crossover import co_singlepoint

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
    #create a pop p with M individuals
p = []
for i in range(M):
    while len(p) < i:
        choice = random.choice(P)
        p.append(choice)

    #select 2 individuals (aqui aplicar selection algorithm)
    #teste com random choice

    #apply crossover (1 point)
p1, p2, offspring1, offspring2 = co_singlepoint(p)

    #apply mutation

    #add the resut in pop
for i in P:
    if i == p1:
        x = Individual(offspring1)
        i == x
    elif i == p2:
        y = Individual(offspring2)
        i == y


#Survivours + Result
print(P)
#return improved pop