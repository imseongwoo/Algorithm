def solution(n):
    answer = 0
    res = []
    while n > 0:
        res.append(n%3)
        n = n // 3

    res.reverse()
    for i in range(len(res)):
        answer += 3**i * res[i]

    return answer


print(solution(125))