#!/usr/bin/env python

import re
import random
from copy import deepcopy


def read_adacency_list():
    result = {}

    text_file = open("../data/karger_min_cut.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines:
        line_list = [int(x) for x in re.split(r'\t+', line)[:-1]]
        result[line_list[0]] = line_list[1:]

    return result


def contract_edge(graph, n1, n2):
    graph[n1] += graph[n2]
    del graph[n2]
    graph[n1] = [x for x in graph[n1] if not (x == n1 or x == n2)]
    for i in graph:
        graph[i] = [x if x != n2 else n1 for x in graph[i]]


def pick_random_edge(graph):
    n1_random = random.choice(list(graph.keys()))
    n2_random = random.choice(graph[n1_random])
    return n1_random, n2_random


def karger_min_cut(graph):
    while len(graph) > 2:
        n1, n2 = pick_random_edge(graph)
        contract_edge(graph, n1, n2)
    return graph


if __name__ == "__main__":
    graph = read_adacency_list()
    graph_nodes_number = len(graph)
    experiments_number = graph_nodes_number^2
    min_cuts = graph_nodes_number

    for _ in range(experiments_number):
        graph_tmp = deepcopy(graph)
        karger_min_cut(graph_tmp)
        local_min_cuts = len(graph_tmp.itervalues().next())

        if local_min_cuts < min_cuts:
            min_cuts = local_min_cuts
    
    assert min_cuts == 17

    print "All good."
