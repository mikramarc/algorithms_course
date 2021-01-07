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
    for job in jobs:
        data_with_idx_and_score.append([job, float(job[0])/float(job[1])])

    return data_with_idx_and_score

def merge(A, B):
    imax = len(A) - 1
    jmax = len(B) - 1
    i = 0
    j = 0
    res = []

    for _ in range(imax + jmax + 2):
        if A[i][1] == B[j][1]:
            if A[i][0][0] >= B[i][0][0]:
                res.append(A[i])
                i += 1 
            else:
                res.append(B[j])
                j += 1

            if i > imax:
                final_res = res + B[j:]
                break
            if j > jmax:
                final_res = res + A[i:]
                break
        elif A[i][1] > B[j][1]:
            res.append(A[i])
            i += 1
            if i > imax:
                final_res = res + B[j:]
                break
        else:
            res.append(B[j])
            j += 1
            if j > jmax:
                final_res = res + A[i:]
                break

    # happy = False
    # while not happy:
    #     happy = True
    #     for i in range(len(final_res) - 1):
    #         if final_res[i][1] == final_res[i+1][1]:
    #             if final_res[i][0][0] < final_res[i+1][0][0]:
    #                 tmp = final_res[i]
    #                 final_res[i] = final_res[i+1]
    #                 final_res[i+1] = tmp
    #                 happy = False
    #                 break


    return final_res

def sort_by_score(data):
    # data format: [[weight, time], score]

    if len(data) == 1:
        return data
    
    if len(data) == 2:
        result = []
        if data[0][1] == data[1][1]:
            if data[0][0][0] >= data[1][0][0]:
                result = [data[0], data[1]]
            else:
                result = [data[1], data[0]]
        elif data[0][1] > data[1][1]:
            result = [data[0], data[1]]
        else:
            result = [data[1], data[0]]

        return result

    data_0 = data[0: len(data)/2]
    data_1 = data[len(data)/2:]

    data_0_sorted = sort_by_score(data_0)
    data_1_sorted = sort_by_score(data_1)
    return merge(data_0_sorted, data_1_sorted)

def compute_weighted_sum(jobs):
    current_time = 0
    weighted_sum = 0
    for job in jobs:
        current_time += job[0][1]
        weighted_sum += job[0][0] * current_time
    return weighted_sum

if __name__ == "__main__":
    data = read_data()
    preprocessed_data = preprocess_data(data)
    # print preprocessed_data
    # print preprocess_data(data)

    test_data_to_merge_0 = [[[5, 3], 2],
                            [[11, 10], 1]]

    test_data_to_merge_1 = [[[10, 5], 5],
                            [[6, 4], 2]]

    # print merge(test_data_to_merge_0, test_data_to_merge_1)

    test_data_to_merge_0 = [[[5, 3], 2],
                            [[11, 10], 2],
                            [[14, 10], 2],
                            [[8, 10], 2],
                            [[1, 10], 2]]

    test_data_to_merge_1 = [[[10, 5], 5],
                            [[6, 4], 2],
                            [[2, 10], 2],
                            [[13, 10], 2]]

    print merge(test_data_to_merge_0, test_data_to_merge_1)

    test_data = [[[11, 10], 1.1],
                 [[10, 5], 2],
                 [[5, 3], 5/3],
                 [[8, 12], 8/12],
                 [[6, 4], 6/4],
                 [[13, 2], 13/2],
                 [[13, 11], 13/11]]

    test_data_schedule = sort_by_score(test_data)
    print test_data_schedule
    print compute_weighted_sum(test_data_schedule)

    data_schedule = sort_by_score(preprocessed_data)
    print compute_weighted_sum(data_schedule)

