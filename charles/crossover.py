import random
import numpy as np

def co_singlepoint(p):
    p1 = random.choice(p)
    p2 = random.choice(p)
    while np.array_equal(p1,p2):
        p2 = random.choice(p)

    #apply crossover (1 point)
    co_point = random.randint(1, len(p1.solution)-1)
    offspring1 = np.vstack((p1.solution[:co_point],p2.solution[co_point:]))
    offspring2 = np.vstack((p2.solution[:co_point],p1.solution[co_point:]))

    return p1, p2, offspring1, offspring2
