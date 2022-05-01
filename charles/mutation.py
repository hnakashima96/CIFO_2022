from itertools import permutations
import math
import random

def mutation(mutation_choice):
    line_index = random.choice(range(len(mutation_choice.solution)))
    line_choice = mutation_choice.solution[line_index]


    #identifying values and positions to change
    position_numbers = []
    change_numbers = []
    for index, value in enumerate(line_choice):
        if value < 0:
            position_numbers.append(index)
            change_numbers.append(value)

    #permutation of possible values (mutation)
    possible = list(permutations(change_numbers))
    mutation = random.randrange(math.factorial(len(change_numbers)))

    #add the resut in pop
    for index_p, position in enumerate(position_numbers):
        line_choice[position] = possible[mutation][index_p]

    mutation_choice.solution[line_index] == line_choice

    return (mutation_choice.solution)