def setRanking(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else: return 6


def solution(lottos, win_nums):
    answer = []
    max_count = 0
    min_count = 0
    for a in lottos:
        if a in win_nums:
            max_count += 1
        elif a == 0:
            max_count += 1
            continue

    for a in lottos:
        if a in win_nums:
            min_count += 1
        elif a == 0:
            continue
    print(max_count, min_count)
    answer.append(setRanking(max_count))
    answer.append(setRanking(min_count))

    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])