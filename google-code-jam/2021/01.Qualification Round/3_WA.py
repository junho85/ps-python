tc = int(input())


def solve(N, C):
    if C < N - 1:
        return "IMPOSSIBLE"
    if C > (N - 1) * 2:
        return "IMPOSSIBLE"
    if C == (N - 1): # min - sorted
        return " ".join([str(int) for int in list(range(1, N + 1))])
    if C == (N - 1) * 2: # max - reversed
        return " ".join([str(int) for int in reversed(list(range(1, N + 1)))])

    reverse_end_pos = C - (N - 1)
    ls = list(range(1, N + 1))
    ls[0:reverse_end_pos+1] = reversed(ls[0:reverse_end_pos+1])

    return " ".join([str(int) for int in ls])


for t in range(1, tc+1):
    (N, C) = map(int, input().split())
    ans = solve(N, C)
    print("Case #" + str(t) + ": " + str(ans))
