from itertools import permutations


tc = int(input())


def reversort(list):
    result = 0 # sum of cost
    for i in range(len(list)-1):
        min_pos = list[i::].index(min(list[i::]))
        result += min_pos + 1
        list[i:min_pos+i+1] = reversed(list[i:min_pos+i+1])
    return result


def solve(N, C):
    if C < N - 1:
        return "IMPOSSIBLE"

    for p in list(permutations(range(1, N + 1))):
        pt = p[:]
        p = list(p)
        if reversort(p) == C:
            return " ".join([str(int) for int in pt])
    return "IMPOSSIBLE"


for t in range(1, tc+1):
    (N, C) = map(int, input().split())
    ans = solve(N, C)
    print("Case #" + str(t) + ": " + str(ans))
