import heapq

n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    # x가 0이 아니라면
    # 우선순위 큐에 넣어줍니다.
    # 단, 절댓값이 작은 값부터 나오도록
    # (|x|, x) 형태로 넣어줍니다.
    if x != 0:
        heapq.heappush(pq, (abs(x), x))

    else:
        if not pq:
            print(0)
            continue
        _, v = heapq.heappop(pq)
        print(v)