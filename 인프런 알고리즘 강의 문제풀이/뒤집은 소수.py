n = int(input())
arr = list(map(str,input().split()))
ref = []
def isPrime(n):
    ans = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ans += 1
    if ans == 2:
        return ref.append(n)

for i in arr:
    i = list(i)
    i.reverse()

    ans =''
    for j in range(len(i)):
        ans += i[j]
    ans = int(ans)
    isPrime(ans)

for i in ref:
    print(i,end=' ')

