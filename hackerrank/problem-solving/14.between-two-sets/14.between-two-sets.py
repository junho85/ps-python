# https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

from math import gcd


# Greatest Common Divisor of list
# 리스트의 최대공약수
def gcd_list(nums):
    gcd_nums = None
    for i in range(len(nums)):
        if i == 0:
            gcd_nums = nums[i]
        else:
            gcd_nums = gcd(gcd_nums, nums[i])
    return gcd_nums


# Least common multiple
# 최소공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


# least common multiple of list
# 리스트의 최소공배수
def lcm_list(nums):
    lcm_nums = None
    for i in range(len(nums)):
        if i == 0:
            lcm_nums = nums[i]
        else:
            lcm_nums = lcm(lcm_nums, nums[i])
    return lcm_nums


def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)

    # a의 공배수들 중 gcd_b 이하
    a_cms = []
    i = 1
    while True:
        temp = lcm_a * i
        if temp > gcd_b:
            break

        a_cms.append(temp)
        i += 1

    answer = 0
    for temp in a_cms:
        is_factor = True
        for bb in b:
            if bb % temp != 0:
                is_factor = False
        if is_factor:
            answer += 1

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(str(total))

    # fptr.write(str(total) + '\n')

    # fptr.close()
