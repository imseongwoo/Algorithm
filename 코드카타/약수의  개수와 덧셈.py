
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        temp = check_num(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

def check_num(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

print(solution(13,17))