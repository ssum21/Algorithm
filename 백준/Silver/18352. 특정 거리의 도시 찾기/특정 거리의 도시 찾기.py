import sys
from collections import defaultdict
import math
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
route = defaultdict(list)
visited = [-1] * (N+1)

def makeroute(A, B):
    if not route[A]:
        route[A] = []
    route[A].append(B)

def BFS(start, route):
    queue = deque()
    queue.append(start)
    visited[start] += 1
    while queue:
        temp = queue.popleft()
        for neighbor in route[temp]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[temp] + 1
                queue.append(neighbor)



for i in range(M):
    A, B = map(int, input().split())
    makeroute(A,B)

BFS(X, route)

answer =[]

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)


if(not answer):
    print('-1')
else:
    answer.sort()
    for i in answer:
        print(i)

