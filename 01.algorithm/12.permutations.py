from itertools import permutations

# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(permutations([1, 2, 3], 2)))

from itertools import permutations

for p in permutations(["A", "C", "F", "J", "M", "N", "R", "T"]):
    print(p)

# ('A', 'C', 'F', 'J', 'M', 'N', 'R', 'T')
# ('A', 'C', 'F', 'J', 'M', 'N', 'T', 'R')
# ('A', 'C', 'F', 'J', 'M', 'R', 'N', 'T')
# ('A', 'C', 'F', 'J', 'M', 'R', 'T', 'N')
# ('A', 'C', 'F', 'J', 'M', 'T', 'N', 'R')
# ...


