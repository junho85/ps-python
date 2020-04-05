import sys
(t, b) = [int(i) for i in input().split()]

for i in range(1, b):
    print(i, flush=True)
    # print("fatal error", file=sys.stderr)
    response = input()
    print("===response:" + str(i) + ":" + response, file=sys.stderr)

sys.exit(99)