import sys
import math
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
IsEven = True

def DFS(start, graph):
    global IsEven
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            check[neighbor] = (check[start]+1) %2
            DFS(neighbor, graph)
        elif (check[neighbor] == check[start]):
            IsEven = False




K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visited = [False] * 200001
    check = [0] * (V+1)
    for j in range(E):
        e1, e2 = map(int, input().split())
        graph[e1].append(e2)
        graph[e2].append(e1)
    for i in range(1, V+1):
        if IsEven:
            DFS(i, graph)
        else:
            break
    if(IsEven):
        print("YES")
    else:
        print("NO")
    IsEven = True

