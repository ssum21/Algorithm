import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향: 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0, 1]

# 초기 위치, 초기 크기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0  # 상어 위치 초기화
            break

now_size = 2
eat_cnt = 0
result_time = 0

def bfs(x, y):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fishes = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 상어 크기보다 작거나 같은 물고기면 이동 가능
                if graph[nx][ny] <= now_size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # 먹을 수 있는 물고기라면 저장
                    if 0 < graph[nx][ny] < now_size:
                        fishes.append((visited[nx][ny], nx, ny))
    # 먹을 수 있는 물고기들 반환
    return sorted(fishes)

while True:
    fish_list = bfs(now_x, now_y)

    if not fish_list:
        break  # 더 이상 먹을 물고기가 없으면 종료

    dist, fish_x, fish_y = fish_list[0]  # 가장 가까운 물고기
    result_time += dist
    eat_cnt += 1
    graph[fish_x][fish_y] = 0
    now_x, now_y = fish_x, fish_y

    # 크기 증가
    if eat_cnt == now_size:
        now_size += 1
        eat_cnt = 0

print(result_time)
