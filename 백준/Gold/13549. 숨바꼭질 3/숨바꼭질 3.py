import sys
from collections import deque

input = sys.stdin.readline

n, K = map(int, input().split())

queue = deque([n])
dist = [-1 for _ in range(100001)]
ways = [0 for _ in range(100001)]

dist[n] = 0
ways[n] = 1

while queue:
    k = queue.popleft()
    for i in (k-1, k+1, k*2):
        if 0 <= i < 100001:
            if dist[i] == -1:
                if (i == k*2):
                    dist[i] = dist[k]
                    ways[i] = ways[k]
                    queue.appendleft(i)
                else:
                    dist[i] = dist[k] + 1
                    ways[i] = ways[k]
                    queue.append(i)
            elif dist[i] == dist[k] + 1:
                ways[i] += ways[k]

print(dist[K])