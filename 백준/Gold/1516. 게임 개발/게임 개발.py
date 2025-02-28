import sys
import math
from collections import deque

input = sys.stdin.readline

N = int(input())
time = [0] * (N+1)
build_time = [0] * (N+1)
a = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    build_time[i] = temp[0]
    time[i] = temp[0]
    for k in temp[1:-1]:
        a[k].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1, N+1):
    if(indegree[i]==0):
        queue.append(i)

while queue:
    curr = queue.popleft()
    for next in a[curr]:
        indegree[next] -= 1
        build_time[next] = max(build_time[next], build_time[curr] + time[next])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N+1):
    print(build_time[i])