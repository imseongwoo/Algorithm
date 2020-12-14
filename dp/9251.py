a = input()
b = input()

arr = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)] # 2차원 배열 초기화

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            arr[i+1][j+1] = arr[i][j] + 1   # 2개가 같다면 대각선의 개수 +1
        else:
            arr[i+1][j+1] = max(arr[i+1][j],arr[i][j+1])    # 다르다면 좌측과 상단중에 큰값

print(arr[len(b)][len(a)])