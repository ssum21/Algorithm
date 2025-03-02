import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
a = []
result = [[0]*n for i in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n): # 경유지
    for j in range(n): # 출발지
        for k in range(n): #도착지
            if(a[j][i] == 1 and a[i][k] == 1):
                a[j][k] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()