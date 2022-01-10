n,m = map(int,input().split())
ch = [0] * 10000        # 체크 리스트
dist = [0] * 10000      # 간선을 1이라고 가정한 거리

queue = []
queue.append(n)
ch[n] = 1

while queue:
    temp = queue.pop(0)

    if temp == m:   # 해당 위치에 도달시 종료
        break

    for a in(temp-1,temp+1,temp+5): # 각각 뒤로 1 앞으로 1 앞으로 5 이동 반복
        if 0 <= a <= 10000:     # 직선 좌표 범위
            if ch[a] != 1:      # 방문한 곳이 아니면 실행
                queue.append(a) # 큐에 넣어주기
                ch[a] = 1       # 방문 체크
                dist[a] = dist[temp] + 1    # 거리 1 증가



print(dist[m])     