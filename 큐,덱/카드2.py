from collections import deque
n = int(input())
arr = list(range(1,n+1))
arr = deque(arr)

while len(arr)>1:
    arr.popleft()
    arr.append(arr.popleft())

arr = list(arr)
print(arr[0])