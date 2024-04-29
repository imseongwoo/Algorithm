def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0:
            return False
    return True

def dfs(index, count, current_sum, nums, result):
    if count == 3:
        if isPrime(current_sum):
            result[0] += 1
        return

    for i in range(index, len(nums)):
        dfs(i + 1, count + 1, current_sum + nums[i], nums, result)

def solution(nums):
    result = [0]
    dfs(0, 0, 0, nums, result)
    return result[0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(nums))