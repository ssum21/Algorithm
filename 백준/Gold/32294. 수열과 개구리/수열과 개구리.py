import sys
import heapq

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

rev = [[] for _ in range(n + 1)]

for u in range(1, n + 1):
    v1 = u - a[u]
    v2 = u + a[u]

    if 1 <= v1 <= n:
        rev[v1].append(u)
    else:
        rev[0].append(u)

    if 1 <= v2 <= n:
        rev[v2].append(u)
    else:
        rev[0].append(u)

INF = 10**30
dist = [INF] * (n + 1)
dist[0] = 0

pq = [(0, 0)]
while pq:
    d, v = heapq.heappop(pq)
    if d != dist[v]:
        continue
    for u in rev[v]:
        nd = d + b[u]
        if nd < dist[u]:
            dist[u] = nd
            heapq.heappush(pq, (nd, u))

sys.stdout.write(" ".join(map(str, dist[1:])) + "\n")
