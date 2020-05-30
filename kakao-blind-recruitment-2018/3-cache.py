from collections import deque

def solution(cacheSize, cities):
    answer = 0

    q = deque(maxlen=cacheSize)

    for item in cities:
        item = item.lower()
        if item in q:
            answer += 1
            q.remove(item)
            q.append(item)
        else:
            answer += 5
            q.append(item)

    return answer

assert(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50)
assert(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21)
assert(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60)
assert(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52)
assert(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
assert(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)