def solution(events, limit):
    def is_valid_period(period):
        count = 0
        for i in range(len(events)):
            if i == 0 or events[i] // period != events[i - 1] // period:
                count = 1
            else:
                count += 1
            if count > limit:
                return False
        return True

    max_period = 0
    for period in range(1, events[-1] + 1):
        if is_valid_period(period):
            max_period = period
    return max_period


# 테스트 케이스 1
print(solution([3, 7, 8], 1))  # 결과: 4

# 테스트 케이스 2
print(solution([3, 7, 8], 2))  # 결과: 8

# 테스트 케이스 3
print(solution([1, 2, 3, 4, 5, 6], 1))  # 결과: 1

# 테스트 케이스 4
print(solution([1, 2, 3, 4, 5, 6], 2))  # 결과: 2