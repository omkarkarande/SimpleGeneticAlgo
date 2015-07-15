#Ideal gene sequence for an individual
solution = [None] * 64

#set the solution
def set_solution(sol):
    for i in range(len(sol)):
        solution[i] = int(sol[i])

#Compare the given sample with the ideal and return a fitness value
def calculate_fitness(sample):
    fit_val = 0
    for i in range(len(solution)):
        if sample[i] == solution[i]:
            fit_val += 1

    return fit_val

#get maximum fitness
def get_max_fitness():
    return len(solution)
