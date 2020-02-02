R = range
I = int
P = input
c = I(P())
S = [I(P()) for _ in R(c)]
m = max(S)

M = [[' '] * m for _ in R(m)]


def d(s):
    e = I(s / 2)
    o = I((m - s) / 2)
    for i in R(e+1):
        t = i + o
        l = e - i + o
        z = M[t]
        z[-l - 1] = '*'
        z[l] = '*'
        x=M[-t-1]
        x[-l - 1] = '*'
        x[l] = '*'


for s in S:
    d(s)
for r in M: print(''.join(r))
