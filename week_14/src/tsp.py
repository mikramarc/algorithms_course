#!/usr/bin/env python

import re
import sys
from math import sqrt
from copy import deepcopy
import itertools

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
  
def find_subsets(s, n): 
    return list(itertools.combinations(s, n))

def encode_list(l):
    return ",".join([str(x) for x in l])

def decode_list(string):
    return [float(x) for x in string.split(",")]


if __name__ == "__main__":
    graph= [[0, 1, 3, 6],
            [1, 0, 2, 4],
            [3, 2, 0, 5],
            [6, 4, 5, 0]]

    # graph = read_data('tsp.txt')

    A = ['0'] * 2**(len(graph)-1)

    # print find_subsets(range(1, len(graph)), 2)

    for m in range(1, len(graph)+1):
        print m
        for s in [(0,) + x for x in find_subsets(range(1, len(graph)), m)]:
            l = [float('inf')]*(s[-1]+1)
            A[int_from_subset(s)] = encode_list(l)


    for m in range(1, len(graph)+1):
        print m
        for s in [(0,) + x for x in find_subsets(range(1, len(graph)), m)]:
            list_from_set_s = decode_list(A[int_from_subset(s)])
            for j in s:
                if j == 0:
                    continue
                current_res = float('inf')
                for k in s:
                    if k == j:
                        continue
                    t = set(s)
                    t.remove(j)
                    list_from_set_t = decode_list(A[int_from_subset(tuple(t))])

                    new_res = list_from_set_t[k]+graph[k][j]  # k from shorter set is shorter..?
                    if new_res < current_res:
                        current_res = new_res
                list_from_set_s[j] = current_res
                A[int_from_subset(s)] = encode_list(list_from_set_s)

    final_subset_int = int_from_subset(range(0, len(graph)))
    final_list = decode_list(A[final_subset_int])
    final_result = float('inf')
    for j in range(1, len(graph)):
        final_result = min(final_result, final_list[j] + graph[j][0])

    print final_result
