n,m = map(int,input().split())
arr = []
ans = []
for _ in range(n):
    arr.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        count = 0
        if arr[i][j] == 'B':
            if j % 2 == 0:
                for k in range(i, i + 8):
                    for l in range(j,j+8):
                        if arr[k][l] == 'B' and l % 2 != 0:
                            count += 1
                        elif arr[k][l] == 'W' and l % 2 == 0:
                            count += 1
            else:
                for k in range(i, i + 8):
                    for l in range(j, j + 8):
                        if arr[k][l] == 'B' and l % 2 != 0:
                            count += 1
                        elif arr[k][l] == 'W' and l % 2 == 0:
                            count += 1
            ans.append(count)
        else:
            if j % 2 == 0:
                for k in range(i, i + 8):
                    for l in range(j, j + 8):
                        if arr[k][l] == 'W' and l % 2 != 0:
                            count += 1
                        elif arr[k][l] == 'B' and l % 2 == 0:
                            count += 1
            else:
                for k in range(i, i + 8):
                    for l in range(j, j + 8):
                        if arr[k][l] == 'B' and l % 2 != 0:
                            count += 1
                        elif arr[k][l] == 'W' and l % 2 == 0:
                            count += 1
            ans.append(count)




print(ans)
print(min(ans))