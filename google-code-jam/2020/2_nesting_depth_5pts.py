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
            result += c
    if is_open:
        result += ')'

    return result


tc = int(input())

for t in range(1, tc+1):
    s = input()
    ans = solve(s)
    print("Case #" + str(t) + ": " + ans)

assert (solve("0000") == "0000")
assert (solve("101") == "(1)0(1)")
assert (solve("100") == "(1)00")
assert (solve("0100") == "0(1)00")
assert (solve("0001") == "000(1)")
assert (solve("111000") == "(111)000")
assert (solve("000111") == "000(111)")
assert (solve("1") == "(1)")
assert (solve("") == "")
assert (solve("0") == "0")
