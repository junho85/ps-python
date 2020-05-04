#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    cn = {}
    for a in ar:
        if a in cn:
            cn[a] += 1
        else:
            cn[a] = 1

    temp = []
    for x in cn.values():
        temp.append(int(x/2))

    return sum(temp)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(result)
