import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

graph = defaultdict(list)

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))

dist = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

now_x, now_y = 0, 0

q = deque([(0, 0, False)])
dist[0][0][0] = 1

while q:
    x, y, jump = q.popleft()
    if x == m-1 and y == n-1:
            print(dist[y][x][jump])
            sys.exit(0)
    for dx, dy in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
        if 0<=dx<m and 0<=dy<n:
                if arr[dy][dx] == 0 and dist[dy][dx][jump] == 0:
                    q.append((dx, dy, jump))
                    dist[dy][dx][jump] = dist[y][x][jump] + 1
                elif arr[dy][dx] == 1 and jump == False and dist[dy][dx][1] == 0:
                    q.append((dx, dy, True))
                    dist[dy][dx][1] = dist[y][x][jump] + 1

print(-1)
