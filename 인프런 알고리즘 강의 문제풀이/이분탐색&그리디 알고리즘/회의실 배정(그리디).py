n= int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

array = sorted(array,key=lambda x:(x[1],x[0]))
start = array[0][1]
count = 1
for a,b in array:
    if a >= start:
        count += 1
        start = b
print(count)


