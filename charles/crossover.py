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
def cross_extrems(p1, p2):
    
    rows = random.sample(range(9),random.randint(1,9))
    
    for i in rows:
        genes1 = p1.solution[i,:]
        genes1 = np.extract(genes1<0,genes1)

        genes2 = p2.solution[i,:]
        genes2 = np.extract(genes2<0,genes2)

        genes1[0], genes1[-1] = genes2[-1], genes2[0]

        while len(set(genes1)) < len(genes1):
           genes1[0] = genes1[random.randint(1,len(genes1))] 
           genes1[0], genes1[-1] = genes2[-1], genes2[0]

        np.place(p1.solution[i,:],p1.solution[i,:]<0,genes2)
        np.place(p2.solution[i,:],p2.solution[i,:]<0,genes1)

    return p1, p2

def cycle_co(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    #rows = random.sample(range(9),random.randint(1,9))
    rows = random.sample(range(9),5)
    for row in rows:
        genes1 = p1.solution[row,:]
        genes1 = list(np.extract(genes1<0,genes1))

        genes2 = p2.solution[row,:]
        genes2 = list(np.extract(genes2<0,genes2))

        if genes1==genes2:
            genes1.reverse()
        # Offspring placeholders - None values make it easy to debug for errors
        offspring1 = [None] * len(genes1)
        offspring2 = [None] * len(genes1)
        # While there are still None values in offspring, get the first index of
        # None and start a "cycle" according to the cycle crossover method
        while None in offspring1:
            index = offspring1.index(None)
            # alternate parents between cycles beginning on second cycle
            if index != 0:
                genes1, genes2 = genes2, genes1
            val1 = genes1[index]
            val2 = genes2[index]

            while val1 != val2:
                offspring1[index] = genes1[index]
                offspring2[index] = genes2[index]
                val2 = genes2[index]
                index = genes1.index(val2)
            # In case last values share the same index, fill them in each offspring
            offspring1[index] = genes1[index]
            offspring2[index] = genes2[index]

            
        np.place(p1.solution[row,:],p1.solution[row,:]<0,offspring1)
        np.place(p2.solution[row,:],p2.solution[row,:]<0,offspring2)

    return p1, p2

