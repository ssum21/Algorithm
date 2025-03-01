import math
import sys

input = sys.stdin.readline
n = int(input())
arr = [[sys.maxsize]*n for _ in range(n)]
m = int(input())
for i in range(m):
    start, end, weight = map(int, input().split())
    if (arr[start-1][end-1]>weight):
        arr[start-1][end-1] = weight

for i in range(n):
    arr[i][i]=0

for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])

for i in range(n):
    for j in range(n):
        if (arr[i][j] == sys.maxsize):
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()

