import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([N])
length = 100000
visited = [False for _ in range(length+1)]
visited[N] = True
ways = [sys.maxsize for _ in range(length+1)]
ways[N] = 0
chance = 0
parent = [-1] * (length + 1)

while q:
    value = q.popleft()
    if(value == K):
        print(ways[K])
        break
    for index in (value-1, value+1, value*2):
        if 0<=index<=length:
            if not visited[index]:
                visited[index] = True
                ways[index] = min(ways[value] + 1, ways[index])
                parent[index] = value
                q.append(index)

path = []
curr = K
while curr != -1:
    path.append(curr)
    curr = parent[curr]
path.reverse()  # N에서 K로 가는 경로로 만들기 위해 뒤집기

# 경로 출력 (각 정수를 공백으로 구분)
print(" ".join(map(str, path)))
