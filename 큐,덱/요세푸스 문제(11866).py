from collections import deque
n,k=map(int,input().split())
dq = list(range(1,n+1))
dq = deque(dq)
ref= []
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    ref.append(dq.popleft())

ref = str(ref)
ref = ref.replace('[','<').replace(']','>')

print(ref)
