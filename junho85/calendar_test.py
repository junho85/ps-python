from datetime import date, timedelta

sum = 0
step = 3000
m = step
d = date(year=2018, month=9, day=20)
for i in range(26):
    sum += m
    print(i+1, d, m)
    d += timedelta(days=7)
    m += step

print(sum)