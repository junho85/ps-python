def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))