n = int(input())
for _ in range(n):
    cnt = 0
    arr = list(map(int,input().split()))
    avg = (sum(arr)-arr[0])/arr[0]
    for i in range(1,len(arr)):
        if arr[i] > avg:
           cnt += 1
    answer = (cnt/arr[0])*100
    print(f'{answer:.3f}%')