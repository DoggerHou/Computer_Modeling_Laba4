import numpy as np
import scipy
from matplotlib import pyplot as plt
import random


class City:


    def __init__(self, coordinates):
        self.number = coordinates.split()[0]
        self.__coordinates = [int(i) for i in coordinates.split()[1:]]


    def get_coordinates(self):
        return self.__coordinates


    def get_city(self):
        return self.number


# Получить расстояние между двумя городами
def get_distance(city1, city2):
    x1, y1, z1 = city1.get_coordinates()
    x2, y2, z2 = city2.get_coordinates()
    return np.sqrt(np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2))


def sum_distance(cyt):
    sum = 0
    for i in range(0, len(cyt)-1):
        sum += get_distance(cyt[i], cyt[i+1])
    sum += get_distance(cyt[0], cyt[-1])
    return sum


def mutate(city1, city2):
    return 0


# Одноточечное скрещивание
def single_crossover(parent1, parent2):
    return 0


# Двухточечное скрещивание
def double_crossover(parent1, parent2):
    U1 = random.randrange(1, len(parent1)-1)
    U2 = random.randrange(1, len(parent1)-1)
    # Чтобы не выбрать неподходящие точки разрыва
    while U1 + 1 == U2 or U1 == U2 or U1 - 1 == U2:
        U2 = random.randrange(1, len(parent1)-1)

    child1 = []
    used = []

    for i in range(len(parent1)):
        for i in range(U1):
            child1.append(parent1[i])
            used.append(parent1[i])
        for i in range(U1, U2):
            if not parent2[i] in used:
                child1.append(parent2[i])
                used.append(parent2[i])
        for i in range (U2, len(parent1)):
            if not parent1[i] in used:
                child1.append(parent1[i])



    child2 = []


    return [child1, child2]





with open('10.txt') as f:
    data = f.readlines()
    cities = [City(i) for i in data]


GENERATION_SIZE = 50                            # Размер популяции

population = []
estimate_best_route = []



# Создали случайную популяцию
for i in range(len(cities)):
    buff = cities.copy()
    random.shuffle(buff)
    population.append(buff)
for i in population:
    print('Расстояние = ' + str(sum_distance(i)), *i, '\n\n', sep='\n')


# Выбираем двух родителей для скрещенивания
for i in range(GENERATION_SIZE):
    u1 = random.randrange(0, len(population))
    u2 = random.randrange(0, len(population))
    #Чтобы не выбрать одного родителя
    while u1 == u2:
        u2 = random.randrange(0, len(population))

    if len(cities) > 7:
        child = double_crossover(population[u1], population[u2])
    else:
        child = double_crossover(population[u1], population[u2])

