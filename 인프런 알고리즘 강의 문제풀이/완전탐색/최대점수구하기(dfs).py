def DFS(v,sum,t):
    global maxnum
    if t > m:
        return
    if v==n or t>m:
        if sum > maxnum:
            maxnum = sum
        return
    else:
        DFS(v+1,sum+graph[v][0],t+graph[v][1])
        DFS(v+1,sum,t)


maxnum = -2147000000
n,m = map(int,input().split())
graph = [0]*(n+1)
ch = [0]*n
for i in range(n):
    score,time = map(int,input().split())
    graph[i] = (score,time)
DFS(0,0,0)
print(maxnum)

# 답
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__=="__main__":
    n, m=map(int, input().split())
    pv=list()
    pt=list()
    for i in range(n):
        a, b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0, 0, 0)
    print(res)
