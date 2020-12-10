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

# 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수는 가장 긴 증가하는 전깃줄의 개수를 구한뒤 전체 전깃줄 개수에서 빼주면 된다.