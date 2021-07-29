# def DFS(v,sum):         # 시간초과 발생
#     global temp
#     if sum > c:
#         return
#     if v == n:
#         if sum >temp:
#             temp = sum
#         # ref.append(sum)
#         return
#
#     else:
#         DFS(v+1,sum+arr[v])
#         DFS(v+1,sum)
#
# if __name__=="__main__":
#     c, n = map(int, input().split())
#     arr = []
#     ref = []
#     temp = 0
#     for _ in range(n):
#         arr.append(int(input()))
#     DFS(0,0)
#     print(temp)
#
# # 답
# import sys
# sys.stdin=open("input.txt", "r")
# def DFS(L, sum, tsum):
#     global result
#     if sum+(total-tsum)<result:
#         return
#     if sum>c:
#         return
#     if L==n:
#         if sum>result:
#             result=sum
#     else:
#         DFS(L+1, sum+a[L], tsum+a[L])
#         DFS(L+1, sum, tsum+a[L])
#
#
# if __name__=="__main__":
#     c, n=map(int, input().split())
#     a=[0]*n
#     result=-2147000000
#     for i in range(n):
#         a[i]=int(input())
#     total=sum(a)
#     DFS(0, 0, 0)
#     print(result)

# 복습

def dfs(v,sum,tsum):
    global temp
    if sum+(total - tsum)<temp:
        return

    if sum>c:
        return
    if v==n:
        if sum > temp:
            temp = sum
    else:
        dfs(v+1,sum+a[v],tsum+a[v])
        dfs(v+1,sum,tsum+a[v])



c,n = map(int,input().split())
a = []
temp = -1
for i in range(n):
    a.append(int(input()))
total = sum(a)
dfs(0,0,0)
print(temp)

























