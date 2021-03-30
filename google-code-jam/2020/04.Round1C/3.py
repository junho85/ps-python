from collections import Counter

def solve(sn, dn, s):
    if sn == 1:
        return dn - 1

    counter = Counter(s)
    if counter.most_common()[0][1] >= dn:
        return 0

    min_ans = dn
    for i in range(sn):
        pick = s[i]
        same_n = counter.get(pick)

        for j in range(sn):
            if i != j:
                if s[j] % pick == 0:
                    a = int(s[j] / pick)
                    if a + same_n >= dn:
                        min_ans = min(min_ans, a - 1)
    return min_ans


tc = int(input())

for t in range(1, tc+1):
    (sn, dn) = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]

    ans = solve(sn, dn, s)
    print("Case #" + str(t) + ": " + str(ans))

