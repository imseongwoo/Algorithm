import itertools

n,m = map(int,input().split())
arr = list(map(int,input().split()))
res = []
for i in range(n):
    temp = arr[i+1:]                                # 자기 자신을 제외하고 2개를 뽑을 리스트 생성
    if len(temp)>=2:                                # 2개를 골라야 하므로 길이가 2 이상
        for x in itertools.combinations(temp,2):    # itertools 를 이용하여 temp 에서 2개를 뽑는 경우의 수를 리스트로 가지는 x 생성
            ans = sum(x)+arr[i]                     # 리스트의 합과 자기 자신의 합을 더한 값이 m보다 작으면 최종 값에 append 시켜준다.
            if ans <= m:
                res.append(ans)
print(max(res))                                     # 최댓값 출력