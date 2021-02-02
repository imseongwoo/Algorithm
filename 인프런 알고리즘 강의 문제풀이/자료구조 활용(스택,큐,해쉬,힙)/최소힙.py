import heapq
ref = []
while True:
    n = int(input())
    if n == 0:
        print(heapq.heappop(ref))

    elif n== -1:
        break
    else:
        heapq.heappush(ref,n)