k,n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 0
end = max(arr)
ans = []
while start <= end:
    mid = (end+start)//2
    result = 0
    for a in arr:
        if a > mid:
            result += a//mid
    if result >= n:
        ans.append(mid)
        start = mid + 1

    else:
        end = mid-1

print(max(ans))

#답
k,n = map(int,input().split())
line = []
res = 0
largest = 0
def count(len):
    cnt=0
    for x in line:
        cnt += (x//len)
    return cnt

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest=max(largest,tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
