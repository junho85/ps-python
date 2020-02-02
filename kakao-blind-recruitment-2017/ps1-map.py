def solution(n, arr1, arr2):
    answer = []

    for idx in range(n):
        result_arr = arr1[idx] | arr2[idx]

        # answer.append(bin(result_arr)[2:].zfill(n).replace('1', '#').replace('0', ' '))
        answer.append(format(result_arr, 'b').zfill(n).replace('1', '#').replace('0', ' '))

    return answer


print(bin(5))
print(bin(5)[2:])
print(format(5, 'b'))

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))