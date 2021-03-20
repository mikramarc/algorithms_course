#!/usr/bin/env python

import re
from math import floor, log
from random import getrandbits, uniform


def read_data(filename):
    data = []
    text_file = open("../data/{}".format(filename), "r")
    lines = text_file.readlines()
    text_file.close()

    for line in lines[1:]:
        data.append([int(x) for x in re.split(r' +', line[:-1])])

    return (int(lines[0]), data)


class TwoSat(object):
    def __init__(self, n, conditions):
        self.n = n
        self.variables = []
        self._conditions = conditions
        self.conditions_satified = False
        self.first_unsatisfactory_cond = []

        self._init_variables()
        self.check_if_conditions_satisfied()

    def _init_variables(self):
        self.variables = [bool(getrandbits(1)) for _ in range(self.n)]

    def check_if_condition_satisfied(self, condition):
        var_1 = self.variables[abs(condition[0]) - 1]
        if condition[0] < 0:
            var_1 = not var_1
        var_2 = self.variables[abs(condition[1]) - 1]
        if condition[1] < 0:
            var_2 = not var_2
        if not (var_1 or var_2):
            return False
        return True

    def check_if_conditions_satisfied(self):
        for condition in self._conditions:
            if not self.check_if_condition_satisfied(condition):
                self.conditions_satified = False
                self.first_unsatisfactory_cond = condition
                return
        self.conditions_satified = True

    def flip_variable(self, index):
        self.variables[index - 1] = not self.variables[index - 1]


def run_2sat(n, conditions):
    for i in range(int(floor(log(n, 2)))):
        ts = TwoSat(n, conditions)
        for j in range(2*n):
            if ts.conditions_satified:
                return True
            uns_condition = ts.first_unsatisfactory_cond
            ts.flip_variable(abs(uns_condition[int(getrandbits(1))]))
            ts.check_if_conditions_satisfied()
    return False


def reduce_conditions(conditions):
    current_conditions = conditions
    len_current_conditions = len(current_conditions)
    conditions_reduced = True

    while(conditions_reduced):
        result = []
        pos_x = set()
        neg_x = set()

        for condition in current_conditions:
            for v in condition:
                if v > 0:
                    pos_x.add(v)
                else:
                    neg_x.add(v)

        for c in current_conditions:
            if not ((abs(c[0]) in pos_x and -abs(c[0]) in neg_x) and (abs(c[1]) in pos_x and -abs(c[1]) in neg_x)):
                continue
            result.append(c)

        if len(result) == len(current_conditions):
            conditions_reduced = False
        current_conditions = result

    return result


if __name__ == "__main__":
    n, conditions = read_data('2sat6.txt')
    red_c = reduce_conditions(conditions)
    print run_2sat(n, red_c)
