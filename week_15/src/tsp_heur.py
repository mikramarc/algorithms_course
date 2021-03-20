#!/usr/bin/env python

import re
from math import sqrt
import itertools
import time


def read_data(filename):
    data = []
    text_file = open("../data/{}".format(filename), "r")
    lines = text_file.readlines()
    text_file.close()

    for i in range(1, len(lines)):
        data.append([])
        city_1_coord = [float(x) for x in re.split(r' +', lines[i][:-2])[1:3]]
        data[i-1] = city_1_coord

    return data


def euclidean_distance(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


if __name__ == "__main__":
    data = read_data('nn.txt')
    
    cities_not_visited = set(range(1, len(data)))
    current_city = 0
    new_city = 0
    result = 0

    while len(cities_not_visited) > 0:
        current_distance = float('inf')
        for city in cities_not_visited:
            new_distance = euclidean_distance(data[current_city], data[city])
            if new_distance < current_distance:
                current_distance = new_distance
                new_city = city
        result += current_distance
        current_city = new_city
        cities_not_visited.remove(new_city)

    result += euclidean_distance(data[0], data[new_city])
    print result
