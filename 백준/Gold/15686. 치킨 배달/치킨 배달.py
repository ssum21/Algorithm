import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
chicken_graph = []
house_loc = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 2:
            chicken_graph.append((i, j))
        elif row[j] == 1:
            house_loc.append((i, j))

min_total_distance = sys.maxsize

for chicken_comb in combinations(chicken_graph, m):
    total_distance = 0
    for hx, hy in house_loc:
        distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chicken_comb)
        total_distance += distance
    min_total_distance = min(min_total_distance, total_distance)

print(min_total_distance)