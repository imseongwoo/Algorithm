n = int(input())
arr = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp[0][0] = arr[0][0]

for a in range(n):
    for b in range(n):
        if a == 0 and b == 0:
            continue
        if a == 0:
            dp[a][b] = dp[a][b - 1] + arr[a][b]
        elif b == 0:
            dp[a][b] = dp[a - 1][b] + arr[a][b]
        else:
            dp[a][b] = min(dp[a - 1][b], dp[a][b - 1]) + arr[a][b]
print(dp[n-1][n-1])
#  3 6 11
#  5 8 12
# 11 13 14
