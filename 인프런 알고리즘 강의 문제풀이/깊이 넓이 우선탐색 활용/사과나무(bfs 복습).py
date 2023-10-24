from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
arr = []
queue = deque()
ch = [[0]*n for _ in range(n)]
queue.append((n//2,n//2))
ch[n//2][n//2] = 1
sum = 0
level = 0

for _ in range(n):
    arr.append(list(map(int,input().split())))

sum += arr[n//2][n//2]

while True:
    if level == n//2:
        break

    size = len(queue)

    for _ in range(size):
        temp = queue.popleft()
        for a in range(4):
            nx = temp[0]+dx[a]
            ny = temp[1]+dy[a]

            if ch[nx][ny] != 1:
                sum += arr[nx][ny]
                ch[nx][ny] = 1
                queue.append((nx,ny))
    level += 1

print(sum)



'''
50  30 29 25 53     29 25 53 10 39 23  
'''
