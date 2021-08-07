
n,m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c

for a in range(n):
    for b in range(n):
        print(graph[a][b],end=' ')
    print()