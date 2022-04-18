from random import randint

def template_mutation(individual):

    return individual

def binary_mutation(individual):

    mut_point = randint(0, (len(individual)-1))

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary"
        )
    return individual

