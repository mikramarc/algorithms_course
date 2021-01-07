#!/usr/bin/env python

import re

def read_data():
    graph = {}
    text_file = open("../data/edges.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        line_list = [int(x) for x in re.split(r' +', line)]
        if line_list[0] not in graph:
            graph[line_list[0]] = []
        if line_list[1] not in graph:
            graph[line_list[1]] = []

        graph[line_list[0]].append([line_list[1], line_list[2]])
        graph[line_list[1]].append([line_list[0], line_list[2]])

    return graph

if __name__ == "__main__":
    graph = read_data()
    remaining_vertices = [x + 1 for x in range(500)]

    graph = {1: [[2, 1], [4, 3], [3, 4]],
             2: [[1, 1], [4, 2]],
             3: [[1, 4], [4, 5]],
             4: [[1, 3], [2, 2], [3, 5]]}

    remaining_vertices = [x + 1 for x in range(4)]

    current_vertex = 1
    current_cost = 0
    remaining_vertices.remove(1)
    spanning_tree = [1] 

    while remaining_vertices:
        edges = []
        for vertex in spanning_tree:
            for edge in graph[vertex]:
                if edge[0] not in spanning_tree:
                    edges.append(edge)
        min_edge = min(edges, key=lambda x: x[1])
        current_cost += min_edge[1]
        spanning_tree.append(min_edge[0])
        remaining_vertices.remove(min_edge[0])
    print current_cost
    