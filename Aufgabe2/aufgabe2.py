# Charly Wallaston Mar.NR. 2011897
# MLE WS 21/22 Aufgabe2

import numpy as np
import pandas as pd
import random
from math import e

# create 2D array with ramdom int values, diagonals=0, array[x][y]=array[y][x]

n_cities = 100
last_fitness = 1000000000

# create 2D array
distances = np.random.randint(20, 800, size=(n_cities, n_cities))

# convert all diagonals to 0
np.fill_diagonal(distances, 0)

# make distances[x][y] = distances[y][x]
for x in range(n_cities):
    if x == n_cities / 2:
        break
    for y in range(n_cities):
        distances[x][y] = distances[y][x]

# convert array in pandas DataFrame
df_distances = pd.DataFrame(distances)

print(df_distances)


# swap tow random positions in route array
def move_one_step_at_random(route, i1, i2):
    route[i1], route[i2] = route[i2], route[i1]
    return route


# undo the swap
def undo_move(route, i1, i2):
    route[i1], route[i2] = route[i2], route[i1]
    return route


# get distance of route out of distance df
def fitness(df, route):
    total_distance = 0
    for i in range(len(route)):
        station = route[i]
        if i + 1 == len(route):
            nextStation = 0
        else:
            nextStation = route[i + 1]
        total_distance += df[station][nextStation]
    return total_distance


# minimize length of route
def get_shortest_route_simulated_annealing(df, start_temp, epsilon):
    hypothesis = df.index.values.tolist()
    last_fitness = fitness(df, hypothesis)
    temp = start_temp
    while True:
        i1, i2 = random.sample(hypothesis, 2)
        new_fitness = fitness(df, move_one_step_at_random(hypothesis, i1, i2))

        if new_fitness <= last_fitness:
            last_fitness = new_fitness
            print(new_fitness)
            print(hypothesis)
        elif random.uniform(0, 1) < e ** ((last_fitness - new_fitness) / temp):
            last_fitness = new_fitness
        else:
            hypothesis = undo_move(hypothesis, i1, i2)
        temp = temp - epsilon
        if temp < epsilon:
            break
    return hypothesis


shortest_route = get_shortest_route_simulated_annealing(df_distances, 45, 0.01)
print('\n', '\n', '\n', '\n', '\n')
print('shortest route: ', shortest_route)
print('shortest distance: ', fitness(df_distances, shortest_route))
