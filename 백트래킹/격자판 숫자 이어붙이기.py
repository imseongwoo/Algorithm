def dfs(n, num, ci, cj):
    if n == CNT:
        sset.add(num)
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(n + 1, num * 10 + arr[ni][nj], ni, nj)


T = int(input())
for test_case in range(1, T + 1):
    N, CNT = 4, 7
    arr = [list(map(int, input().split())) for _ in range(N)]

    sset = set()
    for si in range(N):
        for sj in range(N):
            dfs(1, arr[si][sj], si, sj)

    print(f'#{test_case} {len(sset)}')