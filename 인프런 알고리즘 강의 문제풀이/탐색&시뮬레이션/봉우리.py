# 내 풀이
n = int(input())
ref = 0
a = [list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*(n+2))
a.insert(n+1,[0]*(n+2))
for i in range(1,n+1):
    a[i].append(0)
    a[i].insert(0,0)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(x, y):
    count = 0
    global ref
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if a[nx][ny] < a[x][y]:
            count += 1
    if count == 4:
        ref += 1


for x in range(1,n+1):
    for y in range(1,n+1):
        check(x,y)
print(ref)

"""답"""
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)