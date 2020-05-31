from math import gcd
from functools import reduce

print(reduce(gcd, [2, 4, 8], 2))
print(reduce(gcd, [16, 32, 96], 32))

print(reduce(lambda x, y: x * y, [1, 2]))  # 2
print(reduce(lambda x, y: x * y, [1, 2, 3]))  # 6
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 24


# assert(gcd_array([16, 32, 96]) == 16)