for t in range(int(input())):
    activities = []
    for n in range(int(input())):
        activity = [int(x) for x in input().split()]
        activities.append([n, activity])

    cend = 0
    jend = 0

    is_impossible = False
    for (n, activity) in sorted(activities, key=lambda x: x[1][0]):
        if cend <= activity[0]:
            cend = activity[1]
            activities[n].append('C')
        elif jend <= activity[0]:
            jend = activity[1]
            activities[n].append('J')
        else:
            is_impossible = True
            break

    print("Case #" + str(t+1) + ": " + (is_impossible and "IMPOSSIBLE" or
                                        "".join([x[2] for x in sorted(activities, key=lambda x: x[0])]
                                        )))

