# https://programmers.co.kr/skill_checks/66037?challenge_id=898
def solution(s):
    length = len(s)
    if length == 0:
        return s

    center = int(length / 2)
    if length % 2 == 0:
        return s[center-1:center + 1]
    else:
        return s[center]

print(solution("a"))
print(solution("abcde"))
print(solution("qwer"))