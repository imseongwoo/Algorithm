def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])

    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.add(v[0])
                link.add(v[1])      # update로 link.update([v[0], v[1]]) 이렇게 구현해도됨
                answer += v[2]
                break

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])