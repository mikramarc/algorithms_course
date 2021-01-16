#!/usr/bin/env python

def read_data():
    data = []
    text_file = open("../data/huffman.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    for idx, line in enumerate(lines[1:]):
        data.append(int(line))
    return data

if __name__ == "__main__":
    # data = read_data()

    data = [1, 4, 5, 4]

    mwis = []
    mwis.append(0)
    mwis.append(data[0])

    for idx in range(1, len(data)):
        mwis.append(max(mwis[idx], mwis[idx-1] + data[idx]))

    print mwis
