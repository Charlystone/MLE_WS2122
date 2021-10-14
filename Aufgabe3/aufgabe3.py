import numpy as np
from math import e
import random

# capacity in liter
capacity = 100

c = 0.01

r = 0.4  # crossover part

m = 30

genome_size = 100

fitness_threshold = 0.00001


# List of random float numbers with size 100
def get_list_of_random_volumes(list_size, max_volume):
    volumes = np.random.random(list_size)
    for i in range(list_size):
        volumes[i] = round(volumes[i], 3)
        volumes[i] = volumes[i] * (max_volume - 1) + 1
    return volumes


volume_list = get_list_of_random_volumes(100, 10)


def get_volume_regarding_genome(genome):
    volume_arr = volume_list * genome
    return volume_arr.sum()


# 10 genomes with 100 Bits, p(1) = 0.182, only genomes with volume <= 100 allowed
def get_population(population_size):
    population = []
    j = 0
    while j <= population_size:
        genome = np.random.random((1, genome_size)).tolist()[0]
        for i in range(genome_size):
            if genome[i] <= 0.182:  # p(1) = 0.182
                genome[i] = 1
            else:
                genome[i] = 0
        if get_volume_regarding_genome(genome) <= 100.00:  # only genomes with volume <= 100 allowed
            population.append(genome)
            j += 1
    population
    return population


population = get_population(10)

p = len(population)

population_s = []


def fitness(genome):
    volume = get_volume_regarding_genome(genome)
    return e ** (-c * ((100 - volume) ** 2))


def pr(hypothesis):
    total_fitness = 0
    for i in p:
        total_fitness += fitness(population[i])

    return fitness(hypothesis) / total_fitness


def select_hypothesis():
    rand_num = np.random.random()
    total = 0
    index = np.random.rand(p)
    while True:
        index += 1
        index %= p
        total = total + pr(index)
        if total > rand_num:
            break
    return index


def selection():
    for idx in range(int((1 - r) * p)):
        population_s.append(population[select_hypothesis()])


def crossover_operator(genome1, genome2):
    split_idx = np.random.randint(genome_size)
    genome1[:split_idx], genome2[:split_idx] = genome2[:split_idx], genome1[:split_idx]
    return [genome1, genome2]


def crossover():
    for idx in range(int(r * p / 2)):
        new_genome_pair = crossover_operator(population[select_hypothesis()], population[select_hypothesis()])
        population_s.append(new_genome_pair[0]).append(new_genome_pair[1])


def mutation():
    for idx in range(m):
        rand_idx = np.random.randint(p)
        rand_genome = population_s[rand_idx]
        rand_idx = np.random.randint(p)
        if rand_genome[rand_idx] == 0:
            rand_genome[rand_idx] = 1
        else:
            rand_genome[rand_idx] = 0


def update():
    population = population_s


def get_max_fitness():
    fitness_list = []
    for genome in population:
        fitness_list.append(fitness(genome))

    return min(fitness_list)


max_fitness = get_max_fitness()


while get_max_fitness() > fitness_threshold:
    selection()
    crossover()
    mutation()
    update()
    max_fitness = get_max_fitness()

print(max_fitness)