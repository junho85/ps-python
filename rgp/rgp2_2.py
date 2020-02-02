def outer():
    x = []
    def inner():
        x.append(None)
        print(len(x))
    return inner

c = outer()
c()
c()
c()