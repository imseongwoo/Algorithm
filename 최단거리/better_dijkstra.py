import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)          # 무한을 의미하는 값으로 10억을 설정

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))   # 최단거리 테이블이 변경될 때 거리값과 노드값을 우선순위큐에 넣어준다

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])

