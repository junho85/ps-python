T = int(input())

for idx in range(T):
    N = int(input())
    P = input()
    ans = ""
    for c in P:
        if c == "E":
            ans += "S"
        else:
            ans += "E"
    print("Case #" + str(idx + 1) + ": " + ans)

