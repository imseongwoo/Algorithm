from collections import deque

dx = [-1, 0, 1, 0]              # 상하좌우 방향 벡터
dy = [0, 1, 0, -1]

def check():
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                return False

m,n = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

q = deque()
dist = [[0]*m for _ in range(n)]

for a in range(n):
    for b in range(m):
        if arr[a][b] == 1:
           q.append((a,b))


while q:
    temp = q.popleft()
    for a in range(4):
        nx = temp[0] + dx[a]
        ny = temp[1] + dy[a]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            dist[nx][ny] = dist[temp[0]][temp[1]] + 1
            q.append((nx,ny))
maxnum = -2
for a in range(n):
    for b in range(m):
        if dist[a][b] > maxnum:
            maxnum = dist[a][b]

if check() == False:
    print('-1')
else:
    print(maxnum)


