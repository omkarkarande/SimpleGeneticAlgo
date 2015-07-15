from Individual import Individual

class Population():

    #Save a given individual at the given index in the population pool
    def save_individual(self, index, individual):
        self.individuals[index] = individual

    #Get an individual at the given index
    def get_individual(self, index):
        return self.individuals[index]

    #Get the fittest individual from the population
    def get_fittest(self):
        fittest = self.individuals[0]
        for i in range(1, self.size):
            if fittest.get_fitness() <= self.get_individual(i).get_fitness():
                fittest = self.get_individual(i)
        return fittest

    #Get the size of the population
    def get_size(self):
        return len(self.individuals)


    def __init__(self, size, initialize_population):
        self.size = size
        self.individuals = [None] * size

        if initialize_population:
            for i in range(0, size):
                individual = Individual()
                individual.generate_individual()
                self.save_individual(i, individual)
