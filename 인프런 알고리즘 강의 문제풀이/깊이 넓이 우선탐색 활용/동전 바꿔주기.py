
def dfs(l,sum):
    global count        # 가지수 check
    if sum > T:         # cut edge. 지폐의 금액을 넘어가는 경우에는 return 시켜준다.
        return

    if l == k:          # 동전을 포함하지 않는 경우도 존재하기 때문에 트리 중간에 해당하는 지폐 금액에 부합하더라도 l==k 일때만(단말노드에 도착했을 때) count를 증가시켜주면 된다.
        if sum == T:
            count += 1
    else:
        for a in range(pb[l]+1):
            dfs(l+1,sum+a*pa[l])

count = 0

T = int(input())
k = int(input())
pa = []         # 동전 금액 저장 리스트
pb = []         # 동전 개수 저장 리스트
for _ in range(k):
    p,n = map(int,input().split())
    pa.append(p)
    pb.append(n)


dfs(0,0)
print(count)
