import sys
import queue
from heapq import heappush, heappop

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())
    max_heap = []
    min_heap = []
    result = []
    numbers = []

    while len(numbers) < M:
        numbers.extend(list(map(int, input().split())))

    for i in range(M):
        num = numbers[i]
        if(len(max_heap)<=len(min_heap)):
            heappush(max_heap,-num)
        else:
            heappush(min_heap, num)
        
        if min_heap and -max_heap[0] > min_heap[0]:
            temp_max = -heappop(max_heap)
            temp_min = heappop(min_heap)
            heappush(max_heap, -temp_min)
            heappush(min_heap, temp_max)
        
        if (i + 1) % 2 == 1:
            result.append(-max_heap[0]) 
    
    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i+10])