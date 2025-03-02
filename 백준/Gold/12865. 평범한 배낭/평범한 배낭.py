import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())

items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

def promising(i):
    if i<=K:
        return True
    else:
        return False
thing = [0] * (K+1)

for W, V in items:
    for current_wieght in range(K, W-1 , -1):
        thing[current_wieght] = max(thing[current_wieght], thing[current_wieght-W]+V)

result = 0

for j in thing:
    if (result < j) :
        result = j

print(result)
