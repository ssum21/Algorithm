import sys

input = sys.stdin.readline
max_value = sys.maxsize

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

minimum_cost = distance[0] * cost[0]
now_cost = cost[0]

for i in range(1, len(distance)):
    if cost[i] < now_cost:
        now_cost = cost[i]
    minimum_cost += now_cost * distance[i]


print(minimum_cost)