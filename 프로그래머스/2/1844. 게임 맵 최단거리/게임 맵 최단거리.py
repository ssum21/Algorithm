from collections import deque

def solution(maps):
        
    x = 0
    y = 0
    answer = 0

    
    max_x = len(maps[0])
    max_y = len(maps)
    
    queue = deque([(0, 0, 1)])
    visited = [[False]* max_x for _ in range(max_y)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == max_x -1 and y == max_y -1:
            return dist
        
        for i in range(4):
            next_loc_x = x + dx[i]
            next_loc_y = y + dy[i]
        
            if next_loc_x >= 0 and next_loc_x < max_x and next_loc_y >= 0 and next_loc_y < max_y:
                if maps[next_loc_y][next_loc_x] == 1 and not visited[next_loc_y][next_loc_x]:
                    queue.append((next_loc_x, next_loc_y, dist+1))
                    visited[next_loc_y][next_loc_x] = True
                    
    return -1

            