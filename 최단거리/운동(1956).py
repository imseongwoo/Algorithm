import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]

for a in range(1,v+1):
    for b in range(1,v+1):
        if a==b:
            graph[a][b] = 0

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
ref = []
for a in range(1,v+1):
    for b in range(a+1,v+1):
        if graph[a][b] != INF and graph[b][a] != INF:
            ans = graph[a][b] + graph[b][a]
            ref.append(ans)

if ref:
    print(min(ref))
else:
    print(-1)