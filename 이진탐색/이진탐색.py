n, target = 13, 45
arr = [23, 34, 36, 41, 45, 49, 52, 57, 64, 72, 76, 81, 89]

idx = -1

left, right = 0, n - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        idx = mid
        break

    if arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1


def lower_bound(target):
    left = 0
    right = n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx


def upper_bound(target):
    left = 0  # 첫 번째 원소의 위치로 설정합니다.
    right = n - 1  # 마지막 원소의 위치로 설정합니다.
    min_idx = n  # 최소이므로, 답이 될 수 있는 값보다 더 큰 값으로 설정합니다.

    while left <= right:  # [left, right]가 유효한 구간이면 계속 수행합니다.
        mid = (left + right) // 2  # 가운데 위치를 선택합니다.
        if arr[mid] > target:  # 만약에 선택한 원소가 target보다 크다면
            min_idx = min(min_idx, mid)  # 큰 값들의 위치 중 최솟값을 계속 갱신해줍니다.
            right = mid - 1  # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        else:
            left = mid + 1  # 같거나 작은 경우라면 left를 바꿔줍니다.

    return min_idx

# 배열 내 데이터의 수는 upper bound - lower bound
# lower bound와 upper bound의 위치가 같으면 배열 내 값이 없다