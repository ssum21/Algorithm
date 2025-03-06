from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

def BFS(start, graph,n):
    distance = [-1]*(n+1)
    distance[1] = 0
    queue = deque([start])
    visited = set([start])
    while queue:
        k = queue.popleft()
        for neighbor in graph[k]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[k] + 1
    max_distance = max(distance)
    answer = distance.count(max_distance)
    return answer

def solution(n, edge):
    answer = 0
    arr = defaultdict(list)
    for s, e in edge:
        arr[s].append(e)
        arr[e].append(s)
    return BFS(1, arr, n)