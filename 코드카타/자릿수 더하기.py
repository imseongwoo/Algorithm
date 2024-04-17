def solution(n):
    answer = 0
    n = str(n)
    for a in n:
        answer += int(a)
    return answer
