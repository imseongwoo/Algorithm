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

# 답
import heapq as hq
a =  []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a,n)