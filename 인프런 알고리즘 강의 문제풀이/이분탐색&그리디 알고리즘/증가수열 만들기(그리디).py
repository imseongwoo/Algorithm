# 내 풀이
from collections import deque
n=int(input())
arr = list(map(int,input().split()))
arr = deque(arr)
count = 1
res = []
if arr[0] < arr[-1]:
    temp = arr[0]
    arr.popleft()
    res.append('L')
else:
    temp = arr[-1]
    arr.pop()
    res.append('R')

while arr:
    if arr[0] > temp and arr[-1] > temp:
        if arr[0] > arr[-1]:
            count += 1
            temp = arr[-1]
            arr.pop()
            res.append('R')
            continue
        else:
            count+=1
            temp = arr[0]
            arr.popleft()
            res.append('L')
            continue
    elif arr[0] > temp:
        count += 1
        temp = arr[0]
        arr.popleft()
        res.append('L')

    elif arr[-1] > temp:
        count += 1
        temp = arr[-1]
        arr.pop()
        res.append('R')
    else:
        break

print(count)
for a in res:
    print(a,end='')

# 답
n = int(input())
a = list(map(int,input().split()))
lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while lt <= rt:                 # 투포인터
    if a[lt] > last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort()                  # 양 쪽 수가 전부 last 값보다 클 경우 더 작은 수를 택하기 위해서 정렬
    if len(tmp) == 0:
        break
    else:
        res = res+tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)
