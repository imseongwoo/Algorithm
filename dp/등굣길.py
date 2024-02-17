
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1

    for a in range(n):
        for b in range(m):
            if ([b+1,a+1] in puddles) or (a==0 and b==0):
                continue
            else:
                dp[a][b] = (dp[a-1][b] + dp[a][b-1]) % 1000000007
    return dp[-1][-1]

print(solution(4,3,[[2,2]]))