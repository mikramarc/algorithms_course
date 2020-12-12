#!/usr/bin/env python

import re
import random
from copy import deepcopy
from collections import defaultdict
import sys

sys.setrecursionlimit(50000)

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
        self.finishing_time = 0
        self.finishing_times = {}
        self.sccs = {}
        self.previous_scc = set()
        self.s = 0

    def run_dfs(self, start_node):
        self.dfs(start_node)
        return self.explored_nodes, self.finishing_times

    def dfs(self, start_node):
        self.explored_nodes.add(start_node)
        self.sccs[self.s].append(start_node)
        for node in self.graph[start_node]:
            if node not in self.explored_nodes:
                self.dfs(node)
        self.finishing_time += 1
        self.finishing_times[start_node] = self.finishing_time

    def run_dfs_loop(self):
        self.dfs_loop()
        return self.sccs, self.finishing_times

    def dfs_loop(self):
        for i in range(len(self.graph), 0, -1):
            print i
            if i not in self.explored_nodes:
                self.s = i
                self.sccs[self.s] = []
                self.run_dfs(i)


if __name__ == "__main__":
    graph = read_adacency_list()
    # graph_1 = {1: [2, 3],
    #          2: [4], 
    #          3: [4],
    #          4: []}

    # graph_2 = {1: [7],
    #            2: [5], 
    #            3: [9],
    #            4: [1],
    #            5: [8],
    #            6: [3, 8],
    #            7: [4, 9],
    #            8: [2],
    #            9: [6]}

    # graph = {1: [4],
    #            2: [8],
    #            3: [6],
    #            4: [7],
    #            5: [2],
    #            6: [9],
    #            7: [1],
    #            8: [5, 6],
    #            9: [3, 7]}

    graph_rev = reverse_graph(graph)
    dfs = DFS(graph_rev)
    res = dfs.run_dfs_loop()
    node_to_time_mapping = res[1]
    graph_nodes_as_time_mapping = {}
    for key, value in graph.iteritems():
        graph_nodes_as_time_mapping[node_to_time_mapping[key]] = [node_to_time_mapping[x] for x in value]

    dfs_2 = DFS(graph_nodes_as_time_mapping)
    res = dfs_2.run_dfs_loop()
    final_res = res[0]

    answer = ""
    for key, value in final_res.iteritems():
        answer += str(len(value)) + ","

    answer = answer[:-1]
    print answer