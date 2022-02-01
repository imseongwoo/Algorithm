
n = int(input())

arr = []

for _ in range(n):
    a,h,w = map(int,input().split())
    arr.append((a,h,w))
arr.sort(reverse=True)
arr.insert(0,0)

d = [0] * (n+1)


for a in range(1,n+1):
    temp = 0
    for b in range(1,a):
        if arr[a][0] < arr[b][0] and arr[a][2] < arr[b][2]:
            temp = max(temp,d[b])

    d[a] = temp + arr[a][1]

print(max(d))