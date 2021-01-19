def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
target_list = list(map(int,input().split()))

for a in target_list:
    result = binary_search(arr,a,0,n-1)
    if result !=  None:
        print(1)
    else:
        print(0)