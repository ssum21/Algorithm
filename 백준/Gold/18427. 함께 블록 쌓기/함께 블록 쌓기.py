import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
backpack = []
for _ in range(n):
    backpack.append(list(map(int, input().split())))

dp_table = [[0 for _ in range(h+1)] for _ in range(n+1)]
dp_table[0][0] = 1

for i in range(1, n+1):
    for j in range(h+1):
        dp_table[i][j] += dp_table[i-1][j]

    for k in backpack[i-1]:
        for l in range(h, k-1, -1):
            dp_table[i][l] += dp_table[i-1][l-k]

print(dp_table[n][h]%10007)