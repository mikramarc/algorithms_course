#!/usr/bin/env python

import re
import random
from copy import deepcopy
from collections import defaultdict

def read_adacency_list():
    text_file = open("../data/SCC.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    result = {}
    for i in range(len(lines)):
        result[i+1] = []

    for line in lines:
        line_list = [int(x) for x in re.split(r' +', line)[:-1]]
        result[line_list[0]].append(line_list[1])

    return result

def reverse_graph(graph):
    result = {}
    for i in range(len(graph)):
        result[i+1] = []

    for tail, head in graph.iteritems():
        for node in head:
            result[node].append(tail)
    return result

if __name__ == "__main__":
    # graph = read_adacency_list()
    graph = {1: [2, 3],
             2: [4], 
             3: [4],
             4: []}
    print graph
    print reverse_graph(graph)

    # print graph[1]