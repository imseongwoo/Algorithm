import heapq
def solution(scoville, k):
    answer = 0
    length = len(scoville)
    heapq.heapify(scoville)

    while True:
        food_one = heapq.heappop(scoville)
        if food_one >= k:
            break
        if answer >= length-1:
            return -1
        food_two = heapq.heappop(scoville)
        new_food = food_one + food_two * 2
        heapq.heappush(scoville, new_food)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
