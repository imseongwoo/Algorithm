# 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def DFS(L):
    if L==m:
        for i in range(m):
            print(res[i],end=' ')

        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i] = 1
                res[L] = i
                # if all(a != 0 for a in res):
                #     for a in res:
                #
                DFS(L+1)
                ch[i] = 0

if __name__=="__main__":
    n,m = list(map(int,input().split()))
    res = [0]*m
    ch = [0] * (n+1)
    DFS(0)

# 답

import sys

sys.stdin = open("input.txt", "r")


def DFS(L, s):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)


n, m = map(int, input().split())
res = [0] * (n + 1)
cnt = 0
DFS(0, 1)
print(cnt)