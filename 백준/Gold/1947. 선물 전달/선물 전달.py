import sys

input = sys.stdin.readline

N = int(input())

D = [0] * (N+5)
D[0] = 0
D[1] = 0
D[2] = 1
D[3] = 2

for i in range(3, N+1):
    D[i] = ((i-1) * (D[i-2] + D[i-1]))%1000000000

print(D[N])