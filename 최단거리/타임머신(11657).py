import sys
input = sys.stdin.readline
INF = int(1e9)

graph = []
n,m = map(int,input().split())

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))

def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            graph_cost = graph[j][2]

            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + graph_cost:
                distance[next_node] = distance[cur_node] + graph_cost

                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

