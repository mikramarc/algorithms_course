#!/usr/bin/env python

import re
import random
from copy import deepcopy
from collections import defaultdict
import sys

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

class DFS(object):
    def __init__(self, graph):
        self.graph = graph
        self.explored_nodes = set()

    def run(self, start_node):
        explored_nodes_list = list(self.dfs(start_node))
        self.explored_nodes.clear()
        return explored_nodes_list

    def dfs(self, start_node):
        self.explored_nodes.add(start_node)
        for node in self.graph[start_node]:
            if node not in self.explored_nodes:
                self.explored_nodes |= self.dfs(node)
        return self.explored_nodes

if __name__ == "__main__":
    # graph = read_adacency_list()
    graph_1 = {1: [2, 3],
             2: [4], 
             3: [4],
             4: []}

    graph_2 = {1: [7],
               2: [5], 
               3: [9],
               4: [1],
               5: [8],
               6: [3, 8],
               7: [4, 9],
               8: [2],
               9: [6]}

    print graph_2
    dfs = DFS(graph_2)
    print dfs.run(9)

    # print graph[1]