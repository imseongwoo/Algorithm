# n,m = map(int,input().split())
#
# dp = [0] * (m+1)
#
# for i in range(n):
#     s,t = map(int,input().split())
#     for j in range(t,m+1):
#
#         if j < 2*t:
#             dp[j] = max(dp[j], dp[j-t]+s)
#         else:
#             dp[j] = max(dp[j], dp[])
# print(dp[m])


if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1);
    for i in range(n):
        ps, pt=map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j]=max(dy[j], dy[j-pt]+ps)
    print(dy[m])
