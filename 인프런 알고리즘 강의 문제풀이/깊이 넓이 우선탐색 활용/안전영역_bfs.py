from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]              # 상하좌우 방향 벡터
dy = [0, 1, 0, -1]

res = []
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

maxnum = -1

for a in range(n):          # 최대값 찾기
    for b in range(n):
        if arr[a][b] > maxnum:
            maxnum = arr[a][b]



for a in range(maxnum):     # 모든 높이에 대해서 반복
    height = a              # 비가 안오는 경우도 고려
    q = deque()
    arr2 = deepcopy(arr)       # 2차원 리스트 복사
    cnt = 0
    for i in range(n):          # 리스트의 모든 항목에 대해서 반복
        for j in range(n):
            if arr2[i][j] > height:     # 안전한 위치면 실행
                q.append((i,j))
                arr2[i][j] = 0          # 방문 체크

                while q:
                    tmp = q.popleft()
                    for x in range(4):
                        tx = tmp[0] + dx[x]
                        ty = tmp[1] + dy[x]

                        if 0 <= tx < n and 0 <= ty < n and arr2[tx][ty] > height:
                            arr2[tx][ty] = 0
                            q.append((tx,ty))
                cnt += 1
    res.append(cnt)

print(max(res))