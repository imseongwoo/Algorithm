n = int(input())
count = 0
num = 666
while True:

    num = str(num)
    if '666' in num:
        count += 1
        if count == n:
            print(num)
            break
    num = int(num)
    num += 1

