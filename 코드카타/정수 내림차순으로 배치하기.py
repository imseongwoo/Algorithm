def solution(n):
    answer = []
    n = str(n)
    for a in n:
        answer.append(a)
    answer.sort(reverse=True)
    new = ''.join(answer)
    return int(new)

solution(118372)