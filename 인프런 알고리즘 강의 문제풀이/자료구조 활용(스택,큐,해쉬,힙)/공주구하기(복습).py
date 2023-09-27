n,k = map(int,input().split())
queue = list(range(1,n+1))

while len(queue) != 1:
    for _ in range(k-1):
        tmp = queue.pop(0)
        queue.append(tmp)
    queue.pop(0)

print(queue[0])