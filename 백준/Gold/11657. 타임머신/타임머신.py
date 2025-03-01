import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 노드, 에지

edges = []
distance = [sys.maxsize] * (N+1)

for i in range(M):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

distance[1] = 0 #1번에서 부터 출발

for i in range(N-1): # 노드 개수 -1
    for start, end, weight in edges: # 에지 개수
        if distance[start] != sys.maxsize and distance[end] > distance[start] + weight:
            distance[end] = distance[start] + weight

mCycle = False

for start, end, weight in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + weight:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)
        