from collections import deque

a,b = map(int,input().split())
queue = deque()
queue.append(a)
ch = [0]*10000
dist = [0]*10000

while queue:
    temp = queue.popleft()

    if temp == b:
        break

    for i in (temp-1, temp+1, temp+5):
        if ch[i] != 1:
            queue.append(i)
            ch[i] = 1
            dist[i] = dist[temp] + 1
print(dist[b])