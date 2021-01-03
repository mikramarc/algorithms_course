#!/usr/bin/env python

import re

def read_data():
    data = []
    text_file = open("../data/jobs.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        data.append([int(x) for x in re.split(r' +', line)])

    return data

def preprocess_data(jobs):
    data_with_idx_and_score = []
    for idx, job in enumerate(jobs):
        data_with_idx_and_score.append([idx, job, job[0] - job[1]])

    return data_with_idx_and_score

def merge(A, B):
    imax = len(A) - 1
    jmax = len(B) - 1
    i = 0
    j = 0
    res = []

    for _ in range(imax + jmax + 2):
        if A[i][2] == B[j][2]:
            if A[i][1][0] >= B[i][1][0]:
                res.append(A[i])
                res.append(B[j])
            else:
                res.append(B[j])
                res.append(A[i])
            i += 1
            j += 1

            if i > imax:
                return res + B[j:]
            if j > jmax:
                return res + A[i:]
        elif A[i][2] > B[j][2]:
            res.append(A[i])
            i += 1
            if i > imax:
                return res + B[j:]
        else:
            res.append(B[j])
            j += 1
            if j > jmax:
                return res + A[i:]

def sort_by_score(data):
    # data format: [idx, [weight, time], score]

    if len(data) == 1:
        return data
    
    if len(data) == 2:
        result = []
        if data[0][2] == data[1][2]:
            if data[0][1][0] >= data[1][1][0]:
                result = [data[0], data[1]]
            else:
                result = [data[1], data[0]]
        elif data[0][2] > data[1][2]:
            result = [data[0], data[1]]
        else:
            result = [data[1], data[0]]

        return result

    data_0 = data[0: len(data)/2]
    data_1 = data[len(data)/2:]

    data_0_sorted = sort_by_score(data_0)
    data_1_sorted = sort_by_score(data_1)
    return merge(data_0_sorted, data_1_sorted)


if __name__ == "__main__":
    data = read_data()
    # print preprocess_data(data)

    test_data_to_merge_0 = [[1, [11, 10], 1],
                            [0, [5, 3], 2]]

    test_data_to_merge_1 = [[2, [6, 4], 2],
                            [3, [10, 5], 5]]

    # print merge(test_data_to_merge_0, test_data_to_merge_1)

    test_data = [[0, [11, 10], 1],
                 [1, [10, 5], 5],
                 [2, [5, 3], 2],
                 [3, [8, 12], -4],
                 [4, [6, 4], 2],
                 [5, [13, 2], 11]]

    print sort_by_score(test_data)

