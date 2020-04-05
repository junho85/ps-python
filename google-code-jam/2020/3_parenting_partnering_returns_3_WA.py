def solve(schedules):
    answer = None

    cameron_schedule = None
    jamie_schedule = None

    sorted_schedules = sorted(schedules)
    for i in range(len(sorted_schedules)):
        cur_schedule = sorted_schedules[i]

        # Jamie 먼저
        if i == 0:
            answer = "J"
            jamie_schedule = cur_schedule
            continue

        (cur_start, cur_end) = cur_schedule

        if cameron_schedule:
            (cameron_start, cameron_end) = cameron_schedule
            if cur_start >= cameron_end:
                cameron_schedule = None

        if jamie_schedule:
            (jamie_start, jamie_end) = jamie_schedule
            if cur_start >= jamie_end:
                jamie_schedule = None

        # 둘다 스케쥴 있으면 실패
        if cameron_schedule is not None and jamie_schedule is not None:
            return "IMPOSSIBLE"

        if jamie_schedule is None:
            jamie_schedule = cur_schedule
            answer += "J"
        else:
            cameron_schedule = cur_schedule
            answer += "C"
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
assert (solve([[1, 200], [1, 200]]) == "JC")
assert (solve([[0, 1], [0, 1]]) == "JC")
assert (solve([[0, 100], [50, 200], [100, 300]]) == "JCJ")
assert (solve([[0, 100], [50, 150], [100, 200], [150, 250]]) == "JCJC")
assert (solve([[0, 100], [50, 150], [100, 200], [150, 250], [200, 300]]) == "JCJCJ")
assert (solve([[1, 3], [2, 4], [3, 5]]) == "JCJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302]]) == "JCJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 320]]) == "JCJJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 400], [400, 401]]) == "JCJJJJ")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 410], [400, 401]]) == "JCJJJC")
assert (solve([[100, 300], [200, 400], [300, 301], [301, 302], [310, 410], [400, 401], [401, 402]]) == "JCJJJCC")

assert (solve([[100, 300], [200, 400], [300, 301], [300, 301]]) == "IMPOSSIBLE")
assert (solve([[1, 200], [2, 3], [3, 4], [4, 205], [200, 202], [201, 203]]) == "IMPOSSIBLE")
assert (solve([[0, 1], [0, 1], [0, 1]]) == "IMPOSSIBLE")
assert (solve([[0, 100], [0, 100], [50, 100]]) == "IMPOSSIBLE")
