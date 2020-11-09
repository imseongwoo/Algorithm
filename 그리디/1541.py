sentence = input().split('-')

arr = []
for i in sentence:
    answer = 0
    for j in i.split('+'):
        answer += int(j)
    arr.append(answer)

sum = arr[0]
for k in range(1,len(arr)):
    sum = sum - arr[k]

print(sum)