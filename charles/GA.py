from random import choice,random
from charles.crossover import co_singlepoint
from charles.charles import Individual

def GA(P,p_cross, p_mu,selection_choice,mutation_choice,**kwargs):
    #inicializa uma probabilidade 
    p= p_cross
    p_mu = p_mu
    #selection
    first_sel = selection_choice(P)
    second_sel = selection_choice(P)

    #randomly choose to do crossover or reproduce
    if random() < p:
        #apply crossover (1 point) in population
        offspring1, offspring2 = co_singlepoint(first_sel, second_sel)
    else:
        offspring1, offspring2 = first_sel, second_sel

    #apply mutation on the offsprings and substitute in the actual population
    if random() < p_mu:
        offspring1 = mutation_choice(offspring1)
    if random() < p_mu:
        offspring2 = mutation_choice(offspring2)
    
    return [Individual(offspring1.solution), Individual(offspring2.solution)]
