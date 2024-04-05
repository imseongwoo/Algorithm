import math
n = int(input())
arr = []

if n == 1:
    print(0)
    exit(0)

arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True:
        j = 2

        while (i * j) <= n:
            arr[i*j] = False
            j += 1

prime_list = []
for i in range(2, n + 1):
    if arr[i] == True:
        prime_list.append(i)


start = 0
end = 0
sum = prime_list[0]
answer = 0
while True:
    if end > len(prime_list) - 1:
        break
    if sum == n:
        answer += 1
        sum -= prime_list[start]
        start += 1
    elif sum > n:
        sum -= prime_list[start]
        start += 1
    else:
        end += 1
        if end == (len(prime_list) - 1):
            if prime_list[end] == n:
                answer += 1
            break
        sum += prime_list[end]

print(answer)
