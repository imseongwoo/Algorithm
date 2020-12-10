import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(int,input().split()))

dpt = [1] * n
dpr = [1] * n
dpsum = [0] * n

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            dpt[j] = max(dpt[i] + 1, dpt[j])

arr.reverse()

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            dpr[j] = max(dpr[i] + 1, dpr[j])
dpr.reverse()
for i in range(n):
    dpsum[i] = dpt[i] + dpr[i]

print(max(dpsum)-1)

# 순방향으로 증가하는 수열의 개수를 dp 로 구한뒤 역방향으로 증가하는 수열의 개수를 더해준다