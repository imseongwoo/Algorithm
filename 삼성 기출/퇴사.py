def dfs(l, arr, maxval):
    global max_cost
    if l >= n+1:
        if maxval > max_cost:
            max_cost = maxval
        return
    else:
        if l + arr[l][0] <= n+1:
            dfs(l + arr[l][0], arr, maxval + arr[l][1])
        dfs(l+1, arr, maxval)


n = int(input())
arr = []
max_cost = -1
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.insert(0,(0,0))
dfs(1, arr, 0)
print(max_cost)
