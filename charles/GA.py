from charles import Population, Individual
import random
from crossover import co_singlepoint
from Sudoku.functions_2 import get_neighbour, fitness
from Sudoku.data_sudoku import grid
from mutation import mutation
sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour

#fazer o loop para conseguir chegar a fitness igual a zero

size = 100
M = 25

pop1 = Population(
            size=size,
            optim='min',
            grid=sudoku_grid
        )

pop1_copy = pop1

def GA(P,M):

    improve_fit = 100

    for i in range(len(P)):
        if P.individuals[i].fitness < improve_fit:
            improve_fit = P.individuals[i].fitness

    # #loop
        #create a pop p with M individuals
    p_index = []

    for i in range(M):
        while len(p_index) < i:
            choice = random.choice(range(len(P)))
            flag = True
            for j in p_index:
                if j == choice:
                    flag = False
            if flag:
                p_index.append(choice)

    #apply crossover (1 point) in population
    p1_index, p2_index, offspring1, offspring2 = co_singlepoint(p_index, P)

    #Apply mutation on the offsprings and substitute in the actual population
    #
    P.individuals[p1_index] = Individual(mutation(offspring1))
    P.individuals[p2_index] = Individual(mutation(offspring2))

###### CHECK IN POP CHANGED CONFIRMED ##########

    return P


#Conferir se o mutation está mudando os offspring
#Adicionar o elisitmo
#exemplo
#https://www.youtube.com/watch?v=llDfPufkQxw