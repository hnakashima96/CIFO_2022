from itertools import permutations
import math
import random

def mutation(ind):
    
    mutation_choice = ind.solution

    line_index = random.choice(range(len(mutation_choice)))
    line_choice = mutation_choice[line_index]

    #identifying values and positions to change
    position_numbers = []
    change_numbers = []
    for index, value in enumerate(line_choice):
        if value < 0:
            position_numbers.append(index)
            change_numbers.append(value)

    #permutation of possible values 
    possible = list(permutations(change_numbers))
    mutation = random.randrange(math.factorial(len(change_numbers)))
    
    #add the resut in pop
    for index_p, position in enumerate(position_numbers):
        line_choice[position] = possible[mutation][index_p]

    mutation_choice[line_index] = line_choice

    ind.solution = mutation_choice

    return ind

def swap_mutation(individual):
    
    mutation_choice = individual.solution

    line_index = random.choice(range(len(mutation_choice)))

    line_choice = mutation_choice[line_index]

    #identifying possible index to change
    position_numbers = [i for i in range(9) if line_choice[i] < 0]

    #get 2 ramdom index of values in a line to swap
    index1, index2 = random.sample(position_numbers,2)

    #swap values
    line_choice[index1], line_choice[index2] = line_choice[index2], line_choice[index1]

    #replace new line
    mutation_choice[line_index] = line_choice

    individual.solution = mutation_choice

    return individual