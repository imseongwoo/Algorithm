def dfs():
    if len(temp) == m:     # 종료조건
        print(' '.join(map(str, temp)))
        return

    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)  # 사용
            dfs()
            temp.pop()  # 사용했던거 풀어주기

n,m = map(int, input().split())
temp = []
dfs()
