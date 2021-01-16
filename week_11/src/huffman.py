#!/usr/bin/env python

import heapq

class Metanode(object):
    def __init__(self):
        self.nodes = []
        self.metanode_weight = 0

    def __lt__(self, other):
        return self.metanode_weight < other.metanode_weight

    def __str__(self):
        return str(self.nodes) + '\n' + str(self.metanode_weight)

    def add_metanode(self, metanode):
        new_nodes = []
        new_nodes.append(self.nodes)
        new_nodes.append(metanode.nodes)
        self.nodes = new_nodes

        self.metanode_weight += metanode.metanode_weight    

    def add_node(self, node):
        self.nodes.append(node[0])
        self.metanode_weight += node[1]


def read_data():
    data = []
    text_file = open("../data/huffman.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    for idx, line in enumerate(lines[1:]):
        data.append([idx+1, int(line)])
    return data


def transform_data_to_metanodes(data):
    data_metanodes = []
    for node in data:
        metanode = Metanode()
        metanode.add_node(node)
        data_metanodes.append(metanode)
    return data_metanodes


def get_tree_max_depth(tree, depth):
    if len(tree) == 1:
        return depth
    return max(get_tree_max_depth(tree[0], depth+1), get_tree_max_depth(tree[1], depth+1))


def get_tree_min_depth(tree, depth):
    if len(tree) == 1:
        return depth
    return min(get_tree_min_depth(tree[0], depth+1), get_tree_min_depth(tree[1], depth+1))

def huffman(data):
    data_metanodes_heap = transform_data_to_metanodes(data)
    heapq.heapify(data_metanodes_heap)

    while len(data_metanodes_heap) > 2:
        metanode_1 = heapq.heappop(data_metanodes_heap)
        metanode_2 = heapq.heappop(data_metanodes_heap)
        metanode_2.add_metanode(metanode_1)
        heapq.heappush(data_metanodes_heap, metanode_2)

    metanode_1 = heapq.heappop(data_metanodes_heap)
    metanode_2 = heapq.heappop(data_metanodes_heap)
    metanode_2.add_metanode(metanode_1)
    heapq.heappush(data_metanodes_heap, metanode_2)

    max_length = get_tree_max_depth(data_metanodes_heap[0].nodes, 0)
    min_length = get_tree_min_depth(data_metanodes_heap[0].nodes, 0)

    return max_length, min_length

if __name__ == "__main__":
    test_data = [[1, 3], [2, 2], [3, 6],
                 [4, 8], [5, 2], [6, 6]]
    assert huffman(test_data) == (4, 2)
    
    data = read_data()
    assert huffman(data) == (19, 9)

    print "All good."


    