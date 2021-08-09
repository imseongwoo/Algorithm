# 내풀이
def DFS(L):
    global cnt
    if L == n:
        cnt += 1

    else:
        for i in range(1, n + 1):
            if graph[L][i] == 1 and ch[L][i] == 0:
                ch[L][i] = 1
                ch[i][L] = 1
                DFS(i)

            else:
                continue



n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
ch = [[0]*(n+1) for _ in range(n+1)]

cnt = 0
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b] = 1

DFS(1)
print(cnt)
