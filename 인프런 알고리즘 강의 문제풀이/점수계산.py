n = int(input())

grade = list(map(int,input().split()))

score = []

score.append(grade[0])

for i in range(1,n):
    if grade[i] == 0:
        score.append(0)
    elif grade[i] == 1 and grade[i-1] == 0:
        score.append(1)
    else:
        score.append(score[i-1]+1)

print(sum(score))

## 다른풀이
a = list(map(int,input().split()))
cnt = 0
sum = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0