def solution(triangle):
    height = len(triangle)
    dp = [[0]*(a+1) for a in range(height)]

    for a in dp:
        a.insert(0,0)
        a.append(0)

    dp[0][1] = triangle[0][0]
    for i in range(1, height):
        for j in range(1,i+2):
            dp[i][j] = triangle[i][j-1] + max(dp[i-1][j],dp[i-1][j-1])

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
