from scipy.spatial.distance import hamming
from statistics import mean
import numpy as np


class Individual:
    def __init__(self, grid):
        self.grid = grid
        self.sharing_fitness = 0
        self.solution = Individual.get_neighbours(self.grid)
        self.fitness = Individual.fitness(self.solution)

    def fitness(self, prob_sol):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def __repr__(self):
        return f"Individual: (matrix={self.solution}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, grid, **kwargs):
        self.individuals = []
        self.size = size #tpopulation size
        self.optim = optim #optimization problem
        self.grid = grid
        for i in range(size):
            self.individuals.append(
                Individual(grid = self.grid)
            )

    def variance(self):
        '''
            This function takes every individual and compute how much different it is comapred to the a initial individual.
            The resukting sum of difference is the variance. For the Sudoku problem it was used the Hamming distance
            of a flattern representation of the 9x9 matrix of the sudoko.
        '''
        distances = []
        pop = self.individuals
        
        #loop over every individual and append the distance to the initial individual
        for i in range(len(pop)):
            distances.append(hamming(pop[0].solution.flatten(),pop[i].solution.flatten()))
        
        n = len(distances)
        x = mean(distances)

        dmax = max(distances)
        dmin = min(distances)

        #normalize the distances
        normalized_distances = np.array([(x - dmin) / (dmax - dmin) for x in distances])
        normalized_distances = np.nan_to_num(normalized_distances)

        #calculate the variance 
        return round(1/(n-1) * (sum(normalized_distances-x))**2)

    
    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)})"


