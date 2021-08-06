




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

# 답
import sys

sys.stdin = open("input.txt", "r")


def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)