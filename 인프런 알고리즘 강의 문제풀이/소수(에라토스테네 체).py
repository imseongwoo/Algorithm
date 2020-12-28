n = int(input())
ans = 0
for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        ans += 1
print(ans)

# 에라토스네테 체로 푸는 코드

n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2,n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i,n+1,i):
            ch[j] = 1
print(cnt)