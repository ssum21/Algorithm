import sys
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

A = defaultdict(list)
visited = [False] * (N)
max_depth = 0
found = False

for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

def DFS(v, depth):
    global found

    if depth == 4:
        found=True
        return
    
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            visited[i]= True
            DFS(i, depth+1)
            if found :
                return
    
    visited[v] = False

for i in range(N):
    DFS(i, 0)
    if found:
        print(1)
        break
else:
    print(0)