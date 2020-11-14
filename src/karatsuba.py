#!/usr/bin/env python

import math
from math import ceil

def recursive_multiply(A, B):
    n = len(A)
    m = len(B)    

    if n == 1 and m == 1:
        return A[0] * B[0]
    else:
        if n > 1:
            a = A[0: int(ceil(float(n)/2))]
            b = A[int(ceil(float(n)/2)):]
        else:
            a = [0]
            b = A
        if m > 1:
            c = B[0: int(ceil(float(m)/2))]
            d = B[int(ceil(float(m)/2)):]
        else:
            c = [0]
            d = B

        return 10**(n/2+m/2)*recursive_multiply(a, c) + \
               10**(n/2)*recursive_multiply(a, d) + \
               10**(m/2)*recursive_multiply(b, c) + \
               recursive_multiply(b, d)

A = [1, 2, 3]
B = [4, 5, 6]
assert recursive_multiply(A, B) == 56088

A = [1, 2, 3]
B = [4, 5]
assert recursive_multiply(A, B) == 5535

A = [1, 2]
B = [4, 5]
assert recursive_multiply(A, B) == 540

A = [1, 2, 3, 4, 5]
B = [4, 5]
assert recursive_multiply(A, B) == 555525

A = [5]
B = [1, 2, 3, 4, 5]
assert recursive_multiply(A, B) == 61725

print "All good."
