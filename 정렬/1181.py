n = int(input())
arr = set()
for i in range(n):
    arr.add(input())

arr = sorted(arr,key=lambda x:(len(x),x))

arr = list(arr)

for i in range(len(arr)):
    print(arr[i])

