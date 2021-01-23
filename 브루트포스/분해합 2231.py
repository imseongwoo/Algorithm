n = int(input())
for x in range(1,n):
    sum = 0
    a = x
    while a > 0:
        sum += (a%10)
        a = a//10
    result = x + sum
    if result == n:
        print(x)
        break
else:
    print('0')
