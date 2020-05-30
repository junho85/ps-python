# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
# Python 3.7.0

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        merged = arr1[i] | arr2[i]

        tmp = ""
        for j in range(n):
            if ((merged >> j) & 1) == 1:
                tmp = "#" + tmp
            else:
                tmp = " " + tmp
        answer.append(tmp)

    return answer

# test
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))
