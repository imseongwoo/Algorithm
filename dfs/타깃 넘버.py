'''def dfs(l,sum,numbers,target):
    global answer

    if l == len(numbers):
        if sum == target:
            answer += 1
    else:
        dfs(l+1, sum+numbers[l], numbers, target)
        dfs(l+1, sum-numbers[l], numbers, target)


def solution(numbers, target):
    dfs(0,0,numbers,target)
    return answer

print(solution([4,1,2,1],2))
'''
def dfs(l,sum,numbers,target):
    res = 0

    if l == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    else:
        res += dfs(l+1, sum+numbers[l], numbers, target)
        res += dfs(l+1, sum-numbers[l], numbers, target)
    return res


def solution(numbers, target):
    answer = dfs(0,0,numbers,target)
    return answer

print(solution([4,1,2,1],2))