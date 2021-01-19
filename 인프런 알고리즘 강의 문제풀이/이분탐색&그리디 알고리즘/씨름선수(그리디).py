# 내 풀이
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

array.sort(key=lambda x:x[0])

count = 0
res = set()
for a in range(n):
    weight = array[a][1]
    for b in range(a+1,n):
        if array[b][1] > weight:
            res.add(weight)

print(n-len(res))

# 답
# 키를 내림차순으로 정렬 후 몸무게의 최대값을 구하는 과정에서 count 를 증가시킨다.
n = int(input())
body = []
for i in range(n):
    a,b= map(int,input().split())
    body.append((a,b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x,y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)
