def solution(nums):
    answer = 0
    poketmon = {}
    visited = {}
    for a in nums:
        poketmon[a] = poketmon.get(a,0) + 1
        visited[a] = False
    num = 0
    while num != (len(nums) // 2):
        for a in poketmon:
            if num == (len(nums) // 2) :
                break
            if poketmon[a] > 0:
                if not visited[a]:
                    poketmon[a] -= 1
                    num += 1
                    answer += 1
                    visited[a] = True
                else:
                    poketmon[a] -= 1
                    num += 1
    return answer

print(solution([3,3,3,2,2,2]))