# 내풀이
def DFS(L):
    global cnt
    if L == n:
        cnt += 1

    else:
        for i in range(1, n + 1):
            if graph[L][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0           # 이게 문제였어


n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)

cnt = 0
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b] = 1
ch[1]=1
DFS(1)
print(cnt)


# 답
# import sys
#
# sys.stdin = open("input.txt", "r")
#
#
# def DFS(v):
#     global cnt, path
#     if v == n:
#         cnt += 1
#         for x in path:
#             print(x, end=' ')
#         print()
#     else:
#         for i in range(1, n + 1):
#             if g[v][i] == 1 and ch[i] == 0:
#                 ch[i] = 1
#                 path.append(i)
#                 DFS(i)
#                 path.pop()
#                 ch[i] = 0
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     g = [[0] * (n + 1) for _ in range(n + 1)]
#     ch = [0] * (n + 1)
#     for i in range(m):
#         a, b = map(int, input().split())
#         g[a][b] = 1
#     cnt = 0
#     ch[1] = 1
#     path = list()
#     path.append(1)
#     DFS(1)
#     print(cnt)