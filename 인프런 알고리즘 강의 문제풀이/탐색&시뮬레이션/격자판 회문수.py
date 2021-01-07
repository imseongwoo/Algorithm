# 내 풀이
a = [list(map(int,input().split())) for _ in range(7)]
count = 0
def check_col(x,y):
    global count
    if a[x][y] == a[x][y+4] and a[x][y+3] == a[x][y+1]:
        count += 1
def check_row(x,y):
    global count
    if a[x][y] == a[x+4][y] and a[x+1][y] == a[x+3][y]:
        count += 1
for i in range(7):
    for j in range(7):
        if j == 0 or j == 1 or j == 2:
            check_col(i,j)
        if i == 0 or i == 1 or i == 2:
            check_row(i,j)
print(count)

# 답
board = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt+=1