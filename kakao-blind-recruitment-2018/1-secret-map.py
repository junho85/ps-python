# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
# Python 3.7.0

def solution(n, arr1, arr2):
    answer = []

    for idx, item in enumerate(arr1):
        merged = arr1[idx] | arr2[idx]

        tmp = ""
        for item in format(merged, 'b').zfill(n):
            if item == "1":
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)

    return answer

# test
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))

print(1 | 2) # b01 | b10 = b11 = 3
print(format(9, 'b')) # '1001'

print(format(9, 'b').zfill(8)) # '00001001'
print('abcd'.zfill(8)) # '0000abcd'

for idx, item in enumerate([1, 10, 100, 1000]):
    print(idx, item)