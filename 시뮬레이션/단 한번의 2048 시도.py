arr = [
    list(map(int, input().split()))
    for _ in range(4)
]
direct = input()


def merge(direct):
    if direct == 'R':
        for i in range(4):
            for j in range(3, 0, -1):
                if arr[i][j] == arr[i][j - 1]:
                    arr[i][j] = arr[i][j] * 2
                    arr[i][j - 1] = 0


def push(direct):
    if direct == 'R':
        for i in range(4):
            temp = []
            for j in range(3, -1, -1):
                if arr[i][j]:
                    temp.append(arr[i][j])
            shortage = 4 - len(temp)
            for _ in range(shortage):
                temp.append(0)

            for j in range(4):
                arr[i][j] = temp[3 - j]


merge(direct)
push(direct)
for i in range(4):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()
