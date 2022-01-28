n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

d = [0] * (n+1)

for a in range(1,n+1):
    temp = 0
    for b in range(1,a):
        if arr[a] > arr[b]:
            temp = max(temp,d[b])

    d[a] = temp + 1

print(max(d))