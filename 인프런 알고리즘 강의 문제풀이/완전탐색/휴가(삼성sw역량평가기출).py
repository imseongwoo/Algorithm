
def DFS(v,sum):
    global maxnum
    if v==n+1:
        if sum > maxnum:
            maxnum = sum
    else:
        if v+pa[v] <= n+1:
            DFS(v+pa[v],sum+pb[v])
        DFS(v+1,sum)

if __name__ == "__main__":
    maxnum = -2147000000
    n = int(input())
    pa = list()
    pb = list()
    for _ in range(n):
        a,b = map(int,input().split())
        pa.append(a)
        pb.append(b)
    pa.insert(0,0)
    pb.insert(0,0)
    DFS(1,0)
    print(maxnum)