
dx = [-1, 0, 1, 0]              # 상하좌우 방향 벡터
dy = [0, 1, 0, -1]

def dfs(x,y):
    global num      # 가지수 체크
    if x==6 and y==6:       # 도착점 도달하면 +1
        num += 1
    else:
        for a in range(4):   # 상하좌우 반복
            tx = x + dx[a]
            ty = y + dy[a]
            if 0<=tx<=6 and 0<=ty<=6 and check[tx][ty] == 0 and arr[tx][ty] != 1:   # 미로 범위 안에 있고 한번도 가지 않고 지나갈 수 있는 경로라면
                check[tx][ty] = 1   # 체크
                dfs(tx,ty)      # 재귀
                check[tx][ty] = 0       # 돌아갈 때 체크를 해제해줘야 함. 해제하지 않으면 경로가 이어져 있을 경우에 조건문으로 체크가 되지 않음

arr = [list(map(int,input().split())) for _ in range(7)]

check = [[0]*7 for _ in range(7)]

check[0][0] = 1
num = 0
dfs(0,0)
print(num)

