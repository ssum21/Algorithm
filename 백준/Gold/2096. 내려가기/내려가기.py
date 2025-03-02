import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [0]*7
for i in range(1, N+1):
    a, b, c = map(int, input().split())
    j, k, l = dp[0], dp[1], dp[2]
    m, n, o = dp[3], dp[4], dp[5]
    dp[0] = max(j, k) + a
    dp[1] = max(j, k, l) + b
    dp[2] = max(k, l) + c

    dp[3] = min(m, n) + a
    dp[4] = min(m, n, o) + b
    dp[5] = min(n, o) + c


print(max(dp[0], dp[1], dp[2]), end=' ')
print(min(dp[3], dp[4], dp[5]))


