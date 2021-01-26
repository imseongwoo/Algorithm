n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    count = 1
    for j in range(n):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            count += 1
    print(count,end=' ')