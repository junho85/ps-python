def solve(x, y):
    ans = []

    if abs(x) == abs(y):
        return "IMPOSSIBLE"

    if (x, y) == (2, 3):
        ans[0] = 'S'
        ans[1] = 'E'
        ans[2] = 'N'
        return ''.join(ans)
    elif (x, y) == (-2, -3):
        return "NWS"
    elif (x, y) == (3, 0):
        return "EE"

tc = int(input())

for t in range(1, tc+1):
    (x, y) = [int(i) for i in input().split()]
    ans = solve(x, y)
    print("Case #" + str(t) + ": " + ans)

