def solution(x, n):
    answer = []
    if x == 0:
        for _ in range(n):
            answer.append(0)
    if x > 0:
        for i in range(x, x * n + 1, x):
            answer.append(i)
    if x < 0:
        for i in range(x, x * n - 1, x):
            answer.append(i)
    return answer


print(solution(0, 2))
