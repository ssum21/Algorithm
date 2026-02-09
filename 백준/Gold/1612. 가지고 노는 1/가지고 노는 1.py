import sys
input = sys.stdin.readline

N = int(input().strip())

if N % 2 == 0 or N % 5 == 0:
    print(-1)
    sys.exit()

visited = [False] * N
r = 0
k = 0

while True:
    r = (r * 10 + 1) % N
    k += 1
    if r == 0:
        print(k)
        break
    if visited[r]:
        print(-1)
        break
    visited[r] = True
