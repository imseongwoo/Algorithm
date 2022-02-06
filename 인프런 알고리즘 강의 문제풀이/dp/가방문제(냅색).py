count,weight = map(int,input().split())

dp = [0] * (weight+1)

for i in range(count):
    w,v = map(int,input().split())
    for j in range(w,weight+1):
        dp[j] = max(dp[j],dp[j-w]+v)


print(dp[weight])