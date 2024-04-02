def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.add(v[0])
                link.add(v[1])
                answer += v[2]
                break

    return answer


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y: return
    parent[x] = y


def find(parent, x):
    if parent[x] == x: return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def solution(n, costs):
    answer = cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    for i in range(len(costs)):
        if find(parent, costs[i][0]) != find(parent, costs[i][1]):
            union(parent, costs[i][0], costs[i][1])
            answer += costs[i][2]
            cnt += 1
        if cnt == n: break

    return answer