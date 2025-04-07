# 입력
M, N = map(int, input().split())

# 방문 표시용 배열
visited = [[False] * N for _ in range(M)]

# 방향: 오른쪽 → 아래 → 왼쪽 → 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시작점
x, y = 0, 0
visited[x][y] = True

# 초기 방향: 오른쪽 (0)
dir = 0

# 꺾은 횟수
turn_count = 0

# 총 칸 수
total_cells = M * N
visited_cells = 1

while visited_cells < total_cells:
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    # 이동할 수 없는 경우 (벽이거나 이미 방문)
    if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[nx][ny]:
        dir = (dir + 1) % 4  # 방향 전환
        turn_count += 1
        continue  # 방향만 바꾸고 다시 시도
    
    # 이동
    x, y = nx, ny
    visited[x][y] = True
    visited_cells += 1

print(turn_count)
