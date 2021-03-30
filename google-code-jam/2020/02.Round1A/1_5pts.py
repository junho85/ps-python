import sys

def solve(nc, lefts, rights):
    answer = "*"

    # check lefts
    if lefts:
        longleft = max(lefts, key=len)
        lenleft = len(longleft)

        for l in lefts:
            if l != longleft[lenleft-len(l):lenleft]:
                return "*"

        answer = longleft

    # check rights
    if rights:
        longright = max(rights, key=len)
        lenright = len(longright)

        for r in rights:
            if r != longright[lenright-len(r):lenright]:
                return "*"

        answer += longright

    return answer


tc = int(input())

for t in range(1, tc+1):
    nc = int(input())

    lefts = [] # *COCONUTS
    rights = [] # COCONUTS*

    for n in range(1, nc+1):
        line = input()
        if line.startswith('*'):
            lefts.append(line[1:])
        elif line.endswith('*'):
            rights.append(line[:-1])
            print("right", line, file=sys.stderr)
        else:
            (l, r) = line.split('*')
            print(l, r, file=sys.stderr)
            if l:
                lefts.append(l)
            if r:
                rights.append(r)

    ans = solve(nc, lefts, rights)
    print("Case #" + str(t) + ": " + ans)