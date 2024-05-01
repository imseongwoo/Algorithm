def solution(s):
    answer = 0
    a = 0
    b = 0

    for i in range(len(s)):
        if a == b:
            answer += 1
            x = s[i]
            a=0
            b=0

        if s[i] == x:
            a += 1
        else:
            b += 1

    return answer


print(solution("abracadabra"))

from collections import deque

def solution(s):

    ans = 0

    q = deque(s)
    while q:
        a, b = 1, 0
        x = q.popleft()

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans

def solution(s):
    res = []
    answer = 0
    a = 0

    while a < len(s):
        x = s[a]
        counta = 1
        countb = 0

        if a == (len(s) - 1):
            answer += 1
            break

        for i in range(a + 1, len(s)):
            if s[i] != x:
                countb += 1
            else:
                counta += 1
            if counta == countb:
                answer += 1
                a = i + 1
                break
    return answer


print(solution("abracadabra"))

