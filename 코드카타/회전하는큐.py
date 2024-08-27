from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = [i for i in range(1, n + 1)]
num = deque(num)
cnt = 0
for a in arr:
    while True:
        if num[0] == a:
            num.popleft()
            break
        else:
            if num.index(a) <= len(num) // 2:
                num.rotate(-1)
                cnt += 1
            else:
                num.rotate(1)
                cnt += 1
print(cnt)