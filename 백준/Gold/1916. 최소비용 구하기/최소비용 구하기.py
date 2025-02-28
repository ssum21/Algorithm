import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
dist = [sys.maxsize] * (n+1)

myList = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s, e, w = map(int, input().split())
    myList[s].append((e,w))

start, end = map(int, input().split()) #시작 도시, 종료 도시

def dijkstra(start, end):
    queue = PriorityQueue()
    queue.put((0, start))
    dist[start]  = 0
    while (queue.qsize()>0):
        nowNode = queue.get()
        now = nowNode[1]
        if not visited[now]:
            visited[now] = True
            for n in myList[now]:
                if not visited[n[0]] and dist[n[0]] > dist[now]+n[1]:
                    dist[n[0]] = dist[now]+n[1]
                    queue.put((dist[n[0]], n[0]))
    return dist[end]

print(dijkstra(start, end))