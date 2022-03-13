n = int(input())
arr = list(map(int,input().split()))

ans = list(range(1,n+1))
ref = [0]*(n)

for i in range(n):
    for j in range(n):
        if arr[i] == 0 and ref[j] == 0:
            ref[j] = (i+1)
            break
        if ref[j] == 0:
            arr[i] -= 1


for a in ref:
    print(a,end=' ')

# 답
n = int(input())
a = list(map(int,input().split()))
seq =[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j] = i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x,end=' ')



# index 함수를 이용한 풀이

n = int(input())
a = list(map(int,input().split()))
a = a[::-1]
ans = []
for x in a:
    ans.insert(x,n)
    n-=1