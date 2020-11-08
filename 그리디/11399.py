# atm
n = int(input())

p = list(map(int,input().split()))

minp = sorted(p)

list1 =[]

for i in range(n):
    sum = 0
    for j in range(i+1):
        sum += minp[j]
    list1.append(sum)
sump = 0
for i in range(n):
    sump += list1[i]
print(sump)