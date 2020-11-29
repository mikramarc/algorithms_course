#!/usr/bin/env python

def merge(A, B):
    imax = len(A) - 1
    jmax = len(B) - 1
    i = 0
    j = 0
    inversions = 0
    res = []

    for _ in range(imax + jmax + 2):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
            if i > imax:
                return (inversions, res + B[j:])
        else:
            res.append(B[j])
            inversions += imax + 1 - i
            j += 1
            if j > jmax:
                return (inversions, res + A[i:])

def count_intervions(A):
    if len(A) == 1:
        return (0, A)

    if len(A) == 2:
        if A[0] < A[1]:
            res = (0, A)
        else:
            res = (1, [A[1], A[0]])
        return res
    
    A_0 = A[0: len(A)/2]
    A_1 = A[len(A)/2:]
    inversions = 0

    # left inversions
    res_0 = count_intervions(A_0)
    inversions += res_0[0]
    sorted_A_0 = res_0[1]

    # right inversions
    res_1 = count_intervions(A_1)
    inversions += res_1[0]
    sorted_A_1 = res_1[1]

    # split inversions
    res_merge = merge(sorted_A_0, sorted_A_1)
    inversions += res_merge[0]
    sorted_arr = res_merge[1]

    return (inversions, sorted_arr)

if __name__ == "__main__":
    print "Running tests..."

    A_merge = [1, 2, 5]
    B_merge = [3, 7, 8]

    assert merge(A_merge, B_merge) == (1, [1, 2, 3, 5, 7, 8])

    A_merge = [1, 3, 4]
    B_merge = [2, 7, 8]

    assert merge(A_merge, B_merge) == (2, [1, 2, 3, 4, 7, 8])

    A_merge = [1, 3, 5]
    B_merge = [2, 4, 6]

    assert merge(A_merge, B_merge) == (3, [1, 2, 3, 4, 5, 6])

    A = [1, 3, 2, 4, 5, 6]
    assert count_intervions(A)[0] == 1

    A = [1, 2, 6, 5, 3, 4, 9, 14, 10]
    assert count_intervions(A)[0] == 6

    text_file = open("../data/integer_data.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    A = [int(line) for line in lines]
    assert count_intervions(A)[0] == 2407905288

    print "All good."
