# 구간합 풀이
n,m = map(int,input().split())
a = list(map(int,input().split()))

arr = []
sum = 0
for i in a:
    sum += i
    arr.append(sum)

count = 0
for i in range(n):
    for j in range(n):
        if i < j:
            if arr[j] - arr[i] == m:
                count += 1
        elif i == j:
            if arr[i] == m:
                count += 1
print(count)

# 투포인터 풀이

n,m = map(int,input().split())
a = list(map(int,input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot==m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot-=a[lt]
        lt+=1
