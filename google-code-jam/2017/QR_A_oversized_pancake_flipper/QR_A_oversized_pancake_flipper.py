f = open("A-small-practice.in", "r")
T = f.readline() # skip first line

def solve(pancake, size):
    pancake_list = list(pancake)
    result = 0

    for idx, c in enumerate(pancake_list):
        print(pancake_list)
        if c == '-':
            # flip
            for j in range(idx, idx + size):
                if pancake_list[j] == '-':
                    pancake_list[j] = '+'
                else:
                    pancake_list[j] = '-'

            result += 1

        else: # '+'
            pass

    return result

# n = solve("----------", 2)
# print(n)


for i, x in enumerate(f):
    pancake, size = x.strip().split(" ")
    print(pancake, size)
    n = solve(pancake, size)

    if n == -1:
        print("IMPOSSIBLE")
    else:
        print("Case #%d: %d" % (i+1, n))

f.close()

