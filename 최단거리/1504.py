import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())
# distance = [INF] * (n+1)

graph = [[] for i in range(n+1)]


for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

vone,vtwo = map(int,input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance
one = dijkstra(1)
tovone = dijkstra(vone)
tovtwo = dijkstra(vtwo)

answer = min(one[vone] + tovone[vtwo] + tovtwo[n],one[vtwo] + tovtwo[vone] + tovone[n])

if answer >= INF:
    print(-1)
else:
    print(answer)


