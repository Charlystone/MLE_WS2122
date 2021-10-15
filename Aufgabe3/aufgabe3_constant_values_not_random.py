import numpy as np
from math import e
import random

# capacity in liter
capacity = 100

c = 0.01

r = 0.4  # crossover part

m = 30

hypothesis_len = 100

fitness_threshold = 0.00000000000001


# List of random float numbers with size 100
def get_list_of_random_volumes(list_size, max_volume):
    volumes = np.random.random(list_size)
    for idx in range(list_size):
        volumes[idx] = round(volumes[idx], 3)
        volumes[idx] = volumes[idx] * (max_volume - 1) + 1
    return volumes


#volume_list = get_list_of_random_volumes(100, 10)

volume_list = np.array([7.552, 9.091, 2.386, 2.188, 9.442, 7.48 , 5.545, 2.89 , 6.193,
       7.705, 8.812, 7.291, 9.64 , 7.354, 8.092, 9.199, 6.373, 5.59 ,
       7.768, 3.313, 7.102, 1.414, 4.537, 5.239, 6.436, 7.075, 3.727,
       1.297, 6.778, 9.136, 4.231, 3.655, 5.284, 5.122, 2.332, 7.543,
       5.248, 6.607, 1.558, 2.647, 6.697, 3.619, 8.767, 6.364, 2.845,
       9.01 , 7.102, 3.259, 2.926, 4.231, 9.172, 5.077, 4.069, 4.618,
       2.008, 2.674, 9.064, 4.582, 8.056, 5.707, 6.535, 8.137, 8.191,
       3.169, 6.004, 6.688, 2.818, 6.589, 4.555, 3.232, 9.838, 9.478,
       4.285, 7.66 , 3.124, 6.193, 3.907, 8.497, 8.128, 5.599, 5.491,
       6.13 , 2.152, 2.665, 6.157, 6.742, 7.372, 1.9  , 7.984, 2.863,
       8.821, 7.228, 2.98 , 5.374, 2.71 , 4.375, 4.996, 5.338, 5.68 ,
       8.74 ])

def get_volume_regarding_hypothesis(hypothesis):
    volume_arr = volume_list * hypothesis
    return volume_arr.sum()


# 10 hypothesiss with 100 Bits, p(1) = 0.182, only hypothesiss with volume <= 100 allowed
def get_population(population_size):
    population = []
    j = 0
    while j <= population_size - 1:
        hypothesis = np.random.random((1, 100)).tolist()[0]
        for idx in range(hypothesis_len):
            if hypothesis[idx] <= 0.182:  # p(1) = 0.182
                hypothesis[idx] = 1
            else:
                hypothesis[idx] = 0
        if get_volume_regarding_hypothesis(hypothesis) <= 100.00:  # only hypothesiss with volume <= 100 allowed
            population.append(hypothesis)
            j += 1
    population
    return population


#population = get_population(10)

population = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
              [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

p = len(population)

population_s = []


def fitness(hypothesis):
    volume = get_volume_regarding_hypothesis(hypothesis)
    return e ** (-c * ((100 - volume) ** 2))


def pr(hypothesis):
    total_fitness = 0
    for idx in range(p):
        total_fitness += fitness(population[idx])
    return fitness(hypothesis) / total_fitness


def select_hypothesis():
    rand_num = np.random.random()
    total = 0
    index = np.random.randint(p)
    while True:
        index += 1
        index %= p
        total = total + pr(population[index])
        if total > rand_num:
            break
    return index


def selection():
    for idx in range(int((1 - r) * p)):
        population_s.append(population[select_hypothesis()])


def crossover_operator(hypothesis1, hypothesis2):
    split_idx = np.random.randint(hypothesis_len)
    hypothesis1[:split_idx], hypothesis2[:split_idx] = hypothesis2[:split_idx], hypothesis1[:split_idx]
    return [hypothesis1, hypothesis2]


def crossover():
    for idx in range(int(r * p / 2)):
        new_hypothesis_pair = crossover_operator(population[select_hypothesis()], population[select_hypothesis()])
        population_s.append(new_hypothesis_pair[0])
        population_s.append(new_hypothesis_pair[1])


def mutation():
    for idx in range(m):
        rand_idx = np.random.randint(p)
        rand_hypothesis = population_s[rand_idx]
        rand_idx = np.random.randint(p)
        if rand_hypothesis[rand_idx] == 0:
            rand_hypothesis[rand_idx] = 1
        else:
            rand_hypothesis[rand_idx] = 0


def update():
    population = population_s


def get_max_fitness():
    fitness_list = []
    for hypothesis in population:
        fitness_list.append(fitness(hypothesis))
    return min(fitness_list)


max_fitness = get_max_fitness()

count = 0

while get_max_fitness() > fitness_threshold:
    selection()
    print(count)
    crossover()
    mutation()
    update()
    max_fitness = get_max_fitness()
    count += 1

print(max_fitness)
