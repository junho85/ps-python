tc = int(input())


def solve(X, Y, arts):
    arts = list(arts)
    result = 0
    for i in range(len(arts)-1):
        left = arts[i]
        right = arts[i+1]

        if left == '?':
            continue
        if right == '?':
            arts[i + 1] = left
            right = left

        if left == 'C' and right == 'J':
            result += X
        elif left == 'J' and right == 'C':
            result += Y

    return result


for t in range(1, tc+1):
    (X, Y, arts) = input().split()
    X = int(X)
    Y = int(Y)

    ans = solve(X, Y, arts)
    print("Case #" + str(t) + ": " + str(ans))
