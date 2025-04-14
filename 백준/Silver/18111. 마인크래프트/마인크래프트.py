import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
min_height = min(map(min, ground))
max_height = max(map(max, ground))
result_time = float('inf')
result_height = 0

for target in range(min_height, max_height + 1):
    remove = 0
    add = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > target:
                remove += ground[i][j] - target
            else:
                add += target - ground[i][j]
    if remove + b >= add:
        time = remove * 2 + add
        if time <= result_time:
            result_time = time
            result_height = target

print(result_time, result_height)
