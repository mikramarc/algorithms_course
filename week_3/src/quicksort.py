#!/usr/bin/env python

from random import randint
from numpy.random import permutation
import time
import sys
from math import ceil

sys.setrecursionlimit(50000)

def partition(A):
    pivot = A[0]
    i = 1

    for j in range(1, len(A)):
        if A[j] < pivot:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1

    tmp = A[i-1]
    A[i-1] = A[0]
    A[0] = tmp

    return pivot, A[0:i-1], A[i:]

def choose_random_pivot(A):
    arr_len = len(A)
    return randint(0, arr_len-1)

def choose_first_el_for_pivot(A):
    return 0

def choose_last_el_for_pivot(A):
    arr_len = len(A)
    return arr_len -1

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
    tmp = A[0]
    A[0] = A[pivot_idx]

    A[pivot_idx] = tmp
    (pivot, Ai, Aj) = partition(A)
    result_i = quicksort(Ai, pivot_func)
    result_j = quicksort(Aj, pivot_func)
    return (m-1 + result_i[0] + result_j[0], result_i[1] + [pivot] + result_j[1])


if __name__ == "__main__":
    A = permutation(10).tolist()
    assert quicksort(A, choose_random_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = permutation(10).tolist()
    assert quicksort(A, choose_first_el_for_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = permutation(10).tolist()
    assert quicksort(A, choose_last_el_for_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    A = permutation(10).tolist()
    assert quicksort(A, choose_median_pivot)[1] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    text_file = open("../data/quick_sort.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    A = [int(line) for line in lines]
    assert quicksort(A, choose_first_el_for_pivot)[0] == 162085

    A = [int(line) for line in lines]
    assert quicksort(A, choose_last_el_for_pivot)[0] == 164123

    A = [int(line) for line in lines]
    assert quicksort(A, choose_median_pivot)[0] == 138382

    print "All good."