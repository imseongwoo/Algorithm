def solution(n):
    answer = -1
    if n==1:
        return 4
    for i in range(1,n//2):
        if i**2 == n:
            answer = (i+1)**2
            break
    return answer

print(solution(1))