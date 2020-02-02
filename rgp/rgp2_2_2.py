from functools import reduce

a = [1,2,3,4,5]
b = map(lambda x: x*2, a) #2,4,6,8,10
c = filter(lambda x: x<=4, b)
d = reduce(lambda x, y: x ** y, c)
print(d)