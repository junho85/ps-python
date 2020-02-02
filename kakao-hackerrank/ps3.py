import math
import os
import random
import re
import sys

import itertools

def findSchedules(workHours, dayHours, pattern):

    questions = 0
    current_work_hours = 0

    for c in pattern:
        if c == '?':
            questions += 1
        else:
            current_work_hours += int(c)

    rest_work_hours = workHours - current_work_hours

    combinations = []
    for item in itertools.combinations_with_replacement(range(dayHours + 1), questions):
        if rest_work_hours == sum(item):
            combinations.append(item)

    # print(combinations)
    result = []
    for combination in combinations:
        permutations = set(list(itertools.permutations(combination)))
        for permutation in permutations:
            permutation_list = list(permutation)
            # make result string
            result_string = ""
            for c in pattern:
                if c == '?':
                    result_string += str(permutation_list.pop(0))
                else:
                    result_string += c
            # append result string
            result.append(result_string)

    # print(result)

    return sorted(result)


if __name__ == '__main__':
    # print(set(list(itertools.permutations([0, 0, 0, 8]))))
    assert(findSchedules(56, 8, "???8???") == ["8888888"])
    assert(findSchedules(3, 2, "??2??00") == ["0020100", "0021000", "0120000", "1020000"])
    assert(findSchedules(8, 2, "??22200") == ["0222200", "1122200", "2022200"])