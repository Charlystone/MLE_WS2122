
import numpy as np
from math import e

# capacity in liter
capacity = 100

#List of random float numbers with size 100
def get_rand_volumes(list_size, max_volume):
    volumes = np.random.random(list_size)
    for i in range(list_size):
        volumes[i] = round(volumes[i], 3)
        volumes[i] = volumes[i] * (max_volume - 1) + 1
    return volumes

#10 Genoms with 100 Bits, p(1) = 0.182, only genoms with volume <= 100 allowed
def get_population(population_size, genom_size, volumes):
    population = []
    j = 0
    while j <= population_size:
        genom = np.random.random((1, genom_size)).tolist()[0]
        for i in range(genom_size):
            if genom[i] <= 0.182: # p(1) = 0.182
                genom[i] = 1
            else:
                genom[i] = 0
        if calc_volume_regarding_genom(volumes, genom) <= 100.00: #only genoms with volume <= 100 allowed
            population.append(genom)
            j += 1
    population
    return population

def calc_volume_regarding_genom(volumes, genom):

    volume_arr = volumes * genom
    return volume_arr.sum()

def fitness(c, genom, volumes):
    volume = calc_volume_regarding_genom(volumes, genom)
    return e**(-c * ((100-volume)**2))

volumes = get_rand_volumes(100, 10)

population = get_population(10, 100, volumes)




for i in range(10):
    print('Fitness of Genom ', i, ': ', fitness(0.01, population[i],volumes))


# 100 - fitness(population?) = as close as possible to zero