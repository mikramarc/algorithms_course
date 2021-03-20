#!/usr/bin/env python

import re
import random
from copy import deepcopy
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def find_largest_elements(arr, how_many):
    results = []
    for i in range(how_many):
        if len(arr) == 0:
            results.append(0)
            continue
        result = max(arr)
        arr.remove(result)
        results.append(result)
    return results


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
    def __init__(self, graph, ignore_ft = False):
        self.graph = graph
        self.explored_nodes = set()
        self.finishing_time = 0
        self.ignore_ft = ignore_ft
        if not ignore_ft:
            self.finishing_times = [None] * (len(graph) + 1)
        else:
            self.finishing_times = []
        self.sccs = [None] * (len(graph) + 1)
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
        if not self.ignore_ft:
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

    graph_rev = reverse_graph(graph)
    dfs = DFS(graph_rev)
    res = dfs.run_dfs_loop()
    node_to_time_mapping = res[1]
    del dfs
    graph_nodes_as_time_mapping = {}
    for key, value in graph.iteritems():
        graph_nodes_as_time_mapping[node_to_time_mapping[key]] = [node_to_time_mapping[x] for x in value]

    dfs_2 = DFS(graph_nodes_as_time_mapping, True)
    res = dfs_2.run_dfs_loop()
    final_res = res[0]
    print final_res

    answer = []
    for value in final_res:
        if value is not None:
            answer.append(len(value))

    print find_largest_elements(answer, 5)
