dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y):
    global num
    if x==6 and y==6:
        num += 1
    else:
        for a in range(4):
            tx = x + dx[a]
            ty = y + dy[a]
            if 0<=tx<=6 and 0<=ty<=6 and check[tx][ty] == 0 and arr[tx][ty] != 1:
                check[tx][ty] = 1
                dfs(tx,ty)
                check[tx][ty] = 0

arr = [list(map(int,input().split())) for _ in range(7)]

check = [[0]*7 for _ in range(7)]
check[0][0] = 1
num = 0
dfs(0,0)
print(num)
