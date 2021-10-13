
# Charly Wallaston Mar.NR. 2011897
# MLE WS 21/22 Aufgabe1

import numpy as np
import pandas as pd
import random

# create 2D array with ramdom int values, diagonals=0, array[x][y]=array[y][x]

n_cities = 100

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
def get_shortest_route(df, reps):
    hypothesis = df.index.values.tolist()
    last_fitness = fitness(df, hypothesis)
    for x in range(reps):
        i1, i2 = random.sample(hypothesis, 2)
        new_fitness = fitness(df, move_one_step_at_random(hypothesis, i1, i2))
        if new_fitness <= last_fitness:
            last_fitness = new_fitness
            print(new_fitness)
            print(hypothesis)
        else:
            hypothesis = undo_move(hypothesis, i1, i2)

    return hypothesis


shortest_route = get_shortest_route(df_distances, 1000)
print('\n', '\n', '\n', '\n', '\n')
print('shortest route: ', shortest_route)
print('shortest distance: ', fitness(df_distances, shortest_route))
print('\n', '\n', '\n', '\n', '\n')

# Realistic sample with real data, data source: http://www.auslandversicherungen.de/entfernungstabelle.html

# get and set up data set
df = pd.read_csv('./distance_40_german_cities.csv', index_col=0)
city_names = df.index.tolist()
df = df.set_axis(city_names, axis=1, inplace=False)

# convert index and colum names into integer, for better handling
# numbers form 0 to 39
idx_numbers = np.arange(start=0, stop=40, step=1).tolist()

df = df.set_axis(idx_numbers, axis=1, inplace=False)
df = df.set_axis(idx_numbers, axis=0, inplace=False)

shortest_route = get_shortest_route(df, 10000)
print('\n', '\n', '\n', '\n', '\n')

print('shortest route: ')

for station in shortest_route:
    print(city_names[station])

print('shortest route: ', shortest_route)
print('shortest distance: ', fitness(df, shortest_route), 'km')
