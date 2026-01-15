import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())

tree = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N + 1)
dp = [1] * (N + 1)

def dfs(curr_node):
    visited[curr_node] = True
    for next_node in tree[curr_node]:
        if not visited[next_node]:
            dfs(next_node)
            dp[curr_node] += dp[next_node]

dfs(R)

for _ in range(Q):
    u = int(input())
    print(dp[u])
