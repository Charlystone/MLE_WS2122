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


volume_list = get_list_of_random_volumes(100, 10)


def get_volume_regarding_hypothesis(hypothesis):
    volume_arr = volume_list * hypothesis
    return volume_arr.sum()


# 10 hypothesiss with 100 Bits, p(1) = 0.182, only hypothesiss with volume <= 100 allowed
def get_population(population_size):
    return np.random.randint(2, size=(population_size, hypothesis_len))


population = get_population(10)

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
