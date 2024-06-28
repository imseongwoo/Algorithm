def dfs(n, sm):
    global ans

    if n == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, sm + arr[n][j])
            v[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = N * 10
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    dfs(0, 0)

    print(f'#{test_case} {ans}')
