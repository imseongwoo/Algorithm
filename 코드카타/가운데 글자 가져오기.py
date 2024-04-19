def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        temp = len(s) // 2
        answer += s[temp-1]
        answer += s[temp]
    else:
        answer += s[len(s) // 2]
    return answer