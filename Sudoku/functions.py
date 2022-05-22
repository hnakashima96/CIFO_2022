import numpy as np
import random
from scipy.spatial.distance import hamming

def get_neighbour(self):
    #copiar a grid inicial
    init_grid = np.copy(self)
   
    #definir quais valores da grid_i não são zeros (comparar com o sudoku)
    for i in range(9):
       fixed = [-x for x in range(1,10) if x not in set(init_grid[i,:])]
       random.shuffle(fixed)
       np.place(init_grid[i,:], init_grid[i,:]==0, fixed)

    return init_grid

def split(array, nrows, ncols):
    '''
    Função para dividir uma matriz de sudoko em uma lista de submatrizes.
    '''

    h = array.shape[1]
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))


def fitness_min(prob_sol):

    #coloca todos os valores do sudoko como positivo para fazer avaliação de duplicados
    #sem isso, o mesmo número no sudoko, mas negativo, não seria considerado duplicado
    prob_sol = np.abs(prob_sol)

    #inicializa o fit
    total_fit = 0

    #conta duplicados de cada linha
    for i in range(9):
        #a função unique gera um array com os valores unicos e outro com o count desses valores no array avaliado
        #exemplo: input:[1,1,3,4,5], output: [1,3,4,5] e [2,1,1,1]
        counts_row = np.unique(prob_sol[:,i], return_counts=True)[1] 
        counts_column = np.unique(prob_sol[i,:], return_counts=True)[1]
        
        total_fit += sum(counts_row-1) + sum(counts_column-1)

    #divide o sudoko em uma lista de sub-matrizes
    sub_matrix = split(prob_sol,3,3)

    #avalia duplicados em cada sub-matriz
    for i in sub_matrix:
        counts = np.unique(i, return_counts=True)[1]
        total_fit += sum(counts-1)

    return total_fit

def fitness_max(prob_sol):

    prob_sol = np.abs(prob_sol)

    #inicializa o fit
    total_fit = 0

    for i in range(9):
        total_fit += len(set(prob_sol[:,i])) + len(set(prob_sol[i,:]))


    #divide o sudoko em uma lista de sub-matrizes
    sub_matrix = split(prob_sol,3,3)

    #avalia duplicados em cada sub-matriz
    for i in sub_matrix:
        unique = np.unique(i)
        total_fit += len(unique)

    return total_fit


def sharring_coef(ind_index,pop):
    
    distances = []
    
    if pop.optim == 'max':
        for i in range(len(pop)):
            if i != ind_index:
                distances.append(1-hamming(pop[ind_index].solution.flatten(),pop[i].solution.flatten()))

        return sum(distances)
    else:
        for i in range(len(pop)):
            if i != ind_index:
                distances.append(hamming(pop[ind_index].solution.flatten(),pop[i].solution.flatten()))

        return sum(distances)


