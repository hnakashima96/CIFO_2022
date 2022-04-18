from random import randint

def template_co(p1, p2):

    return offspring1, offspring2

def single_point_co(p1, p2):
    co_point = randint(1, len(p1)-1)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2

