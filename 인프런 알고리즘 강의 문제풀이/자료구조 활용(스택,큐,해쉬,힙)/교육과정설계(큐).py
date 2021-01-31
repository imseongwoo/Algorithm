must = list(input())
n = int(input())
arr = []
count = 1
for _ in range(n):
    arr.append(input())
for a in arr:

    ref = []

    a = list(a)
    num = len(a)
    for x in a:
        if x in must:
            if not x in ref:
                ref.append(x)
        else:
            continue
    if any(ref[y] != must[y] for y in range(len(ref))):
        print(f'#{count} NO')
        count += 1
    else:
        print(f'#{count} YES')
        count += 1

# 답
from collections import deque

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" % (i + 1))