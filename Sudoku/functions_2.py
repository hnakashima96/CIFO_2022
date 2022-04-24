import numpy as np
import random
from Sudoku.data_sudoku import grid
from charles import Individual, Population
from copy import deepcopy


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

#gerou uma inicialização
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


#funçao para definir o fitness de cada provável solução
def fitness(prob_sol):

    #calcular se os valores da possível solução existe em uma coluna ou em um bloco
    value = 0
    for row in range(9):
        for column in range(9):
            if prob_sol[row][column] < 0:
                if evaluation(grid).rep_column(row, prob_sol[row][column]) \
                        or evaluation(grid).rep_square(row, column, prob_sol[row][column]):
                    value += 1

    return value

#Monkey Patching
Individual.fitness = fitness
Individual.get_neighbours = get_neighbour


pop = Population(
    size=5,
    optim='min',
    grid=grid
)




