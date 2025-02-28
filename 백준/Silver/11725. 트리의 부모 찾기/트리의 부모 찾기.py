import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

arr = []
count = [0] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    arr.append((a,b))

def adj_arr(edge):
    adj_list={}
    for u, v in edge:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

new_arr = adj_arr(arr)

def BFS(start, graph):
    queue = deque([start])
    visited = set([start])
    while queue:
        value = queue.popleft()
        for neighbor in graph[value]:
            if neighbor not in visited:
                count[neighbor] = value
                visited.add(neighbor)
                queue.append(neighbor)

BFS(1, new_arr)

for i in range(2, N+1):
    print(count[i])