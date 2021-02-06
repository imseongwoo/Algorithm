# 내 풀이
def DFS(v):
    if v == n :
        sum=0
        sum2=0
        for i in range(1, max_num+1):
            if ch[i] == 1:
                sum += i
            elif ch[i] == 0 and i in arr:
                sum2 += i
        if sum2 == sum:
            global ref
            ref = 1
            return

    else:
        ch[arr[v]] = 1
        DFS(v + 1)
        ch[arr[v]] = 0
        DFS(v + 1)


if __name__ =="__main__":
    ref=0
    n = int(input())
    arr = list(map(int,input().split()))
    max_num = max(arr)
    sum_num = sum(arr)
    ch = [0]*(max_num+1)
    DFS(0)
    if ref == 0:
        print('NO')
    else:
        print('YES')

