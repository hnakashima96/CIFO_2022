from random import choice,random
from charles.crossover import co_singlepoint
<<<<<<< Updated upstream
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament #,roulette
from charles.charles import Individual

def GA(P,p_cross, p_mu):
    #inicializa uma probabilidade 
    p= p_cross
    p_mu = p_mu
    #selection
    first_sel = tournament(P)
    second_sel = tournament(P)

    #randomly choose to do crossover or reproduce
    if random() < p:
        #apply crossover (1 point) in population
        offspring1, offspring2 = co_singlepoint(first_sel, second_sel)
    else:
        offspring1, offspring2 = first_sel, second_sel

    #apply mutation on the offsprings and substitute in the actual population
    if random() < p_mu:
        offspring1 = swap_mutation(offspring1)
    if random() < p_mu:
        offspring2 = mutation(offspring2)
    
    return [Individual(offspring1.solution), Individual(offspring2.solution)]
=======
from Sudoku.functions_2 import get_neighbour, fitness
# from Sudoku.data_sudoku import grid
from charles.mutation import mutation
# sudoku_grid = grid
#
# # define monkey patch of the charles functions
# Individual.fitness = fitness
# Individual.get_neighbours = get_neighbour
#
# #fazer o loop para conseguir chegar a fitness igual a zero
#
# size = 6
# M = 3
#
# pop1 = Population(
#             size=size,
#             optim='min',
#             grid=sudoku_grid
#         )


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

    #print(p_index)

    #apply crossover (1 point) in population
    #while True:
    p1_index, p2_index, offspring1, offspring2 = co_singlepoint(p_index, P)
        # if fitness(offspring1) < improve_fit:
        #     break
        # if fitness(offspring2) < improve_fit:
        #     break

    #Apply mutation on the offsprings and substitute in the actual population

    mutante_1 = mutation(offspring1)
    mutante_2 = mutation(offspring2)

    #if the fitness of the offspring is better change else not
    if fitness(mutante_1) < P.individuals[p1_index].fitness:
        P.individuals[p1_index] = Individual(mutante_1)

    if fitness(mutante_2) < P.individuals[p2_index].fitness:
        P.individuals[p2_index] = Individual(mutante_2)

###### CHECK IN POP CHANGED CONFIRMED ##########

    return P


>>>>>>> Stashed changes
