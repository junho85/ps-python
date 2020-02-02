class Test:
    a = 10
def get(self):
    print(self.a)
t1 = Test()
setattr(t1, 'get', get)
# t1.get()
t2 = Test
setattr(t2, 'get', get)
t2().get()