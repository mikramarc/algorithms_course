#!/usr/bin/env python

from random import randint
from numpy.random import permutation
import time
import sys
from math import ceil

sys.setrecursionlimit(50000)

def partition(A, pivot_idx):
    i = 0
    pivot = A.pop(pivot_idx)

    for j in range(0, len(A)):
        if A[j] < pivot:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1

    return pivot, A[0:i], A[i:]

def choose_random_pivot(A):
    arr_len = len(A)
    return randint(0, arr_len-1)

def choose_first_el_for_pivot(A):
    return 0

def choose_last_el_for_pivot(A):
    arr_len = len(A)
    return arr_len - 1

def choose_median_pivot(A):
    a_0 = A[0]
    a_last = A[-1]
    a_mid = A[int(ceil(float(len(A))/2)-1)]

    a = [a_0, a_last, a_mid]
    a.sort()

    if a[1] == a_0:
        return 0
    elif a[1] == a_last:
        return len(A) -1
    elif a[1] == a_mid:
        return int(ceil(float(len(A))/2)-1)

def quicksort(A, pivot_func):
    m = len(A)
    if m == 0:
        return (0, [])

    pivot_idx = pivot_func(A)
    (pivot, Ai, Aj) = partition(A, pivot_idx)
    result_i = quicksort(Ai, pivot_func)
    result_j = quicksort(Aj, pivot_func)
    return (m-1 + result_i[0] + result_j[0], result_i[1] + [pivot] + result_j[1])


if __name__ == "__main__":
    A = [1, 4, 2, 3, 8, 7, 5, 6]
    assert partition(A, 1) == (4, [1, 2, 3], [8, 7, 5, 6])

    A = [7, 5, 6, 1, 2, 4, 3, 8]
    assert partition(A, 6) == (3, [1, 2], [6, 7, 5, 4, 8])

    A = permutation(10).tolist()
    assert quicksort(A, choose_random_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = permutation(10).tolist()
    assert quicksort(A, choose_first_el_for_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = permutation(10).tolist()
    assert quicksort(A, choose_last_el_for_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = [5, 6, 1, 2, 4, 3]
    print quicksort(A, choose_first_el_for_pivot) # 11

    A = [5, 6, 1, 2, 4, 3]
    print quicksort(A, choose_last_el_for_pivot) # 9

    A = [2, 3, 6, 4, 1, 5]
    print quicksort(A, choose_first_el_for_pivot) # 10

    A = [2, 3, 6, 4, 1, 5]
    print quicksort(A, choose_last_el_for_pivot) # 11


    print choose_median_pivot([1, 2, 3, 4, 5])
    print choose_median_pivot([4, 5, 6, 7])
    print choose_median_pivot([8, 2, 4, 5, 7, 1])

    # B = permutation(1000000).tolist()
    # B = [x for x in range(10000, 0, -1)]

    # start_time = time.time()
    # quicksort(B, choose_random_pivot)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # B = [x for x in range(10000, 0, -1)]

    # start_time = time.time()
    # quicksort(B, choose_first_el_for_pivot)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # B = [x for x in range(10000, 0, -1)]

    # start_time = time.time()
    # quicksort(B, choose_last_el_for_pivot)
    # print("--- %s seconds ---" % (time.time() - start_time))

    text_file = open("../data/quick_sort.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    A = [int(line) for line in lines]
    print len(A)
    print quicksort(A, choose_median_pivot)[0]


    print "All good."