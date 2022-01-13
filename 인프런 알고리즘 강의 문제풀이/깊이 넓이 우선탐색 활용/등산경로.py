dx = [-1, 0, 1, 0]              # 상하좌우 방향 벡터
dy = [0, 1, 0, -1]
def dfs(x,y):
    global count
    if x==xx and y==yy:
        count += 1
    else:
        for a in range(4):
            tx = x + dx[a]
            ty = y + dy[a]
            if  0 <= tx < n and 0 <= ty < n and check[tx][ty] ==0 and arr[tx][ty] > arr[x][y] :
                check[tx][ty] = 1
                dfs(tx,ty)
                check[tx][ty] = 0

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    count = 0
    check = [[0]*n for _ in range(n)]

    x = y = -1
    xx = yy = -1
    minum = 9999
    maxnum = -1
    for a in range(n):
        for b in range(n):
            if arr[a][b] < minum:
                minum = arr[a][b]
                x = a
                y = b
            if arr[a][b] > maxnum:
                maxnum = arr[a][b]
                xx = a
                yy = b


    check[x][y] = 1
    dfs(x,y)
    print(count)