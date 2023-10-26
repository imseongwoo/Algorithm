def dfs(x, y):
    global answer
    if x == destx and y == desty:
        answer += 1
    else:
        height = arr[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if ch[nx][ny] != 1:
                    if arr[nx][ny] > height:
                        ch[x][y] = 1
                        dfs(nx, ny)
                        ch[x][y] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ch = [[0] * n for _ in range(n)]
start = 2147589
end = -1
answer = 0

startx= 0
starty = 0
destx = 0
desty = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == min(min(arr)):
            startx = i
            starty = j
        if arr[i][j] == max(max(arr)):
            destx = i
            desty = j
dfs(startx, starty)
print(answer)