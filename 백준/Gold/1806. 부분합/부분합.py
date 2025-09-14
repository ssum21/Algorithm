import sys
from collections import deque

input = sys.stdin.readline

n, s = map(int, input().split())
arr = deque(map(int, input().split()))

start, end = 0, 0
tot = 0
min_length = sys.maxsize

while True:
    if tot >= s:
        min_length=(min(min_length, end - start))
        tot -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        tot += arr[end]
        end += 1

if(min_length == sys.maxsize):
    print(0)
else:
    print(min_length)