#!/usr/bin/env python

def read_data():
    data = set()
    text_file = open("../data/2sum.txt", "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines:
        if int(line[:-1]) in data:
            continue
        data.add(int(line[:-1]))
    
    return data


def create_hash_table(data, spread):
    hash_table = {}
    for d in data:
        key = abs(d) / spread
        if key not in hash_table:
            hash_table[key] = []
        hash_table[key].append(d)
    return hash_table


def check_sums_in_interval(data, interval):
    result = set()
    spread = interval[-1]
    hash_table = create_hash_table(data, spread)
    for d in data:
        hash_val = abs(d) / spread
        pair_set = hash_table[hash_val]
        if hash_val - 1 in hash_table:
            pair_set += hash_table[hash_val - 1]
        if hash_val + 1 in hash_table:
            pair_set += hash_table[hash_val + 1]
        for val in pair_set:
            if d == val:
                continue
            if d + val in interval:
                result.add(d + val)
                break
    return len(result)


if __name__ == "__main__":
    data = read_data()
    interval = range(-10000, 10001)

    test_data = set([122, -122, 908, -909, 5, 71, -73, 4, 6])
    test_interval = range(-10, 11)

    result = check_sums_in_interval(test_data, test_interval)
    assert result == 5

    result = check_sums_in_interval(data, interval)
    assert result == 427

    print "All good."   
