import math
import os
import random
import re
import sys

def check_all_string_is_y(str):
    for c in str:
        if 'Y' != c:
            return False

    return True

def maxStreak(m, data):
    max_num = 0
    count = 0
    for row in data:
        if check_all_string_is_y(row):
            count += 1
            max_num = max(max_num, count)
        else:
            count = 0
    return max_num


if __name__ == '__main__':
    assert(maxStreak(2, ["YN", "NN"]) == 0)
    assert(maxStreak(3, ["NYY"]) == 0)
    assert(maxStreak(4, ["YNYY", "YYYY", "YYYY", "YYNY", "NYYN"]) == 2)