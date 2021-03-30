import sys

def solve(lefts, rights):
    answer = None

    # check rights
    if rights:
        longright = max(rights, key=len)
        lenright = len(longright)

        is_wrong = False
        for r in rights:
            if r != longright[lenright-len(r):lenright]:
                is_wrong = True
                break

        if not is_wrong:
            answer = longright

    # check lefts
    if lefts:
        longleft = max(lefts, key=len)
        lenleft = len(longleft)

        is_wrong = False
        for l in lefts:
            if l != longleft[lenleft-len(l):lenleft]:
                is_wrong = True
                break
        if not is_wrong:
            if answer is None:
                answer = longleft
            else:
                answer += longleft

    if answer is None:
        return "*"
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
        else:
            (r, l) = line.split('*')
            if l:
                lefts.append(l)
            if r:
                rights.append(r)

    ans = solve(lefts, rights)
    print("Case #" + str(t) + ": " + ans)

assert(solve(["JAM"], ["CODE"]) == "CODEJAM")