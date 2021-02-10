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

def bin_from_int(i):
    return '{0:b}'.format(i)

def int_from_bin(binary_str):
    return int(binary_str, 2)

def get_set_from_subset_string(subset):
    s = []
    rev_number = list(subset)[::-1]
    for i, el in enumerate(rev_number):
        if el == '0':
            continue
        if el == '1':
            s.append(i+1)
    return s

def change_element_in_string_bin(string, i, val):
    s = list(string)[::-1]
    s[i] = val
    return ''.join(s[::-1])

def int_from_subset(subset):
    result = 0
    for el in subset:
        if el == 0:
            continue
        result += 2**(el-1)
    return result

def sub_lists(l): 
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists 
    return lists
  
def find_subsets(s, n): 
    return [list(x) for x in list(itertools.combinations(s, n))]


if __name__ == "__main__":
    # print int_from_subset([0, 1])
    # print int_from_subset([1, 3, 0])

    # print find_subsets(range(1, 5), 3)

    graph= [[0, 1, 3, 6],
            [1, 0, 2, 4],
            [3, 2, 0, 5],
            [6, 4, 5, 0]]

    # graph = read_data('tsp.txt')
    A = {}
    A[0] = {0: 0}
    number_of_subsets = 2**(len(graph)-1)  # always contains 1

    for m in range(1, len(graph)+1):
        for s in [[0] + x for x in find_subsets(range(1, len(graph)), m)]:
            A[int_from_subset(s)] = {0: float('inf')}

    # for s in range(1, number_of_subsets):
    #     A.append([float('inf')])
    print A

    for m in range(1, len(graph)+1):
        for s in [[0] + x for x in find_subsets(range(1, len(graph)), m)]:
            for j in s:
                if j == 0:
                    continue
                current_res = float('inf')
                for k in s:
                    if k == j:
                        continue
                    t = deepcopy(s)
                    t.remove(j)
                    new_res = A[int_from_subset(t)][k]+graph[k][j]  # k from shorter set is shorter..?
                    if new_res < current_res:
                        current_res = new_res
                A[int_from_subset(s)][j] = current_res
                print A

    final_subset_int = int_from_subset(range(0, len(graph)))
    final_result = float('inf')
    for j in range(1, len(graph)):
        final_result = min(final_result, A[final_subset_int][j] + graph[j][0])

    print final_result


print "All good"