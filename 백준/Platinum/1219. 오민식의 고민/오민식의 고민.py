import sys
from collections import deque

input = sys.stdin.readline

n, start, end, m = map(int, input().split()) #노드 수, 시작, 종료, 에지 수

route = []
now_money = [-sys.maxsize] * (n)

for i in range(m):
    s_node, e_node, weight = map(int, input().split())
    route.append((s_node, e_node, weight))

city_can_money = list(map(int, input().split()))

now_money[start] = city_can_money[start]
for i in range(n+10001):
    for s_node, e_node, weight in route:
        if (now_money[s_node] == -sys.maxsize):
            continue
        elif (now_money[s_node] == sys.maxsize):
            now_money[e_node] = sys.maxsize
        else:
            if (now_money[e_node]<now_money[s_node]-weight+city_can_money[e_node]):
                now_money[e_node]=now_money[s_node]-weight+city_can_money[e_node]
                if (i>=n-1):
                    now_money[e_node] = sys.maxsize


# positive cycle(이익 사이클)이 도착 도시에 영향을 줄 수 있는지 확인하기 위한 준비
# updated 배열: n번째 반복에서 값이 갱신되는(즉, 개선되는) 정점을 표시
updated = [False] * n
for s_node, e_node, weight in route:
    if now_money[s_node] != -sys.maxsize and now_money[e_node] < now_money[s_node] - weight + city_can_money[e_node]:
        updated[e_node] = True  # 이 정점은 추가 갱신이 가능한 것으로 표시

# 만약 갱신된 정점이 있다면, 이들로부터 도착 도시(end)에 도달 가능한지 탐색
# (즉, positive cycle이 도착 도시에도 영향을 미칠 수 있음을 의미)
visited = [False] * n
queue = deque()

for i in range(n):
    if updated[i]:
        queue.append(i)
        visited[i] = True

while queue:
    cur = queue.popleft()
    for s_node, e_node, weight in route:
        if s_node == cur and not visited[e_node]:
            visited[e_node] = True
            queue.append(e_node)

# 만약 도착 도시(end)에 도달할 수 있다면, 무한 이익("Gee")가 가능함.
if visited[end]:
    print("Gee")
# 도착 도시로 아예 갈 수 없는 경우
elif now_money[end] == -sys.maxsize:
    print("gg")
# 그 외에는 계산된 최대 이익 출력
else:
    print(now_money[end])
