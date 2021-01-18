n = int(input())

a = list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(n):      # 수열을 차례대로
    temp = 0
    for j in range(i):  # 해당하는 수열까지 처음부터 확인
        if a[j] < a[i]: # 해당하는 수열의 이전까지의 수들 중 작을 경우
            temp = max(temp,dp[j])  # 작은 경우에 해당하는 dp값과 temp 값을 비교하여 큰 값을 temp에 대입,
            # temp에는 a[i]보다 작은 값들 중 dp 값이 가장 큰 값이 들어가있음.

    dp[i] = temp + 1    # 반복문이 끝나면 temp 값에 +1

print(max(dp))
