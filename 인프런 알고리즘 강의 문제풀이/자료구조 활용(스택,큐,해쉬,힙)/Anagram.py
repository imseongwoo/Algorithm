arr = list(input())
arr2 = list(input())
count = 0
for a in arr:
    if a in arr2:
        arr2.remove(a)
    else:
        print('NO')
        break
else:
    if arr2:
        print('NO')
    else:
        print('YES')