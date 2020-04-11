def solve(schedules):
    answer = ""
    day_min = [0] * (24 * 60)
    who = "J"

    for i, schedule in enumerate(sorted(schedules)):
        is_duplicate = False
        # fill day_min
        (start, end) = schedule
        for min in range(start, end):
            day_min[min] += 1
            if day_min[min] > 2:
                return "IMPOSSIBLE"
            if day_min[min] == 2:
                is_duplicate = True

        if i == 0:
            answer += who
            continue

        if is_duplicate:
            # 일정이 겹쳤을 떄는 다른사람으로
            if who == "J":
                answer += "C"
            else:
                answer += "J"

            # 겹쳤는데 기존거 보다 뒤까지 일하는 경우 현재 작업자 교체
            if day_min[end-1] == 1:
                if who == "J":
                    who = "C"
                else:
                    who = "J"
        else:
            # 겹치는 사람이 없었다면 Jamie가 일한다.
            answer += "J"


    return answer


tc = int(input())

for t in range(1, tc + 1):
    nc = int(input())
    activity_schedules = []
    for n in range(1, nc + 1):
        activity_schedule = [int(i) for i in input().split()]
        activity_schedules.append(activity_schedule)

    ans = solve(activity_schedules)
    print("Case #" + str(t) + ": " + ans)

assert (solve([[360, 480], [420, 540], [600, 660]]) == "JCJ")
assert (solve([[0, 1440], [1, 3], [2, 4]]) == "IMPOSSIBLE")
assert (solve([[1, 2], [2, 3], [3, 4]]) == "JJJ")
assert (solve([[1, 200], [2, 3], [3, 4]]) == "JCC")
assert (solve([[5, 6], [1, 2], [3, 4]]) == "JJJ")

assert (solve([[1, 200], [2, 3], [3, 4], [4, 5]]) == "JCCC")
assert (solve([[1, 200], [2, 3], [3, 4], [4, 5], [10, 20]]) == "JCCCC")
assert (solve([[1, 200], [2, 3], [3, 4], [4, 5], [200, 201]]) == "JCCCJ")
assert (solve([[1, 200], [2, 3], [3, 4], [4, 205], [200, 201], [201, 202]]) == "JCCCJJ")

#                  J       C       C        C          J          J           J            C           C
assert (solve([[1, 200], [2, 3], [3, 4], [4, 300], [200, 201], [201, 202], [202, 400], [301, 303], [303, 304]]) == "JCCCJJJCC")

assert (solve([[1, 200], [1, 200]]) == "JC")
assert (solve([[0, 1], [0, 1]]) == "JC")
assert (solve([[0, 100], [100, 101], [100, 101]]) == "JJC")
assert (solve([[0, 100], [50, 200], [100, 300]]) == "JCJ")
assert (solve([[0, 100], [50, 150], [100, 200], [150, 250]]) == "JCJC")
assert (solve([[0, 100], [50, 150], [100, 200], [150, 250], [200, 300]]) == "JCJCJ")
assert (solve([[1, 3], [2, 4], [3, 5]]) == "JCJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302]]) == "JCJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 320]]) == "JCJJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 400], [400, 401]]) == "JCJJJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 410], [400, 401]]) == "JCJJJC")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 410], [400, 401], [401, 402]]) == "JCJJJCC")

assert (solve([[0, 100], [100, 101], [100, 101], [100, 101]]) == "IMPOSSIBLE")
assert (solve([[100, 300], [200, 400], [300, 301], [300, 301]]) == "IMPOSSIBLE")
assert (solve([[1, 200], [2, 3], [3, 4], [4, 205], [200, 202], [201, 203]]) == "IMPOSSIBLE")
assert (solve([[0, 1], [0, 1], [0, 1]]) == "IMPOSSIBLE")
assert (solve([[0, 100], [0, 100], [50, 100]]) == "IMPOSSIBLE")
