def solution(k, score):
    answer = []

    res = []
    for a in score:
        if len(res) < k:
            res.append(a)
        else:
            if a > min(res):
                res.remove(min(res))
                res.append(a)

        res.sort()
        answer.append(res[0])

    return answer
