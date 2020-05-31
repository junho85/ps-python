from itertools import product

arr1 = ['a', 'b', 'c']
arr2 = ['d', 'e', 'f']

print(list(product(arr1, arr2)))
# [('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'e'), ('c', 'f')]

print("===product===")
arr1 = ['a', 'b', 'c']
arr2 = ['d', 'e', 'f']
arr3 = ['g', 'h', 'i']

print(list(product()))
print(list(product(arr1)))
print(list(product(arr1, arr2)))
print(list(product(arr1, arr2, arr3)))