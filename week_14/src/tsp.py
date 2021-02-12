#!/usr/bin/env python

import re
from math import sqrt
import itertools
import time

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

def int_from_subset(subset):
    result = 0
    for el in subset:
        if el == 0:
            continue
        result += 2**(el-1)
    return result

def int_from_subset_without_num(subset, i):
    result = 0
    for el in subset:
        if el == 0 or el == i:
            continue
        result += 2**(el-1)
    return result
  
def find_subsets(s, n): 
    return itertools.combinations(s, n)


if __name__ == "__main__":
    graph = [[0, 1, 3, 6],
            [1, 0, 2, 4],
            [3, 2, 0, 5],
            [6, 4, 5, 0]]

    graph = read_data('tsp.txt')

    A_prev = [[0]]
    for m in range(1, len(graph)):
        print m
        start_time = time.time()
        A = [[]]*2**(len(graph))
        for s in find_subsets(range(1, len(graph)), m):
            s = (0, ) + s
            subset_int = int_from_subset(s)
            A[subset_int] = [float('inf')]*(s[-1]+1)
            for j in s:
                if j == 0:
                    continue
                subset_int_no_j = int_from_subset_without_num(s, j)
                new_res = float('inf')
                for k in s:
                    if k == j:
                        continue
                    new_res = min(new_res, A_prev[subset_int_no_j][k] + graph[k][j])
                A[subset_int][j] = new_res
        A_prev = A
        print("--- %s seconds ---" % (time.time() - start_time))

    final_subset_int = int_from_subset(range(0, len(graph)))
    final_result = float('inf')
    for j in range(1, len(graph)):
        final_result = min(final_result, A[final_subset_int][j] + graph[j][0])

    print final_result
