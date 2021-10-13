
import numpy as np

# capacity in liter
capacity = 100
from math import e

#List of random float numbers with size 100
def get_rand_volumes(list_size, max_volume):
    volumes = np.random.random(list_size)
    for i in range(list_size):
        volumes[i] = round(volumes[i], 3)
        volumes[i] = volumes[i] * (max_volume - 1) + 1
    return volumes

#10 Genoms with 100 Bits
def get_population(population_size, genom_size):
    return np.random.randint(2, size=(genom_size,population_size))

def calc_volume_regarding_genom(volumes, genom):

    volume_arr = volumes * genom
    return volume_arr.sum()

population = get_population(100, 10)

print(population)

def fitness(c, genom, volumes):
    volume = calc_volume_regarding_genom(volumes, genom)
    return e**(-c * ((100-volume)**2))

volumes = get_rand_volumes(100, 10)

print(volumes)

print('-------')

for i in range(10):
    print(fitness(0.01, population[i],volumes))


# 100 - fitness(population?) = as close as possible to zero