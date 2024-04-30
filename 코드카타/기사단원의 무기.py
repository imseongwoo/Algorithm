def solution(number, limit, power):
    answer = 0
    arr = [1]

    for i in range(2,number+1):
        count = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                if j**2 == i:
                    count += 1  # j가 제곱근인 경우, 한 번만 카운트
                else:
                    count += 2
        arr.append(count)

    for a in arr:
        if a > limit:
            answer += power
        else:
            answer += a
    return answer


solution(10,3,2)
