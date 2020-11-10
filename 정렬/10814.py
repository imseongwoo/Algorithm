
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input().split()))

arr = sorted(arr,key=lambda x:(int(x[0])))



for x,y in arr:
    print(x,y)
