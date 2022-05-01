class Individual:
    def __init__(self, grid):
        self.grid = grid
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
        self.size = size #tamanho da população
        self.optim = optim #tipo de problema
        self.grid = grid
        for i in range(size):
            self.individuals.append(
                Individual(grid = self.grid)
            )


    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)})"

