import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, e = map(int, input().split()) #정점의 개수 N과 간선의 개수 E

graph = [[] for _ in range(n+1)]
distance = [sys.maxsize] * (n+1)
start = 1

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) #반드시 들려야 하는 정점 위치

for i in graph[v1]:
    if(i[0]==v2):
        v_weight = i[1]
        break

q = []


def dijkstra(start):
    distances = [sys.maxsize] * (n + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for nxt, weight in graph[now]:
            cost = dist + weight
            if cost < distances[nxt]:
                distances[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return distances

d1 = dijkstra(1)
dv1 = dijkstra(v1)
dv2 = dijkstra(v2)

path1 = d1[v1] + dv1[v2] + dv2[n]
path2 = d1[v2] + dv2[v1] + dv1[n]
result = min(path1, path2)

print(result if result < sys.maxsize else -1)
