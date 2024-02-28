# 리스트가 주어지고 주어진 리스트에서 k개의 수를 합해서 target 값이 되는 경우 구하기

def solution(nums, target):
    def backtrack(start, curr):
        if len(curr) == 2 and sum(nums[i] for i in curr) == target:
            return curr
        for i in range(start, len(nums)):
            curr.append(i)
            ret = backtrack(i+1, curr)

            if ret:
                return ret

            curr.pop()
        return None

    return backtrack(0,[])

print(solution([4,9,7,5,1], 12))