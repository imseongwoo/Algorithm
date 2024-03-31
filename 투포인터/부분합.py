import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 0
answer = sys.maxsize
sum = 0

while True:
    if sum >= s:
        answer = min(answer, j - i )
        sum -= arr[i]
        i += 1
    elif j==n:
        break
    else:
        sum += arr[j]
        j += 1

if answer == sys.maxsize:
    print(0)
else:
    print(answer)
