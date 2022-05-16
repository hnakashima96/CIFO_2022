import numpy as np
import random

#classe para identificar se o valor existe em linha, coluna ou quadrado 3x3
class evaluation(object):

    def __init__(self, values):
        self.values = values
        return

    #repetição na linha
    def rep_row(self, row, value):
        for i in range(9):
            if (abs(self.values[row][i]) == abs(value)):
                return True
        return False

    #repetição na coluna
    def rep_column(self, column, value):
        for j in range(9):
            if (abs(self.values[j][column]) == abs(value)):
                return True
        return False

    #repetição no bloco
    def rep_square(self, row, column, value):
        x = (column//3)*3
        y = (row//3)*3
        for i in range(3):
            for j in range(3):
                if self.values[y+i][x+j] == abs(value):
                    return True
        return False


def get_neighbour(self):
    #copiar a grid inicial
    init_grid = np.copy(self)
    comparison = evaluation(init_grid)
    #definir quais valores da grid_i não são zeros (comparar com o sudoku)
    for row in range(9):
        for column in range(9):
            if init_grid[row][column] == 0:
                #definir um valor para o espaço vazio
                value = random.randint(1, 9)
                #identificar se esse valor existe na linha enquanto existir escolher outra opção
                while comparison.rep_row(row, value):
                    value = random.randint(1, 9)
                init_grid[row][column] = - value
    #se não existe pode aceitar
            else:
                init_grid[row][column] = self[row][column]
    return init_grid

def split(array, nrows, ncols):
    '''
    Função para dividir uma matriz de sudoko em uma lista de submatrizes.
    '''

    h = array.shape[1]
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))

#funçao para definir o fitness de cada provável solução
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


