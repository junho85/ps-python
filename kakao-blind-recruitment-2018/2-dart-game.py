import re

def multiple(str):
    if str == 'S':
        return 1
    elif str == 'D':
        return 2
    else: # T
        return 3

def s(a, b):
    return pow(int(a), multiple(b))

def is_star(str):
    if len(str) == 1:
        return False
    elif str[1] == '*':
        return True
    else:
        return False

def is_acha(str):
    if len(str) == 1:
        return False
    elif str[1] == '#':
        return True
    else:
        return False

def solution(dartResult):
    r = re.compile("([0-9]+)([A-Z*#]+)([0-9]+)([A-Z*#]+)([0-9]+)([A-Z*#]+)")
    m = r.match(dartResult)

    score1 = s(m.group(1), m.group(2)[0])
    if is_acha(m.group(2)):
        score1 *= -1
    elif is_star(m.group(2)):
        score1 *= 2


    score2 = s(m.group(3), m.group(4)[0])
    if is_acha(m.group(4)):
        score2 *= -1
    elif is_star(m.group(4)):
        score1 *= 2
        score2 *= 2


    score3 = s(m.group(5), m.group(6)[0])
    if is_acha(m.group(6)):
        score3 *= -1
    elif is_star(m.group(6)):
        score2 *= 2
        score3 *= 2


    answer = score1 + score2 + score3
    return answer


# test
assert(solution('1S2D*3T') == 37)
assert(solution('1D2S#10S') == 9)
assert(solution('1D2S3T*') == 59)
