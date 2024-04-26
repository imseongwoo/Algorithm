from collections import deque

def solution(food):
    answer = ''
    one = deque()
    two = deque()

    for i in range(len(food)):
        if i == 0:
            continue
        count = int(food[i] / 2)
        for j in range(count):
            one.append(i)
            two.appendleft(i)

    ans = list(one) + [0] + list(two)

    for a in ans:
        answer += str(a)

    return answer

solution([1, 3, 4, 6])
