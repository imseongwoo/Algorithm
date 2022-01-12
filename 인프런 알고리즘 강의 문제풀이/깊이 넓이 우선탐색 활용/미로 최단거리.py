from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [list(map(int,input().split())) for _ in range(7)]
q = deque()
q.append((0,0))
check = [[0]*7 for _ in range(7)]
dist = [[0]*7 for _ in range(7)]
num = 0
minum = 9999999

while q:
    temp = q.popleft()
    if temp[0] == 6 and temp[1] == 6:

        break


    for a in range(4):
        x = temp[0] + dx[a]
        y = temp[1] + dy[a]

        if x >= 0 and y>=0 and x<=6 and y<=6:
            if arr[x][y] != 1 and check[x][y] == 0:
                q.append((x,y))
                check[x][y] = 1
                dist[x][y] = dist[temp[0]][temp[1]] + 1

if dist[6][6] == 0 :
    print('-1')
else:
    print(dist[6][6])