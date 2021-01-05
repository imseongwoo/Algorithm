# n = int(input())
# graph = [list(map(int,input().split())) for _ in range(n)]
#
# m = int(input())
# for i in range(m):
#     rotate = []
#     a,b,c = map(int,input().split())
#     if b == 0:
#         for j in range(c):
#             rotate.append(graph[a-1][j])
#         del graph[a-1][0:c]
#         for rot in rotate:
#             graph[a-1].append(rot)
#     else:
#         for j in range(n-c):
#             rotate.append(graph[a - 1][j])
#         del graph[a - 1][0:n-c]
#         for rot in rotate:
#             graph[a - 1].append(rot)
#
# start = 0
# end = n-1
# ans = 0
# for i in range(n):
#     for j in range(start,end+1):
#        ans += graph[i][j]
#     if i < n//2:
#         start += 1
#         end -= 1
#     else:
#         start -= 1
#         end += 1
# print(ans)


# 정답

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())  # 맨 뒤 수를 빼서 앞으로 insert = 오른쪽으로 회전

start = 0
end = n-1
ans = 0
for i in range(n):
    for j in range(start,end+1):
       ans += a[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(ans)