#!/usr/bin/env python

import re
import sys

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

def floyd_warshall(graph):
    num_of_vertieces = len(graph)
    A = []

    for i in range(0, num_of_vertieces):
        A.append([])
        for j in range(0, num_of_vertieces):
            A[i].append(0)
            if i == j:
                continue
            elif j+1 in graph[i+1]:
                A[i][j] = graph[i+1][j+1]
            else:
                A[i][j] = float('inf')

    for k in range(1, num_of_vertieces+1):
        print k
        for i in range(0, num_of_vertieces):
            for j in range(0, num_of_vertieces):
                A[i][j] = min(A[i][j], A[i][k-1] + A[k-1][j])

    result = []
    for i in range(0, num_of_vertieces):
        for j in range(0, num_of_vertieces):
            if i == j and A[i][j] < 0:
                return None
            result.append([i+1, j+1, A[i][j]])

    return result

if __name__ == "__main__": 
    graph = read_data('g3.txt')
    
    # graph = {1: {2: -2,},
    #          2: {3: -1},
    #          3: {1: 4, 4: 2, 5: -3},
    #          4: {},
    #          5: {},
    #          6: {4: 1, 5: -4}}

    result = floyd_warshall(graph)
    if result is None:
        print "Negative cycle"
        sys.exit(0)

    final_result = float('inf')
    for pair in result:
        if pair[2] < final_result:
            final_result = pair[2]
    print final_result
