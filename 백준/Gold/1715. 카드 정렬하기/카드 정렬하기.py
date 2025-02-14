import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

min_heap = []

N=int(input().rstrip())

for i in range(N):
    heapq.heappush(min_heap, int(input().rstrip()))

result = 0

first_value = heapq.heappop(min_heap)
result += first_value
while min_heap:
    second_value = heapq.heappop(min_heap)
    result+=second_value
    if min_heap:
        heapq.heappush(min_heap, first_value + second_value)
        first_value=heapq.heappop(min_heap)
        result += first_value
    else:
        break

if(N==1):
    result = 0

print(result)