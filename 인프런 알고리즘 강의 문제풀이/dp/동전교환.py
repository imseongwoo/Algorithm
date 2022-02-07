n = int(input())
money = list(map(int,input().split()))
m = int(input())

dp = [999] * (m+1)
dp.insert(0,0)
for i in range(n):
    for j in range(i,m+1):
        dp[j] = min(dp[j-money[i]]+1,dp[j])


print(dp[m])