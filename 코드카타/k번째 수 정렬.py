def solution(array, commands):
    answer = []
    for i,j,k in commands:
        slice_list = array[i-1:j]
        slice_list.sort()
        answer.append(slice_list[k-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])