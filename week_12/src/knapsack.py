#!/usr/bin/env python

import re
import itertools

def read_data(filename):
    knapsack_problem = {}
    knapsack_problem['items'] = []
    text_file = open("../data/{}".format(filename), "r")
    lines = text_file.readlines()
    text_file.close()

    knapsack_problem['size'] = int(re.split(r' +', lines[0])[0])
    for line in lines[1:]:
        line_list = [int(x) for x in re.split(r' +', line[:-1])]
        knapsack_problem['items'].append(line_list)

    return knapsack_problem

def get_nearest_lower_num(i, l):
    res = min(l, key=lambda x: abs(x - i))
    if res > i:
       return l[l.index(res)-1]
    return res
    

if __name__ == "__main__": 
    knapsack_problem = read_data('knapsack1.txt')
    max_capacity = knapsack_problem['size']
    items = knapsack_problem['items']

    # max_capacity = 6
    # items = [[3, 4],
    #          [2, 3],
    #          [4, 2],
    #          [4, 3]]

    item_weights = []
    for item in items:
        item_weights.append(item[1])

    possible_capacities= []
    checked_caps = set()
    for L in range(0, len(items)+1):
        for subset in itertools.combinations(item_weights, L):
            res = sum(subset)
            if res > max_capacity:
                break
            if res not in checked_caps:
                checked_caps.add(res)
                possible_capacities.append(res)
    possible_capacities.sort()

    print possible_capacities


    A = [{}]
    for cap in possible_capacities:
        A[0][cap] = 0

    for i, item in enumerate(items):
        print i
        A.append({})
        for current_cap in possible_capacities:
            if current_cap - item[1] < 0:
                A[i+1][current_cap] = A[i][current_cap]
                continue
            if current_cap - item[1] not in possible_capacities:
                A[i+1][current_cap] = (max(A[i][current_cap], A[i][get_nearest_lower_num(current_cap - item[1], possible_capacities)] + item[0]))
            else:
                A[i+1][current_cap] = (max(A[i][current_cap], A[i][current_cap - item[1]] + item[0]))

    print A[-1][max_capacity]

    # a = [1, 4, 7, 10]
    # print get_nearest_lower_num(10, a)