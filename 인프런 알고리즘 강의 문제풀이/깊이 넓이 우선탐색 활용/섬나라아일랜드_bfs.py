from collections import deque

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

q = deque()

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i,j))
            arr[i][j] = 0
            num = 1
            while q:
                temp = q.popleft()
                for a in range(8):
                    tx = temp[0] + dx[a]
                    ty = temp[1] + dy[a]

                    if 0 <= tx < n and 0 <= ty < n and arr[tx][ty] == 1:
                        arr[tx][ty] = 0
                        q.append((tx,ty))
                        num += 1
            res.append(num)

print(len(res))

