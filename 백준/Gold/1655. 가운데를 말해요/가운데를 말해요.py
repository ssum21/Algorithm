import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []

for i in range(n):
    k = int(input())
    if len(min_heap) == len(max_heap):
        heappush(max_heap, -k)
    else:
        heappush(min_heap, k)
    
    if min_heap and -max_heap[0] > min_heap[0] :
        temp_max = heappop(max_heap)
        temp_min = heappop(min_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, -temp_max)

    print(-max_heap[0])
