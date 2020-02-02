tc = int(input())

for t in range(1, tc+1):
    line = input()

range_number = input()
a, b = range_number.split()

print(int((a + b) / 2))
# read result
result = input()
if result == "TOO_SMALL":
    pass
elif result == "TOO_BIG":
    pass
else: # CORRECT
    pass
