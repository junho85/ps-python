I = input
n = int(I())
m = int(I())
R = range
global d, y, x
d = 1
w = (n + 1) * 4
h = n * 2 + 1
M = [[' '] * w for _ in R(h)]
y, x = h - 1, -1


def p(a): M[y][x] = a


def l(l):
    global d
    if l:
        d -= 1
    else:
        d += 1
    d %= 4
    p('+')


def D(n):
    global y, x
    for _ in R(n):
        if d % 2:
            for _ in R(4):
                if d == 1:
                    x += 1
                else:
                    x -= 1
                p('-')
        else:
            for _ in R(2):
                if d == 0:
                    y -= 1
                else:
                    y += 1
                p('|')


for i in R(n, 0, -1):
    D(i)
    l(1)

D(i)
for i in R(1, n + 2):
    l(0)
    if i == n + 1:
        D(i - 1)
    else:
        D(i)
p('+')
for r in M: print(''.join(r) * m)
