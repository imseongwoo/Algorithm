n = int(input())
graph = []
row = []
col = []
dia = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    row.append(sum(graph[i]))

for b in range(n):
    sum = 0
    for a in range(n):
        sum += graph[a][b]
    col.append(sum)

ref = 0
for i in range(n):
    for j in range(n):
        if i==j:
            ref += graph[i][j]
dia.append(ref)

ans = 0
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            ans += graph[i][j]
dia.append(ans)

print(max(max(row),max(col),max(dia)))

# 답
n = int(input())
a=[list(map(int,input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)