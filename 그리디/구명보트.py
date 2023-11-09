from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people=deque(people)
    arr = deque()
    while True:
        if not people:
            break
        arr.clear()
        arr.append(people.popleft())
        while arr and sum(arr) <= limit and people:
            arr.append(people.popleft())
        if sum(arr) > limit:
            people.appendleft(arr.pop())

        answer += 1
    return answer

print(solution([70, 80, 50],100))


# 틀렸어 :(
# 정답
def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1

    return len(people) - answer
