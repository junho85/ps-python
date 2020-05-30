#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for a in ar:
        if a in socks:
            socks[a] += 1
        else:
            socks[a] = 1

    pairs = []
    for x in socks.values():
        pairs.append(int(x/2))

    return sum(pairs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
