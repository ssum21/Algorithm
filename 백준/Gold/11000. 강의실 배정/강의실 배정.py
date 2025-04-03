import sys
import heapq

input = sys.stdin.readline

n = int(input())

table = []

for _ in range(n):
    start, end = map(int, input().split())
    table.append((start, end))

table.sort()

rooms = []

heapq.heappush(rooms, table[0][1])

for i in range(1, n):
    if table[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    
    heapq.heappush(rooms, table[i][1])

print(len(rooms))