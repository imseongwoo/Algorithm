from collections import Counter

# def solution(X, Y):
#     # 각 문자열에 대한 Counter 객체 생성
#     countX = Counter(X)
#     countY = Counter(Y)
#
#     # 공통 숫자를 찾아내고, 각 숫자의 최소 빈도를 구해 결과 리스트에 추가
#     result = []
#     for digit in countX:
#         if digit in countY:
#             # 공통 숫자의 최소 빈도만큼 결과 리스트에 추가
#             min_count = min(countX[digit], countY[digit])
#             result.extend([digit] * min_count)
#
#     # 결과 리스트가 비어있으면 "-1" 반환
#     if not result:
#         return "-1"
#
#     # 결과 리스트를 내림차순으로 정렬
#     result.sort(reverse=True)
#
#     # 결과 리스트를 문자열로 변환
#     res = ''.join(result)
#
#     # 모두 0으로만 구성된 경우 "0" 반환
#     if res.lstrip('0') == '':
#         return '0'
#
#     return res


def solution(X, Y):
    # 숫자 개수 세기
    nums = Counter(X) & Counter(Y)
    print(Counter(X))
    print(Counter(Y))
    print(nums)
    if not nums:
        return '-1'  # 공통 없는 경우
    elif list(nums) == ['0']:
        return '0'  # 0만 공통인 경우

    nums_order = sorted(list(nums), reverse=True)  # 내림차순 정렬
    answer = ''
    print(nums_order)
    for num in nums_order:
        print("num ="+ num)
        print("nums[num] =" + str(nums[num]))
        answer += num * nums[num]
    return answer

print(solution("5525", "1255"))