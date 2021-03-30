# Google Code Jam Round1A
```
python 1.py < 1.txt
python 2.py < 2.txt
python 3.py < 3.txt
```

## Template
```
def solve(nc, m):
    k = sum(m[i][i] for i in range(nc))
    r = 0
    c = 0
    for i in range(nc):
        if len(set(m[i])) != nc:
            r += 1
        column = [row[i] for row in m]
        if len(set(column)) != nc:
            c += 1

    return str(k) + " " + str(r) + " " + str(c)

tc = int(input())

for t in range(1, tc+1):
    nc = int(input())
    m = []
    for n in range(1, nc+1):
        row = [int(i) for i in input().split()]
        m.append(row)
    ans = solve(nc, m)
    print("Case #" + str(t) + ": " + ans)
```