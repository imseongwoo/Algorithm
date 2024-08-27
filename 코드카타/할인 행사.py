def solution(want, number, discount):
    answer = 0
    for a in range(len(discount)-9):
        new = discount[a:a+10]
        cnt = 0
        for a in range(len(want)):
            if new.count(want[a]) == number[a]:
                cnt += 1
            else:
                break
        if cnt == len(number):
            answer += 1

    return answer
