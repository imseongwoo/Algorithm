import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
  for j in range(i+1,n):
    if a[i]<a[j]:
      dp[j]=max(dp[i]+1,dp[j])
print(max(dp))


#[출처] 11053:가장 긴 증가하는 부분수열|작성자 456