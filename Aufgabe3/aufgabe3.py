import numpy as np
from math import e
import random

# capacity in liter
capacity = 100
c = 0.0002
r = 0.3  # crossover part
m = 0.6
hypothesis_len = 100
fitness_threshold = 0.99
p = 25
population = []
population_s = []
volume_list = []


def set_volume_list():
    global volume_list
    volume_list = np.random.random(size=(1, 100))
    volume_list = volume_list * 9 + 1


def get_volume_regarding_hypothesis(hypothesis):
    return (volume_list * hypothesis).sum()


def set_population():
    global population

    population = np.zeros((p, hypothesis_len), dtype=int)

    #population = np.random.randint(2, size=(p, hypothesis_len))


def fitness(hypothesis):
    volume_of_hypothesis = get_volume_regarding_hypothesis(hypothesis)
    return e ** (-c * ((100 - volume_of_hypothesis) ** 2))


def pr(hypothesis):
    total_fitness = 0
    for idx in range(p):
        total_fitness += fitness(population[idx])
    return fitness(hypothesis) / total_fitness


def select_hypothesis():
    rand_num = np.random.random()
    total = 0
    idx = np.random.randint(p)
    while True:
        idx += 1
        idx %= p
        total = total + pr(population[idx])
        if total > rand_num:
            break
    return idx


def selection():
    amount_selection = int((1 - r) * p)
    if amount_selection % 2 == 1:
        amount_selection += 1
    for idx in range(amount_selection):
        population_s.append(population[select_hypothesis()].copy())


def crossover_operator(hypothesis1, hypothesis2):
    split_idx = np.random.randint(hypothesis_len)
    hypothesis1[:split_idx], hypothesis2[:split_idx] = hypothesis2[:split_idx], hypothesis1[:split_idx]
    return [hypothesis1, hypothesis2]


def crossover():
    for idx in range(round(r * p / 2)):
        new_hypothesis_pair = crossover_operator(population[select_hypothesis()], population[select_hypothesis()])
        population_s.append(new_hypothesis_pair[0].copy())
        population_s.append(new_hypothesis_pair[1].copy())


def mutation():
    for idx in range(round(m * p)):
        rand_idx = np.random.randint(len(population_s))
        rand_hypothesis = population_s[rand_idx]
        rand_idx = np.random.randint(p)
        if rand_hypothesis[rand_idx] == 0:
            rand_hypothesis[rand_idx] = 1
        else:
            rand_hypothesis[rand_idx] = 0


def update():
    global population
    global population_s

    population = population_s.copy()
    population_s = []


def get_max_fitness():
    fitness_list = []
    for hypothesis in population:
        fitness_list.append(fitness(hypothesis))
    max_idx = fitness_list.index(max(fitness_list))
    print(get_volume_regarding_hypothesis(population[max_idx]))
    return max(fitness_list)


count = 0

set_population()
set_volume_list()

max_fitness = get_max_fitness()

while max_fitness < fitness_threshold:

    selection()
    print('count: ', count, 'max_fitness: ', max_fitness, 'volume: ')
    crossover()
    mutation()
    update()
    if get_max_fitness() > max_fitness:
        max_fitness = get_max_fitness()
    count += 1
    if count > 500:
        break

print('max fitness: ', max_fitness)
