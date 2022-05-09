import random
import numpy as np


def co_singlepoint(p1, p2):
    #apply crossover (1 point)
    co_point = random.randint(1, len(p1.solution)-1)

    offspring1 = np.vstack((p1.solution[:co_point],p2.solution[co_point:]))
    offspring2 = np.vstack((p2.solution[:co_point],p1.solution[co_point:]))
  
    p1.solution = offspring1
    p2.solution = offspring2

    return p1, p2

###CREATE CROSSOVER BETWEEN EXTREMES
