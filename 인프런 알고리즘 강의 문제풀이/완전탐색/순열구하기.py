# # def DFS(l):
# #     if l==m:
# #         for i in range(11):
# #             if res[i]==1:
# #                 print(i,end=' ')
# #         print()
# #     else:
# #         for i in range(1,n+1):
# #             if ch[i] == 0:
# #                 ch[i]=1
# #                 res[l] = i
# #                 DFS(l+1)
# #
# #
# #
# # n,m = map(int,input().split())
# # res = [0] * m
# # ch = [0] * (n+1)
# # DFS(0)
#
#
#
#
#
# import sys
#
# def DFS(L):
#     global cnt
#     if L==m:
#         for i in range(m):
#             print(res[i], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 ch[i]=1
#                 res[L]=i
#                 DFS(L+1)
#                 ch[i]=0
#
# if __name__=="__main__":
#     n, m=map(int, input().split())
#     res=[0]*n
#     ch=[0]*(n+1)
#     cnt=0
#     DFS(0)
#     print(cnt)
#

res = []
res.append(0)
res.append(1)
print(res)