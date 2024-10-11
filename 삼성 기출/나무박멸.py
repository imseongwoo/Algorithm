# n = 격자의 크기, m = 박멸 진행 년 수
# k = 제초제 확산 범위, c = 제초제가 남아있는 년 수
n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
herb = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

herb_dx = [-1, -1, 1, 1]
herb_dy = [-1, 1, -1, 1]

ans = 0


def is_range(x, y):
    return 0 <= x < n and 0 <= y < n


def grow_tree():
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]
                    if is_range(nx, ny) and arr[nx][ny] != 0 and arr[nx][ny] != -1:
                        cnt += 1
                arr[i][j] += cnt


def breed_tree():
    global arr
    narr = [row[:] for row in arr]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                breed_xy = []
                for a in range(4):
                    nx, ny = i + dx[a], j + dy[a]
                    if is_range(nx, ny) and arr[nx][ny] == 0 and herb[nx][ny] == 0:
                        cnt += 1
                        breed_xy.append((nx, ny))
                if not cnt:
                    continue
                breed_n = arr[i][j] // cnt
                for x, y in breed_xy:
                    narr[x][y] += breed_n
    arr = narr


def throw_herb():
    global ans
    max_herb_cnt = 0
    max_x, max_y = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                herb_n = arr[i][j]
                for a in range(4):
                    nx = i
                    ny = j
                    for _ in range(k):
                        nx, ny = nx + herb_dx[a], ny + herb_dy[a]
                        # 전파 도중 벽이 있거나 나무가 없을 경우 그 칸 까지 제초제가 뿌려지고 마무리
                        if is_range(nx, ny) and arr[nx][ny] != -1 and arr[nx][ny] != 0:
                            herb_n += arr[nx][ny]
                if max_herb_cnt < herb_n:
                    max_herb_cnt = herb_n
                    max_x = i
                    max_y = j

    ans += max_herb_cnt

    if arr[max_x][max_y] > 0:
        arr[max_x][max_y] = 0
        herb[max_x][max_y] = c

        x = max_x
        y = max_y

        for a in range(4):
            for _ in range(k):
                nx, ny = x + herb_dx[a], y + herb_dy[a]
                if not is_range(nx, ny):
                    break
                if arr[nx][ny] <= 0:
                    herb[nx][ny] = c
                    break
                arr[nx][ny] = 0
                herb[nx][ny] = c


def delete_herb():
    for i in range(n):
        for j in range(n):
            if herb[i][j] > 0:
                herb[i][j] -= 1


for _ in range(m):
    # 1단계 : 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장
    grow_tree()
    # 2단계 : 기존에 있었던 나무가 아무것도 없는칸에 번식 진행
    breed_tree()
    # 3단계: 제초제 기간 1년 감소
    delete_herb()
    # 4단계 : 가장 많이 박멸되는 칸에 제초제 투하
    throw_herb()

print(ans)
