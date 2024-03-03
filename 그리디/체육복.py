def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for a in lost[:]:       # 리스트의 복사본
        if a in reserve:
            lost.remove(a)
            reserve.remove(a)

    answer = n - len(lost)
    res = {}
    for a in reserve:
        res[a] = False

    for a in lost:
        if a - 1 in reserve and res[a - 1] == False:
            answer += 1
            res[a-1] = True
            continue
        if a + 1 in reserve and res[a + 1] == False:
            answer += 1
            res[a+1] = True
            continue

    return answer


print(solution(5, [2, 4], [2]))
