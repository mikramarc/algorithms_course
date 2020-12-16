#!/usr/bin/env python

from math import ceil
from copy import deepcopy

def read_data():
    data = []
    text_file = open("../data/median.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines:
        data.append(int(line[:-1]))
    
    return data

def calculate_median(sorted_arr):
    return sorted_arr[int(ceil(float(len(sorted_arr))/2)) - 1]

def calculate_median_list(input_data):
    median_list = []
    for idx in range(1, len(input_data) + 1):
        tmp_input_data = deepcopy(input_data[:idx])
        tmp_input_data.sort()
        median_list.append(calculate_median(tmp_input_data))

    return median_list

if __name__ == "__main__":
    test_data_1 = [1, 3, 5]
    test_data_2 = [1, 3, 5, 7]
    data = read_data()

    assert calculate_median(test_data_1) == 3
    assert calculate_median(test_data_2) == 3

    assert calculate_median_list(test_data_1) == [1, 1, 3]
    assert calculate_median_list(test_data_2) == [1, 1, 3, 3]

    data_median_list = calculate_median_list(data)
    assert sum(data_median_list) % 10000 == 1213

    print "All good."