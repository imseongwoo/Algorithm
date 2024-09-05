n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0], arr[i][0])

for j in range(1, n):
    dp[0][j] = min(dp[0][j - 1], arr[0][j])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), arr[i][j])

print(dp[n - 1][n - 1])
###################################################
import sys

sys.setrecursionlimit(10000)

n = int(input())

UNUSED = -1

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

memo = [
    [UNUSED for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def find_maximin(x, y):
    # 미리 계산된 적이 있는 경우 해당 값을 사용해줍니다.
    if memo[x][y] != UNUSED:
        return memo[x][y]

    # 도착 지점에 도착하면 최대 합을 갱신해줍니다.
    if x == n - 1 and y == n - 1:
        memo[n - 1][n - 1] = grid[n - 1][n - 1]
        return grid[n - 1][n - 1]

    dxs, dys = [1, 0], [0, 1]

    # 가능한 방향에 대해 탐색해줍니다.
    maximin = 0
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if in_range(new_x, new_y):
            maximin = max(maximin,
                          min(find_maximin(new_x, new_y), grid[x][y]))

    # 게산된 값을 memo 배열에 저장해줍니다.
    memo[x][y] = maximin

    return maximin


print(find_maximin(0, 0))