import random
import numpy as np
# from charles import Population, Individual
# from Sudoku.functions_2 import fitness, get_neighbour
# from Sudoku.data_sudoku import grid
#
#
# sudoku_grid = grid
#
# # define monkey patch of the charles functions
# Individual.fitness = fitness
# Individual.get_neighbours = get_neighbour
#
# #fazer o loop para conseguir chegar a fitness igual a zero
#
# size = 100
# M = 25
#
# pop = Population(
#             size=size,
#             optim='min',
#             grid=sudoku_grid
#         )
#
# p_index = []
#
# for i in range(M):
#     while len(p_index) < i:
#         choice = random.choice(range(len(pop)))
#         flag = True
#         for j in p_index:
#             if j == choice:
#                 flag = False
#         if flag:
#             p_index.append(choice)

def co_singlepoint(index, p):
    p1_index = random.choice(index)
    p2_index = random.choice(index)
    while np.array_equal(p1_index,p2_index):
        p2_index = random.choice(index)

    p1 = p[p1_index]
    p2 = p[p2_index]


    #apply crossover (1 point)
    co_point = random.randint(1, len(p1.solution)-1)
    offspring1 = np.vstack((p1.solution[:co_point],p2.solution[co_point:]))
    offspring2 = np.vstack((p2.solution[:co_point],p1.solution[co_point:]))

    return p1_index, p2_index, offspring1, offspring2


