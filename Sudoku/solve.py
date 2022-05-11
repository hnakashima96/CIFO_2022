from Sudoku.data_sudoku import grid
from Sudoku.functions_2 import get_neighbour, fitness
from charles.charles import Population, Individual
from charles.GA import GA

sudoku_grid = grid

# define monkey patch of the charles functions
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour

#fazer o loop para conseguir chegar a fitness igual a zero

size = 1000
M = 500
teste = 1000
#initial population
pop = Population(
            size=size,
            optim='min',
            grid=sudoku_grid
    )

solution = 0
#para encontrar o fitness igual a zero
flag_sucesso = False
for i in range(size):
    #print(i)
    if pop.individuals[i].fitness == 0:
        flag_sucesso = True
        solution = pop.individuals[i]
        break
        #create a new population

count = 0
fitness_min = 100 #um chute inicial para conseguir identificar a convergência
#se nao encontrar
while flag_sucesso == False:
        count += 1
        pop1 = Population(
            size=size,
            optim='min',
            grid=sudoku_grid
        )

        pop2 = GA(pop1,M)

        for i in range(len(pop2)):
            if pop2.individuals[i].fitness < fitness_min:
                fitness_min = pop2.individuals[i].fitness

            if pop2.individuals[i].fitness == 0:
                flag_sucesso = True
                solution = pop2.individuals[i]
                break

        print('count:', {count},', Fitness Mínimo',{fitness_min})
        if count > teste:
            print("more than ",{count}," interations, pass limited time")
            break

#print(pop.__getitem__(599).fitness)

# for i in range(10):
#      print(i,pop.individuals[i],pop1.individuals[i])

#print(pop2)

#print(pop.individuals[0].fitness)
