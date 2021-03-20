#!/usr/bin/env python

from math import ceil
from copy import deepcopy
import heapq


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


def calculate_median_list_heap(input_data):
    heap_high = [input_data[0]]
    heap_low = [-1 * input_data[1]]
    median_list = [input_data[0], input_data[1]]

    for value in input_data[2:]:
        if value <= -1 * heapq.nsmallest(1, heap_low)[0]:
            heapq.heappush(heap_low, -1 * value)
        else:
            heapq.heappush(heap_high, value)

        if len(heap_low) > len(heap_high) + 1:
            head = -1 * heapq.heappop(heap_low)
            heapq.heappush(heap_high, head)
        if len(heap_high) > len(heap_low):
            head = heapq.heappop(heap_high)
            heapq.heappush(heap_low, -1 * head)

        median_list.append(-1 * heap_low[0])

    return median_list


if __name__ == "__main__":
    test_data_1 = [1, 3, 5]
    test_data_2 = [1, 3, 5, 7]
    data = read_data()

    assert calculate_median(test_data_1) == 3
    assert calculate_median(test_data_2) == 3

    assert calculate_median_list(test_data_1) == [1, 1, 3]
    assert calculate_median_list(test_data_2) == [1, 1, 3, 3]

    data_median_list = calculate_median_list_heap(data)
    assert sum(data_median_list) % 10000 == 1213

    print "All good."
