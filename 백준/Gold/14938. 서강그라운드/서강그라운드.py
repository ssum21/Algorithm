import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
t = list(map(int, input().split()))

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for i in range(n):
    graph[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if (graph[k][j] > graph[k][i] + graph[i][j]):
                graph[k][j] = graph[k][i] + graph[i][j]

result = 0

for i in range(n):
    sum_temp = 0
    for j in range(n):
        if graph[i][j]<=m:
            sum_temp += t[j]
    if sum_temp>result:
        result = sum_temp

print(result)