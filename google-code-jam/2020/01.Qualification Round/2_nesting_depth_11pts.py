def solve(s):
    result = ""

    for i in range(len(s)):
        c = int(s[i])

        left = c
        right = c

        if i != 0:
            prev_c = int(s[i-1])
            left -= prev_c
        if i != len(s)-1:
            next_c = int(s[i+1])
            right -= next_c

        result += "(" * left
        result += str(c)
        result += ")" * right

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
assert (solve("4") == "((((4))))")
assert (solve("021") == "0((2)1)")
