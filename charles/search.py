from random import choice, uniform #import the values between 0 to 1
from math import exp


def hill_climb(search_space, log = 0):

    start = choice(search_space) #select a random solution
    position = start #change the current solution

    iter_plateu = 0 #avoid be stuck

    if log == 1:
        print(f"Initial position: {start}")

    if search_space.optim == "max":
        while True:

            if iter_plateu >= 5:
                print(f"Best solution found hc: {position}")
                return position

            n = position.get_neighbours()
            n_fit = [i.fitness for i in n]

            if search_space.optim == 'max':
                best_n = n[n_fit.index(max(n_fit))]
                if best_n.fitness > position.fitness:
                    if log == 1:
                        print(f"Found better solution:{position}")
                    iter_plateu = 0
                    position = best_n
                elif best_n.fitness == position.fitness:
                    if log == 1:
                        print(f"Found better solution:{position}")
                    iter_plateu += 1
                    position = best_n
                else:
                    print(f"Best solution hc:{position}")
                    return position

            elif search_space.optim == "min":
                best_n = n[n_fit.index(max(n_fit))]
                if best_n.fitness > position.fitness:
                    if log == 1:
                        print(f"Found better solution:{position}")
                iter_plateu = 0
                position = best_n
            elif best_n.fitness == position.fitness:
                if log == 1:
                    print(f"Found better solution:{position}")
                iter_plateu += 1
                position = best_n
            else:
                print(f"Best solution hc:{position}")
                return position
        else:
            raise Exception("Problem doesn't specify if min or max")

#hardcode for max problem
def sim_annealing(search_space, L, c, alpha =.95): #alpha affect how quickly we reach the best solution
    #Initialize solution from search space (randomly)
    position = choice(search_space)
    elite = position
    #While loop until termination condition
    while c > 0.05:
        #repeat L time (for loop)
        for i in range(L):
            #Generate neighbour
            sol = choice(position.get_neighbours()) #how to improve the implementation?
            #if neigh is better our equal take
            if sol.fitness >= position.fitness:
                position = sol
                if position.fitness > elite.fitness: #
                    elite = position
            #elif weird function, take if met
            else: #only evaluate if the solution is worse
                p = uniform(0,1) #random function 0 to 1
                pc = exp(-abs(sol.fitness - position.fitness)/c)
                if p < pc:
                    position = sol
        #update C
        #update L
        c = c*alpha
    print(f"Sim returned: {position}")
    print(f"Best solution sa:{position}")
    return position




