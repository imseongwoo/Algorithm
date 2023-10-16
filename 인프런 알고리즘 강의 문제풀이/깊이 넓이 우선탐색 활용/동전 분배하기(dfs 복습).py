def dfs(level,sumone,sumtwo,sumthree):
    global ans
    if level==n:
        if sumone != sumtwo and sumone != sumthree and sumtwo != sumthree:
            res = max(sumone,sumtwo,sumthree)-min(sumone,sumtwo,sumthree)
            if res < ans:
                ans = res

    else:
        dfs(level+1,sumone+arr[level],sumtwo,sumthree)
        dfs(level+1,sumone,sumtwo+arr[level],sumthree)
        dfs(level+1,sumone,sumtwo,sumthree+arr[level])


n = int(input())
arr = []
ans = 2147586
for _ in range(n):
    arr.append(int(input()))
dfs(0,0,0,0)
print(arr)
print(ans)