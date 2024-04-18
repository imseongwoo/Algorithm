def solution(x):
    x = str(x)
    sum = 0
    for a in x:
        sum += int(a)
    x = int(x)
    if x % sum == 0:
        answer = True
    else: answer = False

    return answer

solution(10)