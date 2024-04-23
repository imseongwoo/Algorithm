def dfs(l, sum, number, idx):
    res = 0
    if l == 3:
        if sum == 0:
            return 1
        else:
            return 0

    if idx >= len(number):
        return 0

    res += dfs(l + 1, sum + number[idx], number, idx + 1)
    res += dfs(l, sum, number, idx + 1)
    return res


def solution(number):
    return dfs(0, 0, number, 0)


print(solution([-2, 3, 0, 2, -5]))
