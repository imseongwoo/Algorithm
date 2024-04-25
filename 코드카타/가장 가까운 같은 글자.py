def solution(s):
    answer = []
    res = {}
    for i in range(len(s)):
        if s[i] in res:
            ans = i-res[s[i]]
            answer.append(ans)
            res[s[i]] += ans
        else:
            res[s[i]] = i
            answer.append(-1)
    print(answer)

    return answer

solution("banana")