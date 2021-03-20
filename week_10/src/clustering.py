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
    text_file = open("../data/big_data_edges_max_2.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        edges.append([int(x) for x in re.split(r' +', line)])
    return edges


def read_data_big():
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
            break
        
        union_find.merge_two_unions(union_find.get_vertex_union(edge[0]),
                                    union_find.get_vertex_union(edge[1]))

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
        
        union_find.merge_two_unions(union_find.get_vertex_union(edge[0]),
                                    union_find.get_vertex_union(edge[1]))
    
    clusters = union_find.get_unions()
    return len(clusters)


def hamming_distance(point_1, point_2):
    distance = 0
    for bit_1, bit_2 in zip(point_1, point_2):
        if bit_1 != bit_2:
            distance += 1
    return distance


def get_all_distances_0_1_or_2(byte):
    result = []
    result.append(byte)
    for i, _ in enumerate(byte):
        tmp_byte = list(byte)
        tmp_byte[i] = str(int(not bool(int(tmp_byte[i]))))
        result.append("".join(tmp_byte))

    for i, _ in enumerate(byte):
        for j in range(i+1, len(byte)):
            tmp_byte = list(byte)
            tmp_byte[i] = str(int(not bool(int(tmp_byte[i]))))
            tmp_byte[j] = str(int(not bool(int(tmp_byte[j]))))
            result.append("".join(tmp_byte))
    return result


if __name__ == "__main__":
    test_edges_1 = [[1, 2],
                    [5, 6],
                    [3, 4],
                    [1, 7]]
    test_verticies_1 = range(1, 8)
    test_result = max_clustering(test_verticies_1, test_edges_1)
    print test_result

    test_edges_2 = [[1, 2],
                    [3, 4],
                    [1, 1],
                    [2, 1]]
    test_verticies_2 = range(1, 5)
    test_result = max_clustering(test_verticies_2, test_edges_2)
    print test_result

    edges = read_data()
    edges_fin = [[x[0], x[1]] for x in edges]
    verticies = range(1, 200001)
    result = max_clustering(verticies, edges_fin)
    print result
