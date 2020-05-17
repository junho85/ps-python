#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]

    break_best = 0
    break_worst = 0

    for score in scores:
        if score > best:
            best = score
            break_best += 1

        if score < worst:
            worst = score
            break_worst += 1

    return [break_best, break_worst]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
