from collections import deque
from copy import deepcopy


def solution(board):
    def bfs(x, y, val, direct):
        n = len(board)
        ch = [[0] * n for _ in range(n)]
        cost = deepcopy(ch)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque()
        queue.append((x, y, val, direct))
        ch[0][0] = 1

        while queue:
            temp = queue.popleft()
            for i in range(4):
                nx = temp[0] + dx[i]
                ny = temp[1] + dy[i]

                if nx >= 0 and ny >= 0 and nx < n and ny < n and board[nx][ny] != 1:
                    if temp[3] == i:
                        new = temp[2] + 100
                    else:
                        new = temp[2] + 600

                    if cost[nx][ny] == 0 or (cost[nx][ny] != 0 and cost[nx][ny] > new):
                        queue.append((nx, ny, new, i))
                        cost[nx][ny] = new

        return cost[n - 1][n - 1]

    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 3))


print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
