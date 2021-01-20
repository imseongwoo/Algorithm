l = int(input())
arr = list(map(int,input().split()))
m = int(input())

for _ in range(m):
    arr = sorted(arr)
    arr[0] = arr[0] + 1
    arr[l-1] = arr[l-1] -1

print(max(arr)-min(arr))

# l,m 값이 커질 경우 시간초과 대비
L = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = [0] * 101
maxH = float('-inf')
minH = float('inf')
for x in arr:
    cnt[x] += 1
    if x > maxH: maxH = x
    if x < minH: minH = x

for _ in range(m):
    if cnt[maxH] == 1:
        cnt[maxH] -= 1
        maxH -= 1
        cnt[maxH] += 1
    else:
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1

    if cnt[minH] == 1:
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
    else:
        cnt[minH] -= 1
        cnt[minH + 1] += 1

print(maxH - minH)