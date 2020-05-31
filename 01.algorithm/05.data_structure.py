mylist = [1, 1, 2, 3, 5]
print(mylist) # [1, 1, 2, 3, 5]

myset = set(mylist)
print(myset) # {1, 2, 3, 5}


mylist.reverse()
print(mylist) # [5, 3, 2, 1, 1]

mylist.sort()
print(mylist) # [1, 1, 2, 3, 5]

print(list(reversed(mylist))) # [5, 3, 2, 1, 1]
print(sorted(mylist)) # [1, 1, 2, 3, 5]

