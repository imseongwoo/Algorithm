n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

arr = sorted(arr,key=lambda x:(x[1],x[0]))

for a,b in arr:
    print(a,b)
