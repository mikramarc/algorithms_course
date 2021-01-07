#!/usr/bin/env python

import re

class UnionFind(object):
    def __init__(self, initial_verticies):
        self.initial_verticies = initial_verticies
        self.vertex_to_union_mapping= {}
        self.unions = {}

        self.initialize()

    def initialize(self):
        for vertex in self.initial_verticies:
            self.vertex_to_union_mapping[vertex] = vertex
            self.unions[vertex] = []
            self.unions[vertex].append(vertex)

    def get_vertex_union(self, vertex):
        return self.vertex_to_union_mapping[vertex]

    def get_unions(self):
        return self.unions

    def merge_two_unions(self, union_1_leader, union_2_leader):
        if union_1_leader == union_2_leader:
            return
        if len(self.unions[union_1_leader]) >= len(self.unions[union_2_leader]):
            new_leader = union_1_leader
            old_leader = union_2_leader
        else:
            new_leader = union_2_leader
            old_leader = union_1_leader

        for vertex in self.unions[old_leader]:
            self.vertex_to_union_mapping[vertex] = new_leader
        self.unions[new_leader] += self.unions[old_leader]
        del self.unions[old_leader]


def read_data():
    edges = []
    text_file = open("../data/clustering1.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        edges.append([int(x) for x in re.split(r' +', line)])
    return edges

def read_data_2():
    edges = []
    text_file = open("../data/clustering_big.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        edges.append([x for x in [x for x in re.split(r' +', line)][:-1]])
    return edges

def clustering(verticies, edges, clusters):
    edges.sort(key=lambda x: x[2])
    union_find = UnionFind(verticies)

    for idx, edge in enumerate(edges):
        current_unions = union_find.get_unions()
        print current_unions
        
        if len(current_unions) == clusters:
            remaining_edges = edges[idx:]
            # max_spacing = edge[2]
            break
        
        union_find.merge_two_unions(union_find.get_vertex_union(edge[0]), union_find.get_vertex_union(edge[1]))

    for edge in remaining_edges:
        if union_find.get_vertex_union(edge[0]) != union_find.get_vertex_union(edge[1]):
            max_spacing = edge[2]
            break
    
    clusters = union_find.get_unions()
    return (clusters, max_spacing)
    
def max_clustering(verticies, edges):
    union_find = UnionFind(verticies)

    for idx, edge in enumerate(edges):
        current_unions = union_find.get_unions()
        
        union_find.merge_two_unions(union_find.get_vertex_union(edge[0]), union_find.get_vertex_union(edge[1]))
    
    clusters = union_find.get_unions()
    return len(clusters)

def hamming_distance(point_1, point_2):
    distance = 0
    for bit_1, bit_2 in zip(point_1, point_2):
        if bit_1 != bit_2:
            distance += 1
    return distance

if __name__ == "__main__":
    # test_edges = [[1, 2, 1],
    #               [2, 3, 2],
    #               [4, 5, 1],
    #               [3, 6, 7],
    #               [5, 6, 1],
    #               [1, 4, 5],
    #               [2, 6, 6]]
    # test_verticies = range(1, 7)
    # test_result = clustering(test_verticies, test_edges, 2)
    # print test_result

    # test_edges_2 = [[1, 2, 1],
    #               [2, 5, 5],
    #               [5, 6, 1],
    #               [3, 4, 1],
    #               [4, 5, 6],
    #               [1, 3, 7],
    #               [1, 7, 1]]
    # test_verticies_2 = range(1, 8)
    # test_result = clustering(test_verticies_2, test_edges_2, 3)
    # print test_result

    test_edges_3 = [[1, 2],
                  [5, 6],
                  [3, 4],
                  [1, 7]]
    test_verticies_3 = range(1, 8)
    test_result = max_clustering(test_verticies_3, test_edges_3)
    print test_result

    test_edges_4 = [[1, 2],
                    [3, 4]]
    test_verticies_4 = range(1, 5)
    test_result = max_clustering(test_verticies_4, test_edges_4)
    print test_result

    data_big = read_data_2()
    str1 = ''.join(data_big[1])
    print str1

    byte_to_vertex_mapping = {}

    for idx, line in enumerate(data_big):
        byte_to_vertex_mapping[''.join(data_big[idx])] = idx + 1

    # TODO: 
    # for each node list all bytes with distance 1 or 2
    # for each node and each byte of those find vertex with that byte if exists, create a list
    # run max_clustering over that list


    # vertieces = range(1, 200001)
    # edges = []
    # for i in range(0, 200000):
    #     print i
    #     for j in range(i+1, 200000):
    #         hd = hamming_distance(data_big[i], data_big[j])
    #         if hd < 3:
    #             edges.append([i+1, j+1, hd])

    # with open('big_data_edges_max_2.txt', 'w') as f:
    #     for edge in edges:
    #         f.write("{} {} {}\n".format(edge[0], edge[1], edge[2]))


    # edges = read_data()
    # # print edges
    # verticies = range(1, 501)

    # result = clustering(verticies, edges, 4)
    # print result[1]

    # print "All good."
