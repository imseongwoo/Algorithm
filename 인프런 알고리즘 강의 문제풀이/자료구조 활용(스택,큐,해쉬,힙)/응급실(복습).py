from collections import deque

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr = deque(enumerate(arr))

print(arr)

ans = 0
while True:
    tmp = arr.popleft()

    for a in arr:
        if a[1] > tmp[1]:
            arr.append(tmp)
            break
    else:
        ans += 1
        if tmp[0] == m:
            print(ans)
            break
