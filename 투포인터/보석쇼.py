def solution(gems):
    a = 0
    b = 0
    answer = [0, len(gems) - 1]

    res = set(gems)
    dic = {gems[0]: 1}

    while True:
        if len(dic) < len(res):
            b += 1
            if b == len(gems):
                break
            dic[gems[b]] = dic.get(gems[b], 0) + 1
        else:
            if (b-a+1) < (answer[1]-answer[0]+1):
                answer = [a,b]
            if dic[gems[a]] == 1:
                del dic[gems[a]]
            else:
                dic[gems[a]] -= 1
            a += 1
    answer[0] += 1
    answer[1] += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
