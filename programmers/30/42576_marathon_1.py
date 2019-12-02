def solution(participant, completion):
    for c in completion:
        participant.remove(c)

    answer = participant[0]
    return answer


assert(solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo")
