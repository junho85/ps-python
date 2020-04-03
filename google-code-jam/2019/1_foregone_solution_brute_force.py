tc = int(input())


def solve(n):
    for i in range(1, n):
        a = i
        b = n - a

        str_a = str(a)
        str_b = str(b)
        if '4' not in str_a and '4' not in str_b:
            return str_a + " " + str_b


for t in range(1, tc+1):
    n = int(input())
    ans = solve(n)
    print("Case #" + str(t) + ": " + ans)

# assert (solve(4) == "3 1")
# assert (solve(940) == "930 10")
# assert (solve(4444) == "3333 1111")
