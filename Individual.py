import random
import FitnessCalculator

class Individual():

    #Generate an individual with random genes
    def generate_individual(self):
        for i in range(0, self.gene_length):
            self.genes[i] = random.randint(0, 1)

    #Get the length of the gene sequence for the individual
    def get_size(self):
        return len(self.genes)

    #Get a gene at a given position
    def get_gene(self, index):
        return self.genes[index]

    #Set a gene at a given position
    def set_gene(self, index, value):
        self.genes[index] = value
        self.fitness = 0

    #Get the fitness value of the individual
    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = FitnessCalculator.calculate_fitness(self.genes)
        return self.fitness

    #Get a strin representation of the gene sequence
    def get_string(self):
        gene_string = ""
        for x in self.genes:
            gene_string += str(x)
        return gene_string

    def __init__(self):
        self.gene_length = 64
        self.fitness = 0
        self.genes = [None] * self.gene_length
