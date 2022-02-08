INF = int(1e9)
n = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

while True:
    a,b = map(int,input().split())

    if a == -1 and b == -1:
        break
    else:
        graph[a][b] = 1
        graph[b][a] = 1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])


for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('무한',end=" ")
        else:
            print(graph[a][b],end=" ")
    print()