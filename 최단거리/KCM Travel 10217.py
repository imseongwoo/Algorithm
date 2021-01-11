import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

t = int(input())
def dijkstra(start):
    q = deque()
    q.append((0,start,0))
    distance[start][0] = 0
    while q:
        dist,now,money = q.popleft()
        if distance[now][money] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            price = money + i[2]
            if price > m:
                continue
            if cost < distance[i[0]][price]:
                distance[i[0]][price] = cost
                q.append((cost,i[0],price))

for _ in range(t):
    n,m,k = map(int,input().split())
    distance = [[INF]*(m+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int,input().split())
        graph[u].append((v,d,c))
    dijkstra(1)
    if min(distance[n]) != INF:
        print(min(distance[n]))
    else:
        print('Poor KCM')