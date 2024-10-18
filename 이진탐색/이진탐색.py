n, target = 13, 45
arr = [23, 34, 36, 41, 45, 49, 52, 57, 64, 72, 76, 81, 89]

idx = -1

left, right = 0, n-1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        idx = mid
        break

    if arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
