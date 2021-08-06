




def DFS(L,s):
    global cnt
    if L == k:
        if (sum(res) % m) == 0:
            cnt = cnt + 1
    else:
        for i in range(s,n):
            res[L] = num[i]
            DFS(L+1,i+1)





n,k = map(int,input().split())
num = list(map(int,input().split()))
m = int(input())
num.sort()
cnt = 0
res = [0]*(n+1)
DFS(0,0)
print(cnt)