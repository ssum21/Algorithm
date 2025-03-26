import heapq

def solution(scoville, K):
    heapq.heapify(scoville)    
    answer = 0
    
    while True:
        item_1 = heapq.heappop(scoville)
        if item_1 >= K:
            break
        if len(scoville) <= 0:
            return -1
        item_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, item_1 + item_2*2)
        answer += 1
    return answer