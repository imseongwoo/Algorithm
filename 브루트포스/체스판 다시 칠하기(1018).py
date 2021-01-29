# n,m = map(int,input().split())
# arr = []
# ans = []
# for _ in range(n):
#     arr.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         count = 0
#
#         if arr[i][j] == 'W':
#             temp = 'B'
#             for x in range(i,i+8):
#                 for y in range(j,j+8):
#                     if arr[x][y] != temp:
#                         temp = arr[x][y]
#                         continue
#                     else:
#                         count += 1
#                         if temp == 'B':
#                             temp = 'W'
#                         else:
#                             temp = 'B'
#                 else:
#                     if arr[x][j] != temp:
#                         if temp == 'B':
#                             temp = 'W'
#                         else:
#                             temp = 'B'
#             else:
#                 ans.append(count)
#         else:
#             temp = 'W'
#             for x in range(i, i + 8):
#                 for y in range(j, j + 8):
#                     if arr[x][y] != temp:
#                         temp = arr[x][y]
#                         continue
#                     else:
#                         count += 1
#
#                         if temp == 'B':
#                             temp = 'W'
#                         else:
#                             temp = 'B'
#                 else:
#                     if arr[x][j] != temp:
#                         if temp == 'B':
#                             temp = 'W'
#                         else:
#                             temp = 'B'
#
#             else:
#                 ans.append(count)
# print(ans)
# print(min(ans))

# 답
N = 8
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
pivot1 = [str1,str2,str1,str2,str1,str2,str1,str2]
pivot2 = [str2,str1,str2,str1,str2,str1,str2,str1]


def solve():
    a,b = [int(x) for x in input().split()]
    arr = []
    for i in range(a):
        arr.append(input())
    rst = float('inf')
    for i in range(a-N+1):
        for j in range(b-N+1):
            count = 0
            for p in range(N):
                for q in range(N):
                    if arr[i+p][j+q] != pivot1[p][q]:
                        count += 1
            rst = min(rst,count)
            count = 0
            for p in range(N):
                for q in range(N):
                    if arr[i + p][j + q] != pivot2[p][q]:
                        count += 1
            rst = min(rst, count)
    print(rst)
solve()

