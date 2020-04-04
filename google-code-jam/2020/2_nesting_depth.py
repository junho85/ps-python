tc = int(input())

def solve(s):
    result = ""
    is_open = False
    for c in s:
        if c == '0':
            if is_open:
                result += ')'
                is_open = False
            result += c
        else:
            if not is_open:
                result += '('
                is_open = True
                pass
            result += c
    if is_open:
        result += ')'

    return result


for t in range(1, tc+1):
    s = input()
    ans = solve(s)
    print("Case #" + str(t) + ": " + ans)

