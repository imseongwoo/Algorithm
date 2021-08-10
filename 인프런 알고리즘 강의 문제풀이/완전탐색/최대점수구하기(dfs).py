def DFS(v,sum,t):
    global maxnum
    if time >m:
        return
    if v==n:
        # 최대점수구하기
        # sum = sum - graph[v-1][0]
        # t = t - graph[v-1][1]
        if sum > maxnum:
            maxnum = sum

    else:
        DFS(v+1,sum+graph[v][0],t+graph[v][1])
        DFS(v+1,sum,t)


maxnum = -2147000000
n,m = map(int,input().split())
graph = [0]*n
ch = [0]*n
for i in range(n):
    score,time = map(int,input().split())
    graph[i] = (score,time)

DFS(0,0,0)
print(maxnum)
print(graph)