#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    answer = 0
    for i in range(len(ar)):
        for j in ar[i+1:]:
            print(ar[i], "+", j, "=", ar[i] + j)
            if (ar[i] + j) % k == 0:
                answer += 1
    return answer



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
