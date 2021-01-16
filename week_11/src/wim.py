#!/usr/bin/env python

def read_data():
    data = []
    text_file = open("../data/mwis.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    for idx, line in enumerate(lines[1:]):
        data.append(int(line))
    return data

if __name__ == "__main__":
    data = read_data()
    mwis = set()

    mwis_list = []
    mwis_list.append(0)
    mwis_list.append(data[0])

    for idx in range(1, len(data)):
        mwis_list.append(max(mwis_list[idx], mwis_list[idx-1] + data[idx]))

    i = len(data)
    while(i >= 1):
        if mwis_list[i-1] >= mwis_list[i-2] + data[i-1]:
            i -= 1
        else:
            mwis.add(i)
            i -=2

    result = []
    vertieces_to_check = [1, 2, 3, 4, 17, 117, 517, 997]
    for vertex in vertieces_to_check:
        if vertex in mwis:
            result.append(1)
        else:
            result.append(0)
    
    assert result == [1, 0, 1, 0, 0, 1, 1, 0]

    print "All good."
