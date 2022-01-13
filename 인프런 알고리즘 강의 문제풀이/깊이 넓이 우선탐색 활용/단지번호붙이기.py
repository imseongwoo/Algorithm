from copy import deepcopy

dx = [-1, 0, 1, 0]              # 상하좌우 방향 벡터
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
arr2  = deepcopy(arr)
check = [[0]*n for _ in range(n)]
res = []



def dfs(x,y):
    global cnt
    cnt += 1
    arr[x][y] = 0

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if 0 <= nx < n and 0 <= ny < n  and arr[nx][ny] == 1:

            dfs(nx,ny)




for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i,j)
            res.append(cnt)
print(len(res))
print(res)