def solution(office, k):
    n = len(office)  # n x n 배열의 크기
    max_count = 0  # 따뜻하게 할 수 있는 직원 수의 최대값

    # 모든 가능한 k x k 구역을 탐색
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            # 현재 k x k 구역의 1의 개수 세기
            count = 0
            for x in range(i, i + k):
                for y in range(j, j + k):
                    if office[x][y] == 1:
                        count += 1
            # 최대값 갱신
            max_count = max(max_count, count)

    return max_count

# 예시 입력
office = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0]
]
office2 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
k = 2

# 실행 결과 확인
result = solution(office2, k)
print(result)  # 결과: 3
