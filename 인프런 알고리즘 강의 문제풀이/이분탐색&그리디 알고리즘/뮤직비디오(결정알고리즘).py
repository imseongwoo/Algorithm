# 내가 푼 풀이
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.append(0)
start = 1
end = sum(arr)
ref = []
while start <= end:
    mid = (start+end)//2
    result = 0
    count = 0
    for i in range(n):
        result += arr[i]
        if result + arr[i+1] > mid:
            count += 1
            result = 0
    else:
        count += 1
    if mid >= max(arr) and count <= m:
        ref.append(mid)
        end = mid - 1
    else:
        start = mid + 1

print(min(ref))

#답
def Count(capacity):
    cnt=1
    sum=0
    for x in music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n,m=map(int,input().split())
music=list(map(int,input().split()))
maxx = max(music)
lt = 1
rt = sum(music)
res = 0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt = mid-1
    else:
        lt=mid+1
print(res)