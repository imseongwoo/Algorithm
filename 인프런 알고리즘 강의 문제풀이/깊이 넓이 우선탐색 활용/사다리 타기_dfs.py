
dx = [0,0,1]              # 상하좌우 방향 벡터
dy = [-1,1,0]

arr = [list(map(int,input().split())) for _ in range(10)]
res = []

def dfs(x,y,temp):
    ch[x][y] = 1

    if x == 9:
        if arr[x][y] == 2:
            print(temp)
        else:
            return
    else:
        if y - 1 >= 0 and arr[x][y - 1] == 1 and ch[x][y - 1] == 0:
            dfs(x, y - 1, temp)
            ch[x][y - 1] = 0
        elif y + 1 < 10 and arr[x][y + 1] == 1 and ch[x][y + 1] == 0:
            dfs(x, y + 1, temp)
            ch[x][y + 1] = 0
        else:
            dfs(x + 1, y, temp)
            ch[x + 1][y] = 0


ch=[[0]*10 for _ in range(10)]
for a in range(10):
    if arr[0][a] == 1:
        dfs(0,a,a)

