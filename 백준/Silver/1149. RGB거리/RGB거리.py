import sys

input = sys.stdin.readline

N = int(input())

a = []
for i in range(N):
    a.append(list(map(int, input().split())))

DP_table = [[0 for _ in range(3)] for _ in range(N+1)]

DP_table[0][0] = a[0][0]
DP_table[0][1] = a[0][1]
DP_table[0][2] = a[0][2]

for i in range(1, N):
    for j in range(3):
        DP_table[i][j] = min(DP_table[i-1][(j+1)%3], DP_table[i-1][(j+2)%3]) + a[i][j]

print(min(DP_table[N-1][0],DP_table[N-1][1],DP_table[N-1][2]))