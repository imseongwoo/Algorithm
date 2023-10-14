def dfs(level, sum):
    if sum > t:
        return



t = int(input())
k = int(input())
value = []
cnt = []

for _ in range(k):
    p,n = map(int,input().split())
    value.append(p)
    cnt.append(n)

dfs(0,0)