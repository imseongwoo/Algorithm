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

# 답
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x,0) + 1
for x in b:
    str2[x] = str2.get(x,0) + 1
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print('NO')
        break
else:
    print('YES')