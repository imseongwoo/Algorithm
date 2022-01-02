# 첫번째 값부터 차례대로 해당 값을 처리하거나 처리하지않는 로직으로 해결. 트리로 생각하면 편함

def dfs(level, score, time):
    global maxscore

    if time  > m:
        return
    if level == n :     # 종착지점
        if score>maxscore:
            maxscore = score
    else:
        dfs(level + 1, score + arr[level][0], time + arr[level][1])
        dfs(level + 1, score, time)

maxscore = -1
n,m = map(int,input().split())
arr = []
for _ in range(n):

    arr.append(list(map(int,input().split())))


dfs(0,0,0)
print(maxscore)
