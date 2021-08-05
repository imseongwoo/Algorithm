# 내 풀이 ㅎㅎ
def DFS(l,sum):
    global cnt
    if l >= cnt:
        return
    # if l+((m-sum)//max_num) > cnt:
    #     return
    if sum > m:
        return
    if sum == m:
        if l < cnt:
            cnt = l
    else:
        for i in range(n):
            DFS(l+1,sum+a[i])

cnt = 214700000
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
m = int(input())
max_num = max(a)
DFS(0,0)
print(cnt)


""" 답
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L>=res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True)                # 전위순회이기 때문에 첫 출발이 너무 깊게 들어가는것을 반복하기 위해 내림차순으로 적용시켜 시간을 단축함
    DFS(0, 0)
    print(res)
"""