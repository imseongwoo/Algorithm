from collections import deque

arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ch = [[0]*7 for _ in range(7)]
dist = [[0]*7 for _ in range(7)]
queue = deque()
queue.append((0,0))

for _ in range(7):
    arr.append(list(map(int,input().split())))

while queue:
    temp = queue.popleft()

    if temp[0] == 6 and temp[1] == 6:
        break

    ch[temp[0]][temp[1]] = 1
    for i in range(4):
        nx = temp[0]+dx[i]
        ny = temp[1]+dy[i]

        if nx<0 or ny<0 or nx>6 or ny>6:
            continue
        elif ch[nx][ny] == 1:
            continue
        elif arr[nx][ny] == 1:
            continue
        else:
            dist[nx][ny] = dist[temp[0]][temp[1]] + 1
            queue.append((nx,ny))

if dist[6][6] == 0:
    print(-1)
else:
    print(dist[6][6])

# 난 성장했다. ㅎ.ㅎ