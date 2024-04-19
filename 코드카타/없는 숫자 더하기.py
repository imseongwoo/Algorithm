def solution(numbers):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for a in numbers:
        if a in arr:
            arr.remove(a)
    return sum(arr)

solution([1,2,3,4,6,7,8,0])