from collections import Counter


n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr)
average = sum(arr)  // n
centnum = arr[n//2]
print(average)
print(centnum)
c= Counter(arr).most_common()


if len(arr) > 1:
    if c[0][1] == c[1][1]:print(c[1][0])

    else : print(c[0][0])
else : print(arr[0])


rangenum = max(arr)-min(arr)


print(rangenum)

