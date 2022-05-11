from random import choice,random
from charles.crossover import co_singlepoint
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament #,roulette
from charles.charles import Individual

def GA(P,p_cross, p_mu):
    #inicializa uma probabilidade 
    p= p_cross
    p_mu = p_mu
    #selection
    first_sel = tournament(P)
    second_sel = tournament(P)

    #randomly choose to do crossover or reproduce
    if random() < p:
        #apply crossover (1 point) in population
        offspring1, offspring2 = co_singlepoint(first_sel, second_sel)
    else:
        offspring1, offspring2 = first_sel, second_sel

    #apply mutation on the offsprings and substitute in the actual population
    if random() < p_mu:
        offspring1 = swap_mutation(offspring1)
    if random() < p_mu:
        offspring2 = mutation(offspring2)
    
    return [Individual(offspring1.solution), Individual(offspring2.solution)]
