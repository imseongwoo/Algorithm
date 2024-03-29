import heapq

def dijkstra(graph, start, final, n):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]




# 1. 우선순위큐에 시작노드 추가
#     2. 우선순위가 가장 높은(비용이 제일 적은) 노드 추출
#     3. 방문여부 확인
#         4. 비용 업데이트
#         5. 현재 노드와 연결된 노드 우선순위  큐에 추가
#     6. 목적지에 기록도ㅚㄴ 비용 반환
