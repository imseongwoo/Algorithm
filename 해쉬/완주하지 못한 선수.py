def solution(participant, completion):
    answer = ''
    participant_dict = {}
    for a in participant:
        participant_dict[a] = participant_dict.get(a,0) + 1

    for a in completion:
        participant_dict[a] -= 1

    for a in participant_dict:
        if participant_dict[a] != 0:
            answer = a

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))