n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def bomb_type1(x, y):
    coords = {(x, y)}
    for dy in [-2, -1, 1, 2]:
        ny = y + dy
        if 0 <= ny < n:
            coords.add((x, ny))
    return coords

def bomb_type2(x, y):
    coords = {(x, y)}
    for dx, dy in [(1,0), (-1, 0),(0, 1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            coords.add((nx, ny))
    return coords

def bomb_type3(x, y):
    coords = {(x, y)}
    for dx, dy in [(-1, 1), (-1, -1), (1, 1), (1, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            coords.add((nx, ny))
    return coords

bomb_loc = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_loc.append((i, j))

from itertools import product

max_area = 0

def backtrack(idx, destroyed_set):
    global max_area
    
    # 모든 폭탄에 대해 타입을 선택했으면
    if idx == len(bomb_loc):
        max_area = max(max_area, len(destroyed_set))
        return
    
    # 현재 폭탄의 위치
    y, x = bomb_loc[idx]  # (행, 열) = (y, x)
    
    # 3가지 폭탄 타입 시도
    for bomb_func in [bomb_type1, bomb_type2, bomb_type3]:
        # 현재 폭탄으로 초토화되는 좌표들
        new_coords = bomb_func(x, y)
        
        # 기존 set에 합치기
        new_destroyed = destroyed_set | new_coords
        
        # 다음 폭탄으로 진행
        backtrack(idx + 1, new_destroyed)

# 백트래킹 시작
backtrack(0, set())

print(max_area)

    