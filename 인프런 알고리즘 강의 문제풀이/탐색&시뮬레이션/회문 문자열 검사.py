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
# 다른 문제풀이
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('no')
            break
        else:
            print('yes')
            