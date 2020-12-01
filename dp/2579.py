
n = int(input())

d = [0]*(n+1)

arr = []
for i in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])

elif n == 2:
    print(arr[0]+arr[1])

elif n == 3:
    print(max(arr[0] + arr[2],arr[1]+arr[2]))

else:
    d[0] = 0
    d[1] = arr[0]
    d[2] = arr[0] + arr[1]
    for i in range(3, n + 1):
        d[i] = max(d[i - 2] + arr[i - 1], d[i - 3] + arr[i - 2] + arr[i - 1])
    print(d[n])


# import sys
# n = int(sys.stdin.readline())
# lis = []
# for i in range(n):
#     k = int(sys.stdin.readline())
#     lis.append(k)
# dp = [0, lis[0], lis[0] + lis[1]]
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 2] + lis[i - 1], dp[i - 3] + lis[i - 1] + lis[i - 2]))
# print(dp[n])

