import sys

input = sys.stdin.readline
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

INF = sys.maxsize
delta = [-1, 0, 1]  # d=0 left-down, d=1 down, d=2 right-down

dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for d in range(3):
        dp[0][j][d] = a[0][j]

for i in range(1, N):
    for j in range(M):
        for d in range(3):
            pj = j - delta[d]
            if 0 <= pj < M:
                best_prev = INF
                for pd in range(3):
                    if pd != d:
                        best_prev = min(best_prev, dp[i-1][pj][pd])
                dp[i][j][d] = a[i][j] + best_prev

ans = min(dp[N-1][j][d] for j in range(M) for d in range(3))
print(ans)
