tc = int(input())


def solve(list):
    result = 0 # sum of cost
    for i in range(len(list)-1):
        min_pos = list[i::].index(min(list[i::]))
        result += min_pos + 1
        list[i:min_pos+i+1] = reversed(list[i:min_pos+i+1])
    return result


for t in range(1, tc+1):
    int(input()) # ignore
    list = [int(i) for i in input().split()]
    ans = solve(list)
    print("Case #" + str(t) + ": " + str(ans))
