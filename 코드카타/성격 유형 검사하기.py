def solution(survey, choices):
    answer = []
    personality = ["RT", "CF", "JM", "AN"]
    personality_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        if choices[i] > 4:
            personality_dict[survey[i][1]] += (choices[i] - 4)
        elif choices[i] < 4:
            personality_dict[survey[i][0]] += (4 - choices[i])
        else:
            continue

    for a in personality:
        if personality_dict[a[0]] > personality_dict[a[1]]:
            answer.append(a[0])
        elif personality_dict[a[0]] < personality_dict[a[1]]:
            answer.append(a[1])
        else:
            answer.append(a[0])

    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
