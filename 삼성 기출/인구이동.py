from collections import deque

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    temp = [(si, sj)]
    sum = arr[si][sj]
    while q:
        qi, qj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = qi+di, qj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and L<=abs(arr[qi][qj] - arr[ni][nj])<=R:
                q.append((ni, nj))
                visited[ni][nj] = 1
                temp.append((ni, nj))
                sum += arr[ni][nj]
    if len(temp) > 1:
        for ti, tj in temp:
            arr[ti][tj] = sum//len(temp)
        return 1
    return 0

N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0

while ans <= 2000:
    visited = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag = max(flag,bfs(i,j))
    if flag == 0:
        break
    ans += 1
print(ans)
