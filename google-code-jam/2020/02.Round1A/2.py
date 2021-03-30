from collections import deque

pascal = []
def pascals_triangle(n_rows):
    for n in range(n_rows):
        if n-1 in pascal:
            continue

        row = [1]
        if pascal:
            last_row = pascal[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal.append(row)
    return pascal


def solve(nc):
    visited = {}

    positions = deque()

    for n in range(1, nc + 1):
        visited[(n, n)] = 1
        print(visited)
        positions.append((n, n))

    answers = []
    while len(positions) != 0:
        left = positions.popleft()
        answers.append("%d %d" % (left[0], left[1]))

    return "\n" + "\n".join(answers)

tc = int(input())

for t in range(1, tc+1):
    ans = solve(int(input()))
    print("Case #" + str(t) + ": " + ans)