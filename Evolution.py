import random
from Population import Population
from Individual import Individual

class Evolution():

    #Selecting random individuals from the population pool for crossover
    def tournament_selection(self, population):
        #Create a new tournament population
        tournament_population = Population(self.tournament_size, False)

        for i in range(0, self.tournament_size):
            #Select a random individual from the pool for breeding qualification
            index = random.randint(0, population.get_size() - 1)
            tournament_population.save_individual(i, population.get_individual(index))

        #Return the fittest individual from the tournament for breeding
        return tournament_population.get_fittest()

    #Crossover genes from parents and produce a child
    def crossover(self, parent_1, parent_2):
        child = Individual()
        for i in range(0, child.get_size()):
            #Divide the genes according to the uniform rate
            if random.random() <= self.uniform_rate:
                child.set_gene(i, parent_1.get_gene(i))
            else:
                child.set_gene(i, parent_2.get_gene(i))

        return child

    #Mutate individuals for better results
    def mutate(self, individual):
        for i in range(0, individual.get_size()):
            #Randomly set the gene at a position if mutation threshold is not crossed
            if random.random() <= self.mutation_rate:
                individual.set_gene(i, random.randint(0, 1))


    #Evolve the population to create a new generation
    def evolve(self, population):
        new_population = Population(population.get_size(), False)

        #Save the best individual for the next generation if elitism is activated
        if self.elitism:
            new_population.save_individual(0, population.get_fittest())

        #Create Crossovers
        for i in range(self.elitism_offset, population.get_size()):
            parent_1 = self.tournament_selection(population)
            parent_2 = self.tournament_selection(population)
            child = self.crossover(parent_1, parent_2)
            new_population.save_individual(i, child)

        #Create mutants
        for i in range(self.elitism_offset, new_population.get_size()):
            self.mutate(new_population.get_individual(i))

        return new_population


    def __init__(self, elitism_enabled):
        self.uniform_rate = 0.5
        self.mutation_rate = 0.015
        self.tournament_size = 5
        self.elitism = elitism_enabled
        if elitism_enabled:
            self.elitism_offset = 1
        else:
            self.elitism_offset = 0
