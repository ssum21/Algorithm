import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9+7

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

def dfs(u):
    visited[u] = True
    cnt = 1
    for v in graph[u]:
        if not visited[v]:
            cnt += dfs(v)
    return cnt

answer = 1
for i in range(1, N+1):
    if not visited[i]:
        size = dfs(i)
        answer = (answer * size) % MOD

print(answer)