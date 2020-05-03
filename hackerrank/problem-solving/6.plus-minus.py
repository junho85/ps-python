#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    len_arr = len(arr)
    n = 0
    z = 0
    p = 0

    for num in arr:
        if num < 0:
            n += 1
        elif num == 0:
            z += 1
        else:
            p += 1

    print(p / len_arr)
    print(n / len_arr)
    print(z / len_arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
