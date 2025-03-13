import sys
from collections import deque

sys.setrecursionlimit(10**6)

n, K = map(int, input().split())



def BFS(start, K):
    time = 0
    queue=deque([start])
    visited= [False] * (2*K+1)
    visited[start] = True
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == K:
                return(time)
            for next in (cur-1, cur+1, cur*2):
                if 0<=next<=(2*K) and not visited[next]:
                    visited[next] = True
                    queue.append(next)
        time += 1



if n>K:
    print(n-K)
else:
    print(BFS(n, K))