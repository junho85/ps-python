#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for (i, x) in enumerate(apples):
        apples[i] = x + a

    for (i, x) in enumerate(oranges):
        oranges[i] = x + b

    a_in = 0
    for x in apples:
        if s <= x and x <= t:
            a_in += 1
    print(a_in)

    o_in = 0
    for x in oranges:
        if s <= x <= t:
            o_in += 1
    print(o_in)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
