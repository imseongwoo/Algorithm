# n = int(input())
# arr = list(map(int,input().split()))
# res = []
# check = []
# for a in range(n):
#     count = 0
#     for b in range(n):
#         if arr[a] > arr[b]:
#             if arr[b] in check:
#                 continue
#             else:
#                 count += 1
#                 check.append(arr[b])
#     check.clear()
#
#     res.append(count)
#
# for a in res:
#     print(a,end=" ")

# 시간초과

import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
print(numset)
a = list(numset)
a.sort()
print(a)
numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i
print(numdict)
for i in numbers:
    print(numdict[i], end=' ')