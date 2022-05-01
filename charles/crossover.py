import random
import numpy as np

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
