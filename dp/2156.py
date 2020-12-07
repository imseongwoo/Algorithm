n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [0] * (n+1)

d[1] = arr[0]
if n>1:
    d[2] = arr[0] + arr[1]
# d[3] = max(arr[0] + arr[2],arr[1]+arr[2])

for i in range(3,n+1):
    d[i] = max(d[i-2]+arr[i-1],d[i-3]+arr[i-2]+arr[i-1],d[i-1])

print(d[n])