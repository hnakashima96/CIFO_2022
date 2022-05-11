import random
import numpy as np
<<<<<<< Updated upstream


def co_singlepoint(p1, p2):
=======
from charles.selection import roulette

def co_singlepoint(index, p):
    p1_index = roulette(index,p)
    p2_index = roulette(index,p)
    while np.array_equal(p1_index,p2_index):
        p2_index = random.choice(index)

    p1 = p[p1_index]
    p2 = p[p2_index]

>>>>>>> Stashed changes
    #apply crossover (1 point)
    co_point = random.randint(1, len(p1.solution)-1)

    offspring1 = np.vstack((p1.solution[:co_point],p2.solution[co_point:]))
    offspring2 = np.vstack((p2.solution[:co_point],p1.solution[co_point:]))
  
    p1.solution = offspring1
    p2.solution = offspring2

    return p1, p2

###CREATE CROSSOVER BETWEEN EXTREMES
