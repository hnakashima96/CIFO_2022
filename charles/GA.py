from random import choice,random
from charles.crossover import co_singlepoint,cross_extrems,cycle_co
from charles.mutation import mutation,swap_mutation
from charles.selection import tournament,tournament2,rank,roulette
from charles.charles import Individual

def GA(P,p_cross, p_mu, selec_option, co_option, mut_option1, mut_option2):
    #inicializa uma probabilidade 
    p= p_cross
    p_mu = p_mu
    #selection
    first_sel = selec_option(P)
    second_sel = selec_option(P)

    #randomly choose to do crossover or reproduce
    if random() < p:
        #apply crossover (1 point) in population
        offspring1, offspring2 = co_option(first_sel, second_sel)
    else:
        offspring1, offspring2 = first_sel, second_sel

    #apply mutation on the offsprings and substitute in the actual population
    if random() < p_mu:
        offspring1 = mut_option1(offspring1)
    if random() < p_mu:
        offspring2 = mut_option2(offspring2)

    final_offspring1 = Individual(offspring1.solution)
    final_offspring2 = Individual(offspring2.solution)

    return [final_offspring1, final_offspring2]

