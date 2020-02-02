from collections import Counter

def solution(participant, completion):
    participant_dict = {}
    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1

    for c in completion:
        p_count = participant_dict.get(c)
        if p_count == 1:
            del participant_dict[c]
        else:
            participant_dict[c] -= 1

    return list(participant_dict.keys())[0]


assert(solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo")
