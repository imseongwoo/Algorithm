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