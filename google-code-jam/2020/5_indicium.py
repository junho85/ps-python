from collections import deque

def solve(n, k):
    m = []
    for i in range(n):
        row = [j % n + 1 for j in range(i, i + n)]
        m.append(row)

    if n == 2 and k != 2:
        return "IMPOSSIBLE"
    if n == 3 and k != 6:
        return "IMPOSSIBLE"

    if k < n or k > n*n:
        return "IMPOSSIBLE"

    result = ""
    for row in m:
        result += " ".join(str(x) for x in row) + "\n"
        # print(" ".join(row))
    return "POSSIBLE\n" + result

tc = int(input())

for t in range(1, tc+1):
    (n, k) = [int(i) for i in input().split()]
    ans = solve(n, k)
    print("Case #" + str(t) + ": " + ans)
