def solve(schedules):
    answer = "J"
    last_e = None
    last_e_partner = "J"

    sorted_schedules = sorted(schedules)
    for i in range(1, len(sorted_schedules)):
        prev_e = sorted_schedules[i-1][1]
        (s, e) = sorted_schedules[i]

        if last_e is None:
            last_e = max(prev_e, e)
        else:
            if last_e > prev_e and last_e > e:
                return "IMPOSSIBLE"

        if e > last_e:
            last_e = e
            if last_e_partner == "J":
                last_e_partner = "C"
            else:
                last_e_partner = "J"
            answer += last_e_partner
        else:
            if last_e_partner == "J":
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

