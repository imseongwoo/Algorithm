n = int(input())
tester = list(map(int, input().split()))
b,c = map(int, input().split())

answer = 0

for a in tester:
    if a > b:
        answer+=1
        if (a-b) % c == 0:
            answer += (a - b) // c
        else:
            answer += ((a - b) // c + 1)
    else:
        answer += 1

print(answer)