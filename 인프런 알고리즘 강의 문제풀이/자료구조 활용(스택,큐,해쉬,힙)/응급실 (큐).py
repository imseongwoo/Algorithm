# 내 풀이
from collections import deque
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr = deque(arr)

ans = []
ref = []

test = [0] * n
test[m] = 1
test = deque(test)

while arr:                      # 리스트에 값이 있으면
    res = arr.popleft()
    check = test.popleft()
    maxnum = -1
    for i in range(len(arr)):   # 최댓값 구하기
        if arr[i] > maxnum:
            maxnum = arr[i]
    if res >= maxnum:           # 최댓값보다 크거나 같으면 ans리스트 와 순서를 알려주는 ref 리스트에 넣는다.
        ans.append(res)
        ref.append(check)
    else:                       # 작다면 끝에 다시 넣어준다.
        arr.append(res)
        test.append(check)

for i in range(len(ref)):
    if ref[i] == 1:
        print(i+1)

# 답
from collections import deque
n,m = map(int,input().split())
q = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
q=deque(q)
cnt = 0
while True:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):       # 단 한번이라도 참이 되면 any는 참을 리턴한다.
        q.append(cur)
    else:
        cnt += 1
        if cur[0]==m:
            break
print(cnt)