n = int(input())

a = list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(n):
    temp = 0
    for j in range(i):
        if a[j] < a[i]:
            temp = max(temp,dp[j])

    dp[i] = temp + 1

print(max(dp))
