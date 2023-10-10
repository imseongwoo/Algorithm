def dfs(level, price):
    global maxnum
    if level == n+1 :
        if price > maxnum:
            maxnum = price
    else:
        if level + t[level-1] <= n+1:
            dfs(level+t[level-1], price+p[level-1])
        dfs(level+1,price)

maxnum = -1
n = int(input())
t = []
p = []
for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

dfs(1,0)
print(maxnum)