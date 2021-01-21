# 내 풀이
n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
count = 0

while len(arr)>2:
    if m-arr[0] >= min(arr):
        arr.pop()
        arr.pop(0)
        count += 1
    else:
        arr.pop(0)
        count += 1
if sum(arr) <= m:
    count += 1
print(count)

# 답
from collections import deque

n,limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p=deque(p)
cnt = 0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)