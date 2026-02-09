from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
grid = [] # 격자판
boomList = deque() # 폭탄 좌표 리스트

R, C, N = map(int, input().split())

for i in range(R): # 격자판 정보 입력
    row = list(input())
    for j in range(C):
        if row[j] == 'O': # 처음 폭탄 좌표들 저장
            boomList.append([i, j])
    grid.append(row)

t = 1 # 처음 1초가 지난 후에 격자판에 아무 일도 벌어지지 않기 때문에, 초기 시간을 1로 잡아도 된다.

while t < N:

    for i in range(R): # 폭탄 채워넣기
        for j in range(C):
            if grid[i][j] == '.':
                grid[i][j] = 'O'

    t += 1
    if t == N:
        break

    while boomList: # 폭탄 터트리기
        x, y = boomList.popleft()
        grid[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                grid[nx][ny] = '.'

    for i in range(R): # 폭탄 터지고 남은 폭탄들 저장
        for j in range(C):
            if grid[i][j] == 'O':
                boomList.append([i, j])

    t += 1

for g in grid:
    print(''.join(g))