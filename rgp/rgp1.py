def f(x, lst=[]):
    for i in range(x):
        lst.append(i*i)
    print(lst)

f(3)