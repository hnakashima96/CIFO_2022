from charles.charles import Population, Individual
import random
from charles.crossover import co_singlepoint
from charles.mutation import mutation

# from Sudoku.data_sudoku import grid
# #from Sudoku.functions_2 import get_neighbours, fitness
# import Sudoku
#
# # P = Population(
# #     size = 10,
# #     optim='min',
# #     grid = grid
# # )
# # M = 5
# #
# # Individual.fitness = Sudoku.functions_2.fitness
# # Individual.get_neighbours = Sudoku.functions_2.get_neighbours

def GA(P,M):

    #loop
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

    #add the result in Pop

    #Pop.Individuals = Offspring1.Indiv

    P.individuals[p1_index] = Individual(offspring1)
    P.individuals[p2_index] = Individual(offspring2)

###### CHECK IN POP CHANGED CONFIRMED ##########

    #apply mutation in population
    mutant_index = random.choice(range(len(P)))
    mutant = P[mutant_index]

    P[mutant_index] = Individual(mutation(mutant))
    return P

