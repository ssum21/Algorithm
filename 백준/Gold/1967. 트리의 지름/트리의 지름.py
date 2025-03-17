import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    parent, son, weight = map(int, input().split())
    graph[parent].append((son, weight))
    graph[son].append((parent, weight))


dist = [-1 for _ in range(10001)]

def BFS(start):
    q = deque([start])
    visited = set([start])
    while q:
        now = q.popleft()
        for next, weight in graph[now]:
            if next not in visited:
                q.append(next)
                visited.add(next)
                dist[next] = dist[now] + weight

dist[1] = 0
BFS(1)

value = -1
index = 0
for i in range(10001):
    if(dist[i]>value):
        value = dist[i]
        index = i

dist = [-1 for _ in range(10001)]
dist[index] = 0

BFS(index)

print(max(dist))