#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    most_commons = Counter(arr).most_common()

    max_frequencies = most_commons[0][1]

    answer = 5
    for common in most_commons:
        if common[1] != max_frequencies:
            break
        answer = min(answer, common[0])
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
