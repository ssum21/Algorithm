import sys
import math
from collections import deque

input = sys.stdin.readline

# 목표는 만나는 최소 시간과 최소시간에 모든 시간을 다 쓰는 사람의 지나는 도로의 수 카운트

n = int(input()) # 도시 수
m = int(input()) # 도로 수

cityisdegree = [0] * (n+1) # 도시에 대한 진입차수
maxtime = [0] * (n+1) #걸리는 최대 시간
visitedcityroad = [0] * (n+1) # 방문하는 도시의 최대 수 (최대 시간 걸리는 사람이 방문하는 도시의 최대 수)
a = [[] for _ in range(n+1)] # 모든 이어진 도로 정보
reverseA = [[] for _ in range(n+1)] # 모든 이어진 역방향 도로 정보

for i in range(m):
    s, e, min = map(int, input().split()) # 출발 도시, 도착도시, 소요시간
    cityisdegree[e] += 1
    a[s].append((e, min))
    reverseA[e].append((s, min))

s_city, e_city = map(int, input().split()) # 시작 도시, 도착도시

queue = deque()
queue.append(s_city)

while queue:
    now = queue.popleft()
    for e, min in a[now]:
        maxtime[e] = max(maxtime[e], maxtime[now]+min)  # 이 로직 맞는지 점검이 필요할듯?
        cityisdegree[e] -= 1
        if (cityisdegree[e]==0):
            queue.append(e)

resultCount = 0 # 방문 최대횟수
visited = [False] * (n+1)
queue.clear()
queue.append(e_city)

while queue:
    now = queue.popleft()
    for s, min in reverseA[now]:
        if(maxtime[now] == maxtime[s] + min):
            resultCount+=1
            if not visited[s]:
                visited[s] = True
                queue.append(s)


print(maxtime[e_city])
print(resultCount)