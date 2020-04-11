for t in range(int(input())):
    m = []
    nc = int(input())
    for n in range(nc):
        m.append([int(x) for x in input().split()])

    trace = 0
    rbad = 0
    cbad = 0

    for n in range(nc):
        if len(set(m[n])) != nc:
            rbad += 1

        if len(set([m[x][n] for x in range(nc)])) != nc:
            cbad += 1

        trace += m[n][n]

    print("Case #" + str(t+1) + ": ", trace, rbad, cbad)

