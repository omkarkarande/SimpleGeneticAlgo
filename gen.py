import sys

import FitnessCalculator
from Evolution import Evolution
from Population import Population
from Individual import Individual


#Main
def main():

    #Get the sequence to be searched using
    FitnessCalculator.set_solution(str(raw_input("SEQUENCE: ")))

    #Define the population
    pop_size = int(raw_input("Enter population size: "))
    elite_option = str(raw_input("Elitism enabled?(y/n): "))

    #Elite switch
    if elite_option == 'y':
        elitism_enabled = True
    else:
        elitism_enabled = False

    #Create a starting popultation
    population = Population(pop_size, True)

    #Generation count
    generation = 0
    evolution = Evolution(elitism_enabled)

    #Loop until we dont have a solution
    while population.get_fittest().get_fitness() < FitnessCalculator.get_max_fitness():
        generation += 1
        print "GENERATION : " + str(generation) + " FITTEST: " + str(population.get_fittest().get_fitness())
        #Evolve the population
        population = evolution.evolve(population)


    print "SOLUTION FOUND..."
    print "GENERATION: " + str(generation)
    print "GENES: " + population.get_fittest().get_string()

    return

#Main Sentinel
if __name__ == "__main__":
    main()
