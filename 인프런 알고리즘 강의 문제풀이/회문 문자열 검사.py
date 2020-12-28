n = int(input())

for i in range(n):
    cnt = 0
    word = list(input())
    temp = list(reversed(word))

    for i in range(len(word)):
        if word[i].upper() == temp[i].upper():
            cnt += 1

    if cnt == len(word):
        print('YES')
    else:
        print('NO')

# 역순으로 배열하는법 : s==s[::-1]
