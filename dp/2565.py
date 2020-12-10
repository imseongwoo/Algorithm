n = int(input())
d = [0] * 501
arr = [0]*501
for i in range(n):
    a,b = map(int,input().split())
    arr[a] =  b
    d[a] = 1

for i in range(1,500):
  for j in range(i+1,500):
    if arr[i]<arr[j]:
      d[j]=max(d[i]+1,d[j])

print(n-max(d))