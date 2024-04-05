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

# 에라토스테네스 체
def prime_numbers(n):
    arr = [0] * (n+1)  # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n ** (1 / 2))
    for i in range(2, end + 1):
        if arr[i] == 0:  # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i * i, n + 1, i):  # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0

    return [i for i in arr[2:] if arr[i]]