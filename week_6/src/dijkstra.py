#!/usr/bin/env python

import re


def read_adacency_list():
    graph = []
    text_file = open("../data/dijkstra_data.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for idx, line in enumerate(lines):
        graph.append([])
        line_list = [x for x in re.split(r'\t+', line)[:-1]][1:]
        for element in line_list:
            node_and_dist = [int(x) for x in re.split(r',+', element)]
            graph[idx].append(node_and_dist)

    return graph


class Dijkstra(object):
    def __init__(self, graph):
        self.graph_ = graph
        self.processed_nodes_ = []
        self.shortest_paths_ = [1000000] * len(self.graph_)

    def run(self, start_node):
        self.processed_nodes_.append(start_node)
        self.shortest_paths_[start_node - 1] = 0

        while len(self.processed_nodes_) < len(self.graph_):
            current_shortest_path = 1000000
            current_node_to_be_processed = -1
            for processed_node in self.processed_nodes_:
                for adjacent_node in self.graph_[processed_node-1]:
                    if adjacent_node[0] in self.processed_nodes_:
                        continue
                    if self.shortest_paths_[processed_node-1] + adjacent_node[1] < current_shortest_path:
                        current_shortest_path = self.shortest_paths_[processed_node-1] + adjacent_node[1]
                        current_node_to_be_processed = adjacent_node[0]
            self.processed_nodes_.append(current_node_to_be_processed)
            self.shortest_paths_[current_node_to_be_processed - 1] = current_shortest_path

    def get_shortest_paths(self):
        return self.shortest_paths_

    def get_shortest_path_to_node(self, node_idx):
        return self.shortest_paths_[node_idx - 1]


if __name__ == "__main__":    
    test_graph = [[[2, 1], [3, 4]],
                  [[1, 1], [3, 2], [4, 6]],
                  [[1, 4], [2, 2], [4, 3], [5, 100]],
                  [[2, 6], [3, 3], [5, 1]],
                  [[3, 100], [4, 1], [6, 5]],
                  [[5, 5]]]

    d_test = Dijkstra(test_graph)
    d_test.run(1)

    assert d_test.get_shortest_paths() == [0, 1, 3, 6, 7, 12]
    assert d_test.get_shortest_path_to_node(4) == 6

    assignent_graph = read_adacency_list()
    shortest_paths_to_be_checked = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    answer = []
    d = Dijkstra(assignent_graph)
    d.run(1)
    for node in shortest_paths_to_be_checked:
        answer.append(d.get_shortest_path_to_node(node))

    assert answer == [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]

    print "All good."
