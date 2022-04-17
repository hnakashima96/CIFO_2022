import numpy as np
import random
import sys

startingSudoku = """
                    530070000
                    600195000
                    098000060
                    800060003
                    400803001
                    700020006
                    060000280
                    000419005
                    000080079
                """

grid = np.array([[int(i) for i in line] for line in startingSudoku.split()])

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
def get_neighbour():
    #copiar a grid inicial
    init_grid = np.copy(grid)
    #print(init_grid)
    comparison = evaluation(init_grid)
    #print(comparison)
    #definir quais valores da grid_i não são zeros (comparar com o sudoku)
    for row in range(9):
        for column in range(9):
            if init_grid[row][column] == 0:
                #definir um valor para o espaço vazio
                hiromi = random.randint(1, 9)
                #print(row, column, hiromi)
                #identificar se esse valor existe na linha enquanto existir escolher outra opção
                while comparison.rep_row(row, hiromi):
                    hiromi = random.randint(1, 9)
                    #print(row, column, hiromi)
                init_grid[row][column] = - hiromi
    #se não existe pode aceitar
            else:
                init_grid[row][column] = grid[row][column]
    return init_grid

prob_sol = get_neighbour()

#funçao para definir o fitness de cada provável solução
def fitness(prob_sol):

    #calcular se os valores da possível solução existe em uma coluna
    value = 0
    for row in range(9):
        for column in range(9):
            if prob_sol[row][column] < 0:
                if evaluation(grid).rep_column(row, prob_sol[row][column]) \
                        or evaluation(grid).rep_square(row, column, prob_sol[row][column]):
                    value += 1

    return value

print(fitness(prob_sol))


