from copy import deepcopy


def dfs(x, y, check, m, n):
    global answer
    dx = [0, 1]
    dy = [1, 0]
    if x == (n - 1) and y == (m - 1):
        answer += 1
    else:
        for a in range(2):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] != 1:
                check[nx][ny] = 1
                dfs(nx, ny, check, m, n)
                check[nx][ny] = 0


def solution(m, n, puddles):
    global answer

    arr = [[0] * m for _ in range(n)]
    check = deepcopy(arr)
    check[puddles[0][0] - 1][puddles[0][1] - 1] = 1

    dfs(0, 0, check, m, n)

    return answer%1000000007


answer = 0
print(solution(4, 3, [[2, 2]]))
