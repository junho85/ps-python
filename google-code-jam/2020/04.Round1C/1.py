def solve(x, y, m):
    round = 0

    for mm in m:
        round += 1
        if mm == "S":
            y -= 1
        elif mm == "N":
            y += 1
        elif mm == "E":
            x += 1
        else:
            x -= 1

        if abs(x) + abs(y) <= round:
            return round

    return "IMPOSSIBLE"


tc = int(input())

for t in range(1, tc+1):
    (x, y, m) = input().split()
    x = int(x)
    y = int(y)
    ans = solve(x, y, m)
    print("Case #" + str(t) + ": " + str(ans))

