n = int(input())        # n의 크기 입력

graph = [list(map(int,input().split())) for _ in range(n)]  # 격자판 입력

start = end = n//2  # 시작값과 끝값 선언

sum = 0
for i in range(n):      # n번 반복
    for j in range(start,end+1):  # start 부터 end 까지의 수를 반복하면서 더한다
        sum += graph[i][j]
    if i < n//2:        # 증가하는 다이아몬드 모양
        start -= 1
        end += 1
    else:               # 감소하는 다이아몬드 모양
        start += 1
        end -= 1
print(sum)