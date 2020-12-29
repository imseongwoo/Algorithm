a = int(input())
b = int(input())
c = int(input())

ref = a * b * c
ref = list(str(ref))
arr = [0]*10
for i in ref:
    arr[int(i)] += 1
for i in range(10):
    print(arr[i])