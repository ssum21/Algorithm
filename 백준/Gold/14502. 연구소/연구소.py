import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

initGraph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, virusGraph):
    virus = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if virusGraph[nx][ny] == 1:
                continue
            #virus 퍼뜨리기
            if virusGraph[nx][ny] == 0:
                virusGraph[nx][ny] = 2
                virus += 1
                queue.append((nx, ny))
    return virus


# 빈칸인 위치 찾기
empty_list = []
for empty_x in range(n):
    for empty_y in range(m):
        if initGraph[empty_x][empty_y] == 0:
            empty_list.append([empty_x, empty_y])

# 빈칸 위치 중 3개 조합 만들기
three_wall_list = list(combinations(empty_list, 3))

# 빈칸의 조합마다 바이러스 파뜨려서 가장 적은 바이러스의 수 찾기
result = len(empty_list)
for three_wall in three_wall_list:
    virusGraph = copy.deepcopy(initGraph)
    # 벽 세개 만들기
    for wall in three_wall:
        wall_x, wall_y = wall
        virusGraph[wall_x][wall_y] = 1

    virusCount = 0
    for i in range(n):
        for j in range(m):
            if initGraph[i][j] == 2:
                virusCount += bfs(i, j, virusGraph)
    #바이러스가 가장 적게 퍼진수를 저장하기
    if virusCount < result:
        result = virusCount

print(len(empty_list) - result - 3)