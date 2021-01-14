import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)
res = []
while start <= end:
    mid = (start + end)//2
    result = 0
    for i in arr:
        if i > mid:
            result += i-mid
    if result >= m:
        res.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(max(res))