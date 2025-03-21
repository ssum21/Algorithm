import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp_table = [[[0, 0, 0] for _ in range(n+1)] for _ in range(n+1)] # 0 대각선 1 세로 2 가로

dp_table[0][1][2] = 1 

for i in range(n):
    for j in range(n):
        if (graph[i][j]==1): continue
        if j>0:
            dp_table[i][j][2] += dp_table[i][j-1][0] + dp_table[i][j-1][2]
        if i>0:
            dp_table[i][j][1] += dp_table[i-1][j][0] + dp_table[i-1][j][1]
        if i>0 and j>0:
            if graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp_table[i][j][0] += dp_table[i-1][j-1][0] + dp_table[i-1][j-1][1] + dp_table[i-1][j-1][2] 
        

print(dp_table[n-1][n-1][0] + dp_table[n-1][n-1][1] + dp_table[n-1][n-1][2])
