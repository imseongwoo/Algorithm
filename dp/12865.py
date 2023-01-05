import sys

# N, K = map(int, input().split())
# stuff = [[0, 0]]
# knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
#
# for _ in range(N):
#     stuff.append(list(map(int, input().split())))
#
# # 냅색 문제 풀이
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         weight = stuff[i][0]
#         value = stuff[i][1]
#
#         if j < weight:
#             knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
#         else:
#             knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
#
# print(knapsack[N][K])

n,k = map(int,input().split())
dp = [[0]* (k+1) for _ in range(n+1)]
arr = [[0,0]]

for _ in range(n):
    arr.append(list(map(int,input().split())))

for a in range(1,n+1):
    for b in range(1,k+1):
        w = arr[a][0]
        v = arr[a][1]

        if b < w:
            dp[a][b] = dp[a-1][b]
        else:
            dp[a][b] = max(v+dp[a-1][b-w],dp[a-1][b])

print(dp[n][k])