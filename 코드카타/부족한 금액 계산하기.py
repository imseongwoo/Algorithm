def solution(price, money, count):
    answer = 0
    temp = price
    for i in range(count):
        answer += price
        price += temp

    if answer < money:
        return 0
    else:
        answer = answer - money
    return answer

solution(3, 20, 4)