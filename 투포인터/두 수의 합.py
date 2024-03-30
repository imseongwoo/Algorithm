n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

a = 0
b = n - 1
answer = 0

while a <= b:
    if a >= b:
        break
    if arr[a] + arr[b] == x:
        answer += 1
        a += 1
    elif arr[a] + arr[b] < x:
        a += 1
    else:
        b -= 1

print(answer)
