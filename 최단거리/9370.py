import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


T = int(input())

for i in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    x = []
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    for _ in range(t):
        x.append(int(input()))

    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist,now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
        return distance
    tos = dijkstra(s)
    tog = dijkstra(g)
    toh = dijkstra(h)

    case1 = tos[g] + tog[h]
    case2 = tos[h] + toh[g]
    la = []
    for i in range(t):
        answer1 = case1 + toh[x[i]]
        answer2 = case2 + tog[x[i]]

        if (answer1 < INF and answer1 == tos[x[i]]) or (answer2 < INF and answer2 == tos[x[i]]):
            la .append(x[i])

    la.sort()

    for i in la:
        print(i,end=' ')





