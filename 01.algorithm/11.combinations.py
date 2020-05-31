from itertools import combinations

# [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
# (2, 3), (2, 4), (2, 5), (2, 6),
# (3, 4), (3, 5), (3, 6),
# (4, 5), (4, 6),
# (5, 6)]
print(list(combinations([1, 2, 3, 4, 5, 6], 2)))

# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
print(list(combinations([1, 2, 3, 4], 3)))





print(list(combinations([1,2,3], 2)))


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

print("===comb2===")
print(comb2(arr))

def my_combination2(arr):
    result = []
    for i, num1 in enumerate(arr):
        for num2 in arr[i + 1:]:
            result.append((num1, num2))
    return result


print("===my_combination2===")
print(my_combination2(arr))
