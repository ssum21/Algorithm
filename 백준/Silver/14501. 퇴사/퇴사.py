import sys
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
T=[0] * (n+1)
P=[0] * (n+1)
tot = []
maxvalue = [0] * (n+2)

for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())

for i in range(n, 0, -1):
    if(i + T[i] > n+1):
        maxvalue[i] = maxvalue[i+1]
    else:
        maxvalue[i] = max(maxvalue[i+T[i]]+P[i], maxvalue[i+1])

print(maxvalue[1])


