from collections import deque

dx = [1, 0]            # 아래 또는 오른쪽으로 이동
dy = [0, 1]

q = deque()

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

q.append((0,0))
dp[0][0] = arr[0][0]

while q:
    temp = q.popleft()

    for a in range(2):
        tx = temp[0] + dx[a]
        ty = temp[1] + dy[a]

        if 0 <= tx <n and 0 <= ty <n:
            energy = dp[temp[0]][temp[1]] + arr[tx][ty]
            if dp[tx][ty] != 0 :
                dp[tx][ty] = min(dp[tx][ty],energy)
                #q.append((tx,ty))
            else:
                dp[tx][ty] = energy
                q.append((tx,ty))

print(dp[n-1][n-1])