temp = -1

for i in range(9):
    num = int(input())
    if num > temp:
        temp = num
        cnt = i+1
    else:
        continue
print(temp)
print(cnt)