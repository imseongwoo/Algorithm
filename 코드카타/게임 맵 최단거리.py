from collections import deque
from copy import deepcopy

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    n = len(maps)
    m = len(maps[0])

    ch = [[0]*m for _ in range(n)]
    cnt = deepcopy(ch)
    queue = deque()
    queue.append((0,0))

    while queue:
        temp = queue.popleft()

        if temp[0] == n - 1 and temp[1] == m - 1:
            return cnt[temp[0]][temp[1]] + 1

        for i in range(4):
            nx = dx[i] + temp[0]
            ny = dy[i] + temp[1]

            if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] != 0:
                if ch[nx][ny] != 1:
                    queue.append((nx,ny))
                    ch[nx][ny] = 1
                    cnt[nx][ny] = cnt[temp[0]][temp[1]] + 1

    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))