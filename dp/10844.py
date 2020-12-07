import sys

input = sys.stdin.readline
a = int(input())
dp = [[0 for i in range(10)] for j in range(a + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, a + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[a]) % 1000000000)

# 한번 더 풀어봐야함. 2차원 동적계획법 ,dp[i][j]= i 자리수에서 j로 끝나는 수의 개수, 3자리수에서 2로 끝나는 수의 개수는 2자리수에서 1,3 으로 끝나는 개수의 합과 똑같음
