import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
d = defaultdict(list)

for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    d[country].append(gold)
    d[country].append(silver)
    d[country].append(bronze)

arr = sorted(d.items(), key=lambda x:(x[1][0], x[1][1], x[1][2]), reverse=True)

rank = 1
for i in range(len(arr)):
    if i > 0 and arr[i][1] != arr[i-1][1]:
        rank = i + 1
    if arr[i][0] == K:
        print(rank)
        break
