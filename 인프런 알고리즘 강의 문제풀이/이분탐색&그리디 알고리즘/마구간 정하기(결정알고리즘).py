def Count(mid):
    cnt = 1
    endpoint = arr[0]
    for i in range(1,n):
        if arr[i]-endpoint >= mid:
            cnt += 1
            endpoint = arr[i]
    return cnt

n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start = 1
end = max(arr)
res = []
while start <= end:
    mid = (start + end)//2
    result = 0
    if Count(mid) >= c:
        start = mid + 1
        res.append(mid)
    else:
        end = mid - 1

print(max(res))
