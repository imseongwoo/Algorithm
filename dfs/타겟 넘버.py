
def dfs(level,numbers,target, sum):
    res = 0
    if level == len(numbers):
        if sum == target:
            return 1
        else: return 0
    else:
        res += dfs(level+1, numbers, target, sum + numbers[level])
        res += dfs(level+1, numbers, target, sum - numbers[level])
    return res


def solution(numbers, target):
    answer = 0
    answer = dfs(0, numbers, target, 0)

    return answer

print(solution([1,1,1,1,1], 3))