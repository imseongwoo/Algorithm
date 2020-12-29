n = int(input())

for _ in range(n):
    sum = 0
    cnt = 0
    case = list(input())
    for a in case:
        if a == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
            continue
    print(sum)