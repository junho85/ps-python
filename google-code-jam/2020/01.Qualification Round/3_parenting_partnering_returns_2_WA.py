def solve(schedules):
    answer = None
    in_schedule = None
    in_partner = None
    sorted_schedules = sorted(schedules)
    for i in range(len(sorted_schedules)):
        cur_schedule = sorted_schedules[i]
        if i == 0:
            in_partner = "J"
            answer = "J"
            in_schedule = cur_schedule
            continue
        else:
            #
            if in_schedule[1] > sorted_schedules[i-1][1] and in_schedule[1] > cur_schedule[1]:
                return "IMPOSSIBLE"

            # 이전 스케쥴이 끝났으면 아무나 하면 된다
            if in_schedule[1] <= cur_schedule[0]:
                # 희생양 James
                in_partner = "J"
                answer += "J"
            # 안끝났으면 다른 사람이 한다.
            else:
                if in_partner == "J":
                    answer += "C"
                else:
                    answer += "J"

    return answer


tc = int(input())

for t in range(1, tc+1):
    nc = int(input())
    activity_schedules = []
    for n in range(1, nc+1):
        activity_schedule = [int(i) for i in input().split()]
        activity_schedules.append(activity_schedule)

    ans = solve(activity_schedules)
    print("Case #" + str(t) + ": " + ans)

assert(solve([[360, 480],[420, 540],[600, 660]]) == "JCJ")
assert(solve([[1,2], [2,3], [3,4]]) == "JJJ")