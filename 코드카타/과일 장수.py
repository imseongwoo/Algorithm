def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i + m]

        if len(tmp) == m:
            answer += (min(tmp) * m)

    return answer

solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
