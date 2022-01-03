
def dfs(l,p):
    global maxnum
    if l == n+1:
        # if l+pa[l-1] == n+1:
        #     maxnum += p + pb[l-1]
        if p > maxnum:
            maxnum = p
    else:
        if l+pa[l-1] <= n+1:
            dfs(l+pa[l-1],p+pb[l-1])
        dfs(l+1,p)



maxnum = -1
n = int(input())
pa = list()
pb = list()
for _ in range(n):
    a,b = map(int,input().split())
    pa.append(a)
    pb.append(b)

0 
dfs(1,0)
print(maxnum)