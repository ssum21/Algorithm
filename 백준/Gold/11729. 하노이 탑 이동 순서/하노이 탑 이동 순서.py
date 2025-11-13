import sys
from collections import deque
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
count = 0
result = []
def hanoi(n, start, end, temp):
    global count, result
    if n == 1:
        count += 1
        result.append((start, end))
        return
    hanoi(n-1, start, temp, end)
    count += 1
    result.append((start, end))
    hanoi(n-1, temp, end, start)

hanoi(n, 1, 3, 2)
print(count)
for s, e in result:
    print(s, e)

