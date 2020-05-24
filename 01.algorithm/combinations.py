from itertools import combinations

comb = list(combinations(["(", "(", ")", ")"], 4))
print(comb)

arr = [1,2,3,4,5,6]
print(list(combinations(arr, 2)))

def comb2(arr):
    result = []
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            result.append((arr[i], j))
    return result

print(comb2(arr))

print(list(combinations(arr, 3)))