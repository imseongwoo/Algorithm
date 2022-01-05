
def dfs(l,suma,sumb,sumc):
    if l == n:
        if suma != sumb and sumb != sumc and suma != sumc:
            res.append(max(suma,sumb,sumc) - min(suma,sumb,sumc))

    else:
        dfs(l+1,suma+arr[l],sumb,sumc)
        dfs(l+1,suma,sumb+arr[l],sumc)
        dfs(l+1,suma,sumb,sumc+arr[l])



res = []
arr = []
n = int(input())
for _ in range(n):
    a = int(input())
    arr.append(a)

dfs(0,0,0,0)
print(min(res))