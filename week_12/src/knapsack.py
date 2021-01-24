#!/usr/bin/env python

import re

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

if __name__ == "__main__": 
    knapsack_problem = read_data('knapsack_big.txt')
    max_capacity = knapsack_problem['size']
    items = knapsack_problem['items']

    # max_capacity = 6
    # items = [[3, 4],
    #          [2, 3],
    #          [4, 2],
    #          [4, 3]]


    A = [0] * (max_capacity + 1)
    A_new = [0] * (max_capacity + 1)

    for i, item in enumerate(items):
        A_new = [0] * (max_capacity + 1)
        print i
        for current_cap in range(0, max_capacity+1):
            if current_cap - item[1] < 0:
                A_new[current_cap] = A[current_cap]
            else:
                A_new[current_cap] = max(A[current_cap], A[current_cap - item[1]] + item[0])
        A = A_new
    print A[-1]