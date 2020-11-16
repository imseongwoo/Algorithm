# def recursion(n,k):
#     if k==0:
#         return 1
#     if k==1:
#         return n
#     x=recursion(n,int(k//2))
#     if k%2==0:
#         return x*x
#     else:
#         # return n*x*x

n,k = map(int,input().split())
arr=[0]*50
p=0
while k != 1:
    if k%2==0:
        arr[p]=1
        p += 1
    elif k%2==1:
        arr[p]=-1
        p += 1
    k =int(k//2)
tmp=n
p=p-1
for i in range(p,-1,-1):
    if arr[i]==1:
        tmp=tmp*tmp
        tmp %= 1000000007
    elif arr[i] == -1:
        tmp=tmp*tmp
        tmp %= 1000000007
        tmp *= n
        tmp %= 1000000007


print(tmp)

# print(recursion(n,k)%1000000007)