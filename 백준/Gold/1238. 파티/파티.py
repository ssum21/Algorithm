import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, X = map(int, input().split()) # 학생수, 총 도로수, 가야하는 마을
graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    dist = [sys.maxsize] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now]<distance:
            continue
        for next in graph[now]:
            cost = distance + next[1]
            if cost < dist[next[0]]:
                dist[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return dist

#다익스트라 알고리즘 실행
result_arr = []
X_arr = dijkstra(X)

for i in range(1, N+1):
    y_arr = dijkstra(i)
    result_arr.append(y_arr[X] + X_arr[i])

print(max(result_arr))