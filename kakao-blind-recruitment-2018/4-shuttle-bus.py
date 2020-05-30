from datetime import timedelta, datetime
from collections import deque

def format(td):
    return str(int(td.seconds / 60 / 60)).zfill(2) + ":" + str(int(td.seconds / 60) % 60).zfill(2)

def str_to_timedelta(str_time):
    (hour, minute) = str_time.split(":")
    return timedelta(hours=int(hour), minutes=int(minute))

def solution(bus_num, bus_term, max_member, crew_timetable):
    bus_time = timedelta(hours=9, minutes=0) # 09:00

    # create all buses
    all_bus = {}
    for i in range(bus_num):
        str_bustime = format(bus_time)
        all_bus[str_bustime] = deque(maxlen=max_member)
        bus_time += timedelta(minutes=bus_term)

    crew_timetable = deque(sorted(crew_timetable))

    bus_time = timedelta(hours=9, minutes=0)  # 09:00
    last_bus_time = bus_time + timedelta(minutes=(bus_num - 1) * bus_term)
    print("last bus time=" + format(last_bus_time))
    for crew_time in crew_timetable:
        str_bustime = format(bus_time)
        print("* current bus time is " + str_bustime)
        print("crew time=" + crew_time)

        bus_q = all_bus[str_bustime]
        if len(bus_q) >= max_member:
            bus_time += timedelta(minutes=bus_term)
            print("changed to next bus " + format(bus_time))
            continue

        # find next bus
        while crew_time > str_bustime:
            bus_time += timedelta(minutes=bus_term)
            if bus_time > last_bus_time:
                # all bus gone
                break
            str_bustime = format(bus_time)

        bus_q = all_bus[str_bustime]
        print("board crew=" + crew_time + "; seat=" + str(len(bus_q) + 1) + "; bus=" + str_bustime)
        bus_q.append(crew_time)

    # find con's bus

    # last bus if full
    if len(all_bus[format(last_bus_time)]) == max_member:
        bus_q = all_bus[format(last_bus_time)]
        print("asdfasdf")
        str_last_crew_time = bus_q[max_member - 1]
        print(str_last_crew_time)
        return format(str_to_timedelta(str_last_crew_time) - timedelta(minutes=1))

    for key, val in sorted(all_bus.items(), reverse=True):
        print("### bus " + key + ";" + str(list(val)))





    return format(bus_time)



# assert(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]) == "09:00")
# assert(solution(2, 10, 2, ["09:10", "09:09", "08:00"]) == "09:09")
assert(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]) == "08:59")
# assert(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]) == "00:00")
# assert(solution(1, 1, 1, ["23:59"]) == "09:00")
# assert(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]) == "18:00")
