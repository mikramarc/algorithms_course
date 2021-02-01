#!/usr/bin/env python

import re

def read_data(filename):
    graph = {}
    text_file = open("../data/{}".format(filename), "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        line_list = [int(x) for x in re.split(r' +', line[:-1])]
        if line_list[0] not in graph:
            graph[line_list[0]] = {}
        graph[line_list[0]][line_list[1]] = line_list[2]

    return graph

if __name__ == "__main__": 
    # graph = read_data('g1.txt')
    graph = {1: {2: -2,},
             2: {3: -1},
             3: {1: 4, 4: 2, 5: -3},
             4: {},
             5: {},
             6: {4: 1, 5: -4}}

    num_of_edges = len(graph)
    A = []

    for i in range(0, num_of_edges):
        A.append([])
        for j in range(0, num_of_edges):
            A[i].append([])
            if i == j:
                A[i][j].append(0)
            elif j+1 in graph[i+1]:
                A[i][j].append(graph[i+1][j+1])
            else:
                A[i][j].append(float('inf'))
    
    print A

    # for k in range(1, num_of_edges+1):
    #     for i in range(1, num_of_edges+1):
    #         for j in range(1, num_of_edges+1):
    #             pass
