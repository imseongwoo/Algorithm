from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [list(map(int,input().split())) for _ in range(7)]
q = deque()
q.append((0,0))
check = [[0]*7 for _ in range(7)]
dist = [[0]*7 for _ in range(7)]
num = 0

while q:        # 큐가 빌 때까지
    temp = q.popleft()
    if temp[0] == 6 and temp[1] == 6:       # 도착지점 도달 시 종료 거리가 1씩 증가하므로 먼저 도달한 경로가 최단경로임.

        break


    for a in range(4):      # 상하좌우 반복
        x = temp[0] + dx[a]
        y = temp[1] + dy[a]

        if x >= 0 and y>=0 and x<=6 and y<=6: # 미로 범위내에서
            if arr[x][y] != 1 and check[x][y] == 0:     # 방문하지 않았고 벽이 아니라면 실행
                q.append((x,y))     # 큐에 append
                check[x][y] = 1     # check
                dist[x][y] = dist[temp[0]][temp[1]] + 1     # 이전경로까지의 거리+1
#문제 조건
if dist[6][6] == 0 :
    print('-1')
else:
    print(dist[6][6])