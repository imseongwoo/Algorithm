import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):  # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return -heapq.heappop(self.items)

    def top(self):  # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return -self.items[0]

pq = PriorityQueue()
pq.push(2)
pq.push(9)
pq.push(5)
print(pq.top())
pq.pop()

while not pq.empty():
    print(pq.top())
    pq.pop()