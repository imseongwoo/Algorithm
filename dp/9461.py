T = int(input())
arr = []
d = [-1] * 101
for i in range(T):
    n = int(input())
    d[1] = 1
    d[2] = 1
    d[3] = 1

    for j in range(4,n+1):
        d[j] = d[j-2] + d[j-3]

    arr.append(d[n])

for i in range(len(arr)):
    print(arr[i])