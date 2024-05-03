def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    stk = []
    for a in ingredient:
        stk.append(a)
        if stk[-4:] == hamburger:
            answer += 1
            for _ in range(4):
                stk.pop()

    return answer


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
