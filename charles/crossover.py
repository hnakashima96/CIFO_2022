import random
import numpy as np


def co_singlepoint(p1, p2):
    
    #pick a random row number to perform the mutation
    co_point = random.randint(1, len(p1.solution)-1)

    #swap the upper from the picked co_point between individuals
    offspring1 = np.vstack((p1.solution[:co_point],p2.solution[co_point:]))
    offspring2 = np.vstack((p2.solution[:co_point],p1.solution[co_point:]))
  
    p1.solution = offspring1
    p2.solution = offspring2

    return p1, p2


def pmx(p1,p2):
    '''
        Adapted version from:
        https://github.com/SCK22/GeneticAlgorithmTSP/blob/master/GeneticAlgoLibrary.py
    '''
    rows = random.sample(range(9), random.randint(1, 9))

    for k in rows:
        genes1 = p1.solution[k, :]
        genes1 = np.extract(genes1 < 0, genes1)

        genes2 = p2.solution[k, :]
        genes2 = np.extract(genes2 < 0, genes2)

        indexes_for_crossover = random.sample((range(len(genes1))), 2)
        co_start_point, co_end_point = (min(indexes_for_crossover), max(indexes_for_crossover))


        ## generate child 1
        child1 = np.hstack((genes1[0:co_start_point],
                           genes2[co_start_point:co_end_point],
                           genes1[co_end_point:]))
        ## generate child 2
        child2 = np.hstack((genes2[0:co_start_point],
                            genes1[co_start_point:co_end_point],
                            genes2[co_end_point:]))

        ## Create mappings
        #identify the respective index of numbers between arrays
        mapping = list(zip(
                genes1[co_start_point:co_end_point],
                genes2[co_start_point:co_end_point]))

        # run until all the nodes in the route are unique
        while len(np.unique(child1)) != len(child1):
            child1_part = np.hstack((child1[:co_start_point],
                                    child1[co_end_point:]))
            for i in range(len(child1_part)):
                for j in mapping:
                    if child1_part[i] == j[1]:
                        child1_part[i] = j[0]

            child1 = np.hstack((child1_part[:co_start_point],
                               child1[co_start_point:co_end_point],
                               child1_part[co_start_point:]))

        while len(np.unique(child2)) != len(child2):
            child2_part = np.hstack((child2[:co_start_point],
                                     child2[co_end_point:]))

            for i in range(len(child2_part)):
                for j in mapping:
                    if child2_part[i] == j[0]:
                        child2_part[i] = j[1]

            child2 = np.hstack((child2_part[:co_start_point],
                                child2[co_start_point:co_end_point],
                                child2_part[co_start_point:]))

    np.place(p1.solution[k, :], p1.solution[k, :] < 0, child1)
    np.place(p2.solution[k, :], p2.solution[k, :] < 0, child2)


    return p1, p2

def cycle_co(p1, p2):
    """
    Taken from class.

    Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    #select 5 random rows to perform this operation
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

