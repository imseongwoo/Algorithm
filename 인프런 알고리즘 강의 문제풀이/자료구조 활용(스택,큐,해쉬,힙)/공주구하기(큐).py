# 내 풀이
from collections import deque
n,k = map(int,input().split())

arr = deque(range(1,n+1))
count = 0
while len(arr) != 1:
    arr.append(arr.popleft())
    count += 1
    if count == k:
        arr.pop()
        count = 0
arr = list(arr)
print(arr[0])

# 큐에서 뒤쪽으로 값을 보내는 것은 원형으로 도는것과 같은 논리.

# 답
from collections import deque
n,k=map(int,input().split())
dq = list(range(1,n+1))
dq = deque(dq)
while dq:
    for _ in range(k+1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()