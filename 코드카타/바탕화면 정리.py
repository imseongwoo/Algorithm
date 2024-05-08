def solution(wallpaper):
    answer = []
    arr = [[0]*len(wallpaper[0]) for _ in range(len(wallpaper))]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                arr[i][j] = 1

    min_row = 100
    min_col = 100
    max_row = -1
    max_col = -1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                if i < min_row:
                    min_row = i
                if j < min_col:
                    min_col = j
                if i > max_row:
                    max_row = i
                if j > max_col:
                    max_col = j

    answer.append(min_row)
    answer.append(min_col)
    answer.append(max_row+1)
    answer.append(max_col+1)
    return answer

print(solution([".#...", "..#..", "...#."]))


def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]