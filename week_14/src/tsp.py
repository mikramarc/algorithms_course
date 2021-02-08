#!/usr/bin/env python

import re
import sys
from math import sqrt

def read_data(filename):
    graph = []
    text_file = open("../data/{}".format(filename), "r")
    lines = text_file.readlines()
    text_file.close()

    for i in range(1, len(lines)):
        graph.append([])
        for j in range(1, len(lines)):
            city_1_coord = [float(x) for x in re.split(r' +', lines[i][:-1])]
            city_2_coord = [float(x) for x in re.split(r' +', lines[j][:-1])]
            graph[i-1].append(sqrt((city_1_coord[0] - city_2_coord[0])**2 + (city_1_coord[1] - city_2_coord[1])**2))

    return graph

def get_subset_from_int(i):
    return '{0:b}'.format(i)

def get_int_from_subset(subset):
    return int(subset, 2)

def get_int_from_subset_without_val(i, val):
    # val range: 1 - n
    current_subset = list(get_subset_from_int(i))[::-1]
    current_subset[val-1] = '0'
    return_subset = current_subset[::-1]
    return get_int_from_subset(''.join(return_subset))

def get_set_from_subset_string(subset):
    s = []
    #TODO: implement
    return s

if __name__ == "__main__":
    assert get_subset_from_int(7) == '111'
    assert get_int_from_subset('111') == 7
    assert get_int_from_subset_without_val(7, 2) == 5

    test_graph= [[0, 1, 3, 6],
                 [1, 0, 2, 4],
                 [3, 2, 0, 5],
                 [6, 4, 5, 0]]

    # graph = read_data('tsp.txt')
    A = [[0]]
    number_of_subsets = 2**(len(test_graph)-1)  # always contains 1

    for s in range(1, number_of_subsets):
        A.append([float('inf')])

    for m in range(1, len(graph)):
        for s in range(1, number_of_subsets+1):
            for j in get_set_from_subset_string(get_subset_from_int(s)):
                #TODO: Implement
                pass

print "All good"